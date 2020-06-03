# Contains two architectures, cache and associated directory, and runs all the basic pre processing algorithms
# A class level is the input to the hierachical and protogen algorithm
import copy

from graphviz import Digraph
from typing import List, Union, Set

from Algorithms.General.AuxStateHandler import AuxStateHandler

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassStateTuple import StateTuple
from DataObjects.ClassState import State

from DataObjects.ClassCommClassification import CommunicationClassification

from Algorithms.ModelChecker.ModelChecker import ModelChecker
from DataObjects.ClassSystemTuple import SystemTuple
from DataObjects.ClassMachine import Machine
from DataObjects.ClassProtoCCObject import PCCObject
from Algorithms.General.GenStateSets import extract_states_from_sets

from Algorithms.NetworkAnalysis.ClassNetworkClassification import ClassNetworkClassification

from Monitor.ClassDebug import Debug

from DataObjects.ClassMultiDict import MultiDict


class Level(Debug):
    def __init__(self, parser,
                 level_id: str,
                 proto_type=None,
                 run_model_checker: bool = True,
                 debug_enabled: bool = False):

        Debug.__init__(self, debug_enabled)

        self.pheader("LEVEL: " + level_id)

        self.parser = parser
        self.level_id: str = level_id
        self.proto_type: str = proto_type
        self.state_tuple_list: List[SystemTuple] = []
        self.dir_access_classification_map = {}

        # Preprocessing make messages unique
        self.renamedMessages = {}
        self.progressMessages = []
        self.hiddenChangeStates = []

        self.model_checker = None

        # Classify communication
        CommunicationClassification().classify_parser(parser)

        self.message_objects: List[PCCObject] = parser.getMessageNodes()

        # Cache
        caches = list(parser.getCacheIdentifiers())
        assert len(caches) <= 1, "Maximum number of architectures per parser supported is 1"
        self.cache = Architecture(parser, caches[0])

        # Cache preprocessing
        self.find_progress_messages(self.cache.state_sets)
        self.find_hidden_progess_messages(self.cache.state_sets)

        # # Make decision between memory and directory
        snoop = False
        directory = list(parser.getDirIdentifiers())
        if not directory:
            snoop = True
            directory = list(parser.getMemIdentifiers())

        assert len(directory) <= 1, "Maximum number of architectures per parser supported is 1"
        self.directory = Architecture(parser, directory[0])

        if not snoop:
            # Detect directory message type conflicts
            self.renamedMessages.update(self.process_remote_requests(self.cache.state_sets, self.cache.raw_traces))
            self.cache.update_traces()

            # Resolve directory message type conflicts
            self.process_request_messages(self.renamedMessages, self.directory.state_sets)
            # Only handle silent upgrades and different request messages
            self.complete_transitions(self.cache.state_sets, self.directory.state_sets, False)

        # Update the traces
        self.cache.update_traces()
        self.directory.update_traces()

        # INITIAL MODEL CHECKING
        self.init_tuple = StateTuple(self.cache.init_state, self.directory.init_state, self.cache.init_state)
        self.level_name = "Level: " + str(level_id) + " | " + str(self.cache) + " && " + str(self.directory)

        if run_model_checker:
            self.initial_model_checking()

        # Complete all eviction transitions at the directory level to account for concurrency
        self.complete_transitions(self.cache.state_sets, self.directory.state_sets)
        # Update the traces
        self.cache.update_traces()
        self.directory.update_traces()

        self.cache.renamed_messages = self.renamedMessages
        self.directory.renamed_messages = self.renamedMessages

        # Classify cache and directory transitions

        # Murphi
        self.unique_id = []

        # Update machine names in operations
        self.update_mach_name_operation_append(level_id)

        self.network_class = ClassNetworkClassification(parser, self.cache.transitions)

    # MURPHI BACKEND FUNCTIONS
    def update_unique_id(self, add_str: str) -> List[str]:
        self.unique_id.append(add_str)
        return self.unique_id

    def get_unique_id(self) -> List[str]:
        return self.unique_id

    def get_unique_id_str(self):
        return ''.join(self.unique_id)

    def getCacheStates(self):
        return {self.level_id + self.cache.arch_name: extract_states_from_sets(self.cache.state_sets)}

    def getDirStates(self):
        return {self.level_id + self.directory.arch_name: extract_states_from_sets(self.directory.state_sets)}

    def getMsgStrings(self):
        msg_list = []
        for transition in self.cache.transitions + self.directory.transitions:
            trans_msgs = [transition.inMsg] + transition.outMsg
            for trans_msg in trans_msgs:
                if str(trans_msg) not in msg_list:
                    msg_list.append(str(trans_msg))
        return msg_list

    # Update the message send function names
    def update_send_function_names(self, sub_id: str):
        for message_object in self.message_objects:
            # Update Transitions
            cur_send_name = message_object.name
            new_send_name = cur_send_name + sub_id
            self.update_trans_operations(cur_send_name, new_send_name)
            message_object.name = new_send_name
            AuxStateHandler.cond_operations_var_rename(message_object.structure.children, cur_send_name, new_send_name)

    def update_message_name(self, old_msg_name, new_msg_name):
        # Update the progress messages
        if old_msg_name in self.progressMessages:
            self.progressMessages.remove(old_msg_name)
            self.progressMessages.append(new_msg_name)
        self.cache.update_msg_names(old_msg_name, new_msg_name)
        self.directory.update_msg_names(old_msg_name, new_msg_name)
        self.renamedMessages[old_msg_name] = new_msg_name

    def update_trans_operations(self, old_mach_name: str, new_mach_name: str):
        # Update Transitions
        self.cache.update_trans_operation(old_mach_name, new_mach_name)
        self.directory.update_trans_operation(old_mach_name, new_mach_name)

    # Update all machine names
    def update_mach_name_operation(self, old_mach_name: str, new_mach_name: str):
        # Update Transitions
        self.update_trans_operations(old_mach_name, new_mach_name)
        # Update Data Objects
        self.cache.update_data_operation(old_mach_name, new_mach_name)
        self.directory.update_data_operation(old_mach_name, new_mach_name)

    def update_mach_name_operation_append(self, sub_id: str):
        mach_names = {self.cache.get_unique_id_str(): self.cache.get_unique_id_str() + sub_id,
                      self.directory.get_unique_id_str(): self.directory.get_unique_id_str() + sub_id}

        for mach_name in mach_names:
            self.update_mach_name_operation(mach_name, mach_names[mach_name])

        # Update the send names
        self.update_send_function_names(sub_id)

        self.cache.update_unique_id(sub_id)
        self.directory.update_unique_id(sub_id)
        self.update_unique_id(sub_id)

    def update_traces(self):
        self.cache.update_traces()
        self.directory.update_traces()

    # MIGRATED FROM PROTOGEN
    def getMessages(self):
        msglist = copy.copy(self.parser.getMessages())

        replacemsg = []

        for message in msglist:
            if message in self.renamedMessages:
                replacemsg.append(message)
                for assignment in self.renamedMessages[message]:
                    msglist.append(assignment)

        return [msg for msg in msglist if msg not in replacemsg]

    def getRenamedMessages(self):
        return self.renamedMessages

    ####################################################################################################################
    # AGGRESSIVELY DEFER RESPONSE MESSAGES
    ####################################################################################################################
    def find_progress_messages(self, statesets):
        statedict = extract_states_from_sets(statesets)

        for state in statedict:
            if statedict[state].getstartstatesets():
                for transition in statedict[state].gettransitions():
                    if not transition.getfinalstate().getstartstatesets():
                        if not transition.getguard() in self.progressMessages:
                            self.progressMessages.append(transition.getguard())

    def find_hidden_progess_messages(self, statesets):
        statedict = extract_states_from_sets(statesets)

        for state in statedict:
            for transition in statedict[state].gettransitions():
                outmsgtypes = transition.getoutmsgtypes()
                for outmsg in outmsgtypes:
                    if outmsg in self.progressMessages and len(outmsgtypes) > 1:
                        for outmsgadd in outmsgtypes:
                            if outmsgadd not in self.progressMessages:
                                self.progressMessages.append(outmsgadd)
                    break

    ####################################################################################################################
    # 4) PREPROCESSING
    ####################################################################################################################
    ####################################################################################################################
    # CACHE
    ####################################################################################################################

    # In every state all remote requests should be unique
    def process_remote_requests(self, statesets, traces):
        # Get message identifiers
        messagesets = {}
        for stateset in statesets:
            messagesets.update(
                {statesets[stateset].getstablestate().getstatename():
                     set([transition.getguard() for transition in
                          statesets[stateset].getstablestate().getremote()])})


        # Detect conflicts
        conflicts = []
        for refset in messagesets:
            for compset in messagesets:
                refentry = messagesets[refset]
                compentry = messagesets[compset]
                if refset != compset:
                    conflict = refentry.intersection(compentry)
                    if conflict:
                        entry = [{refset, compset}, conflict]
                        if entry not in conflicts:
                            conflicts.append(entry)

        connectivity_pairs = self.get_trace_connectivity_pairs(traces)
        silent_upgrade_pairs = self.get_state_connectivity_pairs(statesets)


        renamedmsg = {}
        # Resolve guard name conflicts
        rename_msg_dict = {}
        covered_msg_dict = {}
        for conflict in conflicts:
            if conflict[0] in connectivity_pairs:
                for messageid in conflict[1]:
                    for setid in conflict[0]:
                        equiv_set = set(setid)
                        for upgrade_pair in silent_upgrade_pairs:
                            if setid in upgrade_pair:
                                equiv_set.update(upgrade_pair)

                        for cur_set in equiv_set:
                            stateset = statesets[cur_set]
                            newmessageid = messageid + "_" + setid


                            if messageid in covered_msg_dict:
                                if cur_set in covered_msg_dict[messageid]:
                                    continue

                            if messageid not in rename_msg_dict:
                                rename_msg_dict.update({messageid: [[cur_set, newmessageid]]})
                                covered_msg_dict.update({messageid: [setid]})
                            else:
                                rename_msg_dict[messageid].append([cur_set, newmessageid])
                                covered_msg_dict[messageid].append(cur_set)

                            states = stateset.getstates()
                            for state in states:
                                transition = state.gettransitionbyguard(messageid)
                                assert not isinstance(transition, list), "No support yet for transition list"
                                if transition:
                                    transition.rename_inmsg_operation(messageid, newmessageid)
                                    transition.rename_outmsg_operation(messageid, newmessageid)
                                    transition.replaceguard(newmessageid)

                            renamedmsg.update(rename_msg_dict)

        self.pheader("Renamed Messages:")
        self.pdebug(renamedmsg)

        return renamedmsg

    def get_state_connectivity_pairs(self, state_sets) -> List[Set[str]]:
        connectivity_pairs = []
        for state_set in state_sets:
            cur_stable_state = state_sets[state_set]
            for trans in cur_stable_state.getstablestate().getaccesshit():
                if trans.startState != trans.finalState:
                    connectivity_pairs.append({str(trans.startState), str(trans.finalState)})

        return connectivity_pairs


    def get_trace_connectivity_pairs(self, traces):
        pairs = []
        for trace in traces:
            pair = {trace[-1].get_state().getstatename(), trace[0].get_state().getstatename()}
            if trace[0].get_transition().getinmsg() or trace[0].get_transition().getoutmsg():
                if pair not in pairs:
                    pairs.append(pair)
            else:
                if pair not in self.hiddenChangeStates:
                    self.hiddenChangeStates.append(pair)
        return pairs

    ####################################################################################################################
    # DIRECTORY
    ####################################################################################################################
    def process_request_messages(self, renamedmessages, statesets):
        for message in renamedmessages:
            curname = message
            for repentry in renamedmessages[message]:
                newname = repentry[1]
                stateset = repentry[0]

                for state_sets in self.hiddenChangeStates:
                    if str(stateset) in state_sets:
                        for new_stateset in state_sets:

                            if new_stateset not in statesets:
                                self.perror("Messages need to be renamed, "
                                            + "but ProtoGen cannot determine dependencies at directory")

                            for state in statesets[new_stateset].getstates():
                                transitions = state.gettransitions()

                                for transition in transitions:
                                    transition.rename_inmsg_operation(curname, newname)
                                    transition.rename_outmsg_operation(curname, newname)
                                    transition.renameoutmsg(curname, newname)



    ####################################################################################################################
    # 9) DIR MEMORY ACCESS COMPLETION
    ####################################################################################################################

    def complete_transitions(self, cache_state_sets, dir_state_sets, non_hidden_evict: bool = True):
        cache_state_sets = list(cache_state_sets.values())
        res = self.access_detection(cache_state_sets)
        self.access_completion(dir_state_sets, res[0])
        self.evict_completion(dir_state_sets, res[1], non_hidden_evict)

    def access_detection(self, cachestatesets):
        accessmap = {}

        [accessmap.update({access: []}) for access in self.parser.Access + self.parser.Evict]

        states = []

        for stateset in cachestatesets:
            states += stateset.getstates()

        for state in states:

            for transition in state.getaccessmiss() + state.getevictmiss():
                accesslist = accessmap.get(transition.getguard(), 0)

                if isinstance(accesslist, list):
                    outmsgs = transition.getoutmsg()
                    for outmsg in outmsgs:
                        accesslist.append(outmsg.getmsgtype())

        # seperate evict accesses
        evictaccess = {}

        for evict in self.parser.Evict:
            evictaccess.update({evict: accessmap[evict]})
            del accessmap[evict]

        return [accessmap, evictaccess]

    def access_completion(self, dirstatesets, accessmap):
        dirstates = extract_states_from_sets(dirstatesets)
        # Only multiple messages related to same access must be considered
        for access in accessmap:
            if len(accessmap[access]) > 1:
                msgtypes = accessmap[access]

                for state in dirstates.values():
                    foundmap = {}
                    misskeys = []
                    for msgtype in msgtypes:
                        transition = state.getmulttransitionsbyguard(msgtype)
                        if transition:
                            foundmap.update({msgtype: transition})
                        else:
                            misskeys.append(msgtype)

                    if len(foundmap):
                        for misskey in misskeys:
                            transitions = foundmap[next(iter(foundmap))]

                            for transition in transitions:
                                newtrans = copy.copy(transition)
                                newtrans.rename_inmsg_operation(str(transition.getinmsg()), misskey)
                                state.addtransitions(newtrans)

    def evict_completion(self, dirstatesets, evictaccess, non_hidden_evict):
        dirstates = extract_states_from_sets(dirstatesets)
        # The possible evictions need to be present in every state due to race conditions
        evictmap = {}
        evictmsgstatemap = {}

        for evict in evictaccess:
            for state in dirstates.values():
                for evictmsg in evictaccess[evict]:
                    transitions = state.getmulttransitionsbyguard(evictmsg)
                    if transitions:
                        for transition in transitions:
                            transarray = evictmap.get(evictmsg, 0)
                            if transarray:
                                if transition not in transarray:
                                    transarray.append(transition)
                            else:
                                evictmap.update({evictmsg: [transition]})
                                evictmsgstatemap.update({state.getstatename(): evictmsg})

        # Handle cache states that are indistinguishable by directory such as E and M
        stateevictmap = {}

        for stateset in dirstatesets:
            state = dirstatesets[stateset].getstablestate().getstatename()
            for pair in self.hiddenChangeStates:
                if state in pair:
                    for entry in pair:
                        if entry != state:
                            if entry in stateevictmap:
                                stateevictmap[entry].append(evictmap[state])
                            else:
                                if state in evictmsgstatemap:
                                    stateevictmap.update({entry: [evictmsgstatemap[state]]})

        # Evictions only need to be possible in stable states
        # Transient states automatically inherit from stable states
        for stateset in dirstatesets:
            state = dirstatesets[stateset].getstablestate()
            for evictaccess in evictmap:

                existtrans = state.getmulttransitionsbyguard(evictaccess)
                if existtrans:
                    continue

                for newevicttrans in evictmap[evictaccess]:

                    evicttranskey = newevicttrans.getguard() + "".join(newevicttrans.getcond())

                    found = 0

                    # UNREACHABLE
                    # TODO: OLD STUPID COPY OPERATIONS TO BE REMOVED
                    #if existtrans:
                    #    for transition in existtrans:
                    #        transkey = transition.getguard() + "".join(transition.getcond())

                    #        if transkey in evicttranskey or evicttranskey in transkey:
                    #            found = 1

                    if not found:
                        hiddenstatetrans = 0
                        if state.getstatename() in stateevictmap:
                            if evictaccess in stateevictmap[state.getstatename()]:
                                hiddenstatetrans = 1

                        if hiddenstatetrans:
                            if newevicttrans.getstartstate() == newevicttrans.getfinalstate():
                                state.addtransitions(newevicttrans.copy_modify_trans(state, state))
                            else:
                                state.addtransitions(newevicttrans.copy_modify_trans(state,
                                                                                newevicttrans.getfinalstate()))
                        else:
                            if non_hidden_evict:
                                state.addtransitions(newevicttrans.copy_modify_trans(state, state))

    ####################################################################################################################
    # MODEL CHECKING
    ####################################################################################################################
    def initial_model_checking(self):

        # Modelchecking load store AND evict
        mod_check = ModelChecker([self.cache, self.directory], True, True)          # evicts
        access_state_tuple_list = mod_check.single_cache_directory_state_space()
        self._generate_dir_access_classification_map(access_state_tuple_list)

        if self.dbg:
            mod_check.draw_allowed_system_tuples()

        self.model_checker = mod_check
        self.state_tuple_list += access_state_tuple_list

    def _get_dir_state_machine(self, state_tuple: SystemTuple) -> Machine:
        dir_machine = state_tuple.get_arch_machines(self.directory)
        assert len(dir_machine) == 1, "More than one dir state not supported"

        return dir_machine[0]

    def _get_cc_access_state_machine(self, state_tuple: SystemTuple) -> Union[Machine, None]:
        access_machine = []
        for machine in state_tuple.system_tuple:
            if machine.cur_trace and machine.cur_trace.access:
                access_machine.append(machine)

        assert len(access_machine) <= 1, "More than one dir state not supported"

        if access_machine:
            return access_machine[0]
        return None

    def _generate_dir_access_classification_map(self, access_state_tuple_list: List[SystemTuple]):
        for state_tuple in access_state_tuple_list:
            dir_machine = self._get_dir_state_machine(state_tuple)
            access_machine = self._get_cc_access_state_machine(state_tuple)

            if not access_machine:
                continue
            self._update_dir_access_classification_map(dir_machine.start_state, access_machine.cur_trace.startstate)
            self._update_dir_access_classification_map(dir_machine.final_state, access_machine.cur_trace.finalstate)

    def _update_dir_access_classification_map(self, dir_state: State, cc_state: State):
        cur_classification = self.cache.state_classification[cc_state]
        if dir_state in self.dir_access_classification_map:
            if self.dir_access_classification_map[dir_state] <= cur_classification:
                self.dir_access_classification_map[dir_state] = cur_classification
        else:
            self.dir_access_classification_map[dir_state] = cur_classification

    # Model checking preparation, extend directory stable state description evict response

    ####################################################################################################################
    # Drawing functions
    ####################################################################################################################

    def draw_system_tuples(self, state_tuples: List[StateTuple]):
        self._draw_system_tuples(state_tuples, self._draw_assymmetric_system_tuple)

    def draw_symmetric_system_tuples(self, state_tuples: List[StateTuple]):
        self._draw_system_tuples(state_tuples, self._draw_symmetric_system_tuple)

    def _draw_system_tuples(self, state_tuples: List[StateTuple], edge_gen_func):
        edges = {}
        graph = Digraph(comment=self.level_name, engine='dot')

        prev_tuples = [self.init_tuple]
        next_tuples = []

        while prev_tuples:
            for state_tuple in state_tuples:
                if state_tuple.prev_tuple in prev_tuples:
                    next_tuples.append(state_tuple)

            for next_tuple in next_tuples:
                edge = edge_gen_func(next_tuple)
                if str(edge) not in edges:
                    edges[str(edge)] = edge
                    graph.edge(*edge[0],
                               label=edge[1])

            prev_tuples = next_tuples
            next_tuples = []

        graph.render('level_state_tuples/' + self.level_name + '.gv', view=True)

    @staticmethod
    def _draw_assymmetric_system_tuple(tuple):
        return [(tuple.draw_str_start_state(), tuple.draw_str_final_state()), tuple.str_access_trace()]

    @staticmethod
    def _draw_symmetric_system_tuple(tuple):
        return [(tuple.symmetric_str_start_state(),
                 tuple.symmetric_str_final_state()),
                tuple.symmetric_str_access_trace()]

