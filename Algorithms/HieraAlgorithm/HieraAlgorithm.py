import copy
from typing import Tuple

from Algorithms.HieraAlgorithm.HieraStateTupleClass.ControllerMappings import *

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassLevel import Level
from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition
from DataObjects.ClassCommClassification import CommunicationClassification
from Algorithms.HieraAlgorithm.HieraStateTupleClass.HieraStateTuple import HieraStateTuple
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Murphi.MurphiModular import MurphiModular

from Monitor.ProtoCCTable import *
from Graphv.ProtoCCGraph import ProtoCCGraph

from Algorithms.HieraAlgorithm.HieraStateSpaceGen.HieraStateSpaceGen import HieraStateSpaceGen
from Algorithms.HieraAlgorithm.HieraTransGen.HieraTransGen import HieraTransGen
from Algorithms.HieraAlgorithm.HieraGraph import HieraGraph

from Monitor.ClassDebug import Debug

# Hierachy evict
enable_non_inclusive = 0


class HieraGen(HieraStateSpaceGen, HieraTransGen, HieraGraph, Debug):

    def __init__(self, low_level: Level, high_level: Level, dbg_term: bool = False, dbg_graph: bool = False):

        Debug.__init__(self, dbg_term)
        self.dbg_graph = dbg_graph

        # for each ll state, add corresponding dir state and possible higher level cache states
        # higher level cache permissions are greater or equal to lower level state permissions

        # Lower level cache optimization
        # Optimization flag: Accesses that do hit in the higher level cache, do not cause the generation of
        self.ll_access_immed_hit = True

        # Higher level cache optimization
        # Optimization flag: Remote access are not conveyed to the lower level cache, if the hl trace final state has
        # lower access permissions than the current lower level caches
        self.hl_remote_immed_hit = True

        self.pessimistic_access = True

        self.complete_defer = False

        self.conservative_access_ll_request = True
        self.conservative_access_hl_request = True

        self.unique_id_str = "HIERA"
        self.unique_id = [self.unique_id_str]

        # Update messages to avoid conflicts for non-stalling implementations
        self.detect_message_dependencies(low_level, high_level)

        self.low_level: Level = copy.deepcopy(low_level)
        self.high_level: Level = copy.deepcopy(high_level)

        self.low_level.update_mach_name_operation(self.low_level.directory.get_unique_id_str(), self.unique_id_str)
        self.high_level.update_mach_name_operation(self.high_level.cache.get_unique_id_str(), self.unique_id_str)

        self.merge_data_objects()

        self.low_level.update_traces()
        self.high_level.update_traces()

        self.init_tuple: HieraStateTuple = HieraStateTuple(self.low_level.init_tuple, self.high_level.cache.init_state)

        ''' Get access mappings from lower level cache controller '''
        self.ll_access_map = access_request_mapping(self.low_level.cache.state_sets)

        self.cc_dir_to_cc_state_map: Dict[State, List[State]] = {}
        self.cc_dir_to_dir_state_map: Dict[State, List[State]] = {}

        # Do the child init here
        HieraStateSpaceGen.__init__(self, self.low_level, self.high_level)
        """ Generate State Transitions """
        HieraTransGen.__init__(self, self.low_level, self.high_level)
        HieraGraph.__init__(self, self.init_tuple, self.low_level, self.high_level)

        # Make new states based on new_state_tuples
        self.cc_dir_transitions = self.cc_dir_fsm_states()

        # Generate new stabel state nodes
        self.stable_states = self.create_cc_dir_states(self.access_state_tuples + self.remote_state_tuples +
                                                        self.ll_evict_state_tuples + self.hl_evict_state_tuples)
        if self.dbg:
            self.print_debug_info()

        # New init_state_id
        new_state_name = self.new_state_name(self.init_tuple.ll_dir_start_state.state,
                                                    self.init_tuple.hl_cc_start_state.state)

        # Make a new architecture
        self.low_level.directory = Architecture(self.low_level.directory.parser,
                                self.low_level.directory.arch_name,
                                self.cc_dir_transitions,
                                list(self.stable_states.keys()),
                                new_state_name,
                                self.unique_id,
                                self.low_level.directory.data_constant,
                                self.low_level.directory.data_object
                                )

        # Make a new architecture
        self.high_level.cache = Architecture(self.high_level.directory.parser,
                                self.high_level.cache.arch_name,
                                self.cc_dir_transitions,
                                list(self.stable_states.keys()),
                                new_state_name,
                                self.unique_id,
                                self.high_level.cache.data_constant,
                                self.high_level.cache.data_object
                                )

        self.replace_archs = [low_level.directory, high_level.cache]

    def get_renamed_messages(self) -> Dict[str, str]:
        return dict(self.low_level.renamedMessages, **self.high_level.renamedMessages)

    def get_controller_level(self):
        return self.low_level, self.high_level

    def print_debug_info(self):
        cc_dir_type = self.low_level.proto_type + "|" + self.high_level.proto_type
        self.pheader("Generated Hierachical SSP Controller: " + cc_dir_type)
        ProtoCCTablePrinter(self.dbg).ptransitiontable(self.cc_dir_transitions)

        if self.dbg_graph:
            ProtoCCGraph("Spec: " + cc_dir_type, self.cc_dir_transitions)

    @staticmethod
    def detect_message_dependencies(low_level: Level, high_level: Level):
        ll_dir_in_message_ids = []
        hl_dir_in_message_ids = []

        for transition in low_level.directory.transitions:
            ll_dir_in_message_ids.append(str(transition.inMsg))
        for transition in low_level.cache.transitions:
            ll_dir_in_message_ids.append(str(transition.inMsg))

        for transition in high_level.cache.transitions:
            hl_dir_in_message_ids.append(str(transition.inMsg))

        msg_name_conflicts = list(filter(None, set(ll_dir_in_message_ids).intersection(set(hl_dir_in_message_ids))))

        for msg_name_conflict in msg_name_conflicts:
            low_level.update_message_name(msg_name_conflict, msg_name_conflict + low_level.get_unique_id_str())

    def merge_data_objects(self):
        data_obj_dir_dict = self.low_level.directory.data_object.get_var_object_dict()
        data_obj_proxy_dict = self.low_level.cache.data_object.get_var_object_dict()
        data_obj_cache_dict = self.high_level.cache.data_object.get_var_object_dict()
        if len(set(data_obj_dir_dict.keys()).intersection(set(data_obj_cache_dict.keys()))) > 0:
            self.pwarning("HIERAGEN: Multiple variable name conflicts detected, no automatic solution yet")

        data_obj_dir_dict.update(data_obj_proxy_dict)
        data_obj_dir_dict.update(data_obj_cache_dict)

        # Only a single init state is allowed
        init_var_list = []
        for obj_var in data_obj_dir_dict:
            if str(data_obj_dir_dict[obj_var]) == MurphiModular.tINITSTATE:
                init_var_list.append(obj_var)

        for ind in range(1, len(init_var_list)):
            data_obj_dir_dict.pop(init_var_list[ind])
            self.update_trans_operation_vars(init_var_list[ind], init_var_list[0])

        # Only a single cache block is allowed
        data_var_list = []
        for obj_var in data_obj_dir_dict:
            if str(data_obj_dir_dict[obj_var]) == MurphiModular.tDATA:
                data_var_list.append(obj_var)
        for ind in range(1, len(data_var_list)):
            data_obj_dir_dict.pop(data_var_list[ind])
            self.update_trans_operation_vars(data_var_list[ind], data_var_list[0])

        var_nodes = list(data_obj_dir_dict.values())
        self.low_level.directory.data_object.structure.children = var_nodes
        self.high_level.cache.data_object.structure.children = var_nodes
        self.low_level.directory.data_object.getvarnames(self.low_level.directory.data_object.structure.children)
        self.high_level.cache.data_object.getvarnames(self.high_level.cache.data_object.structure.children)

    def update_trans_operation_vars(self, cur_var: str, new_var: str):
        self.low_level.cache.update_trans_operation(cur_var, new_var)
        self.low_level.directory.update_trans_operation(cur_var, new_var)
        self.high_level.cache.update_trans_operation(cur_var, new_var)


    """
    ####################################################################################################################
    ##### Make new states
    ####################################################################################################################
    """

    def cc_dir_fsm_states(self) -> List[Transition]:
        renamed_states = {}  # Dict[old cc or dir state, new cc_dir state]

        # Cache ll access transitions
        ll_access_trans = self.ll_cache_access_transitions(renamed_states, self.access_state_tuples)

        ll_upgrade_trans = self.ll_cache_upgrade_transitions(renamed_states, self.upgrade_state_tuples)

        # Cache hl_remote transitions
        remote_trans = self.hl_cache_remote_transitions(renamed_states, self.remote_state_tuples)

        # Evict transitions
        ll_evict_trans = self.ll_cache_evict_transitions(renamed_states,
                                                         self.ll_evict_state_tuples)

        hl_evict_trans = self.cc_dir_evict_transitions(renamed_states, self.hl_evict_state_tuples)

        # Create state looping transitions
        loop_trans_cc = []
        loop_trans_cc = self.cc_dir_loop_transitions(self.cc_dir_to_cc_state_map)
        loop_trans_dir = []
        loop_trans_dir = self.cc_dir_loop_transitions(self.cc_dir_to_dir_state_map)

        all_cc_dir_transitions = ll_access_trans + ll_upgrade_trans + remote_trans + ll_evict_trans + hl_evict_trans + \
                                 loop_trans_cc + loop_trans_dir

        # Remove duplicates
        cc_dir_transitions = self.trans_list_hash_reduction(all_cc_dir_transitions)

        return cc_dir_transitions

    def create_cc_dir_states(self, state_tuples: List[CcDirStateTuple]) -> Dict[str, State]:
        # Detect terminal states, every new state must have an edge that leads to a different new state
        cc_dir_start_state_tuples: Dict[Tuple[State, State], Tuple[State, State]] = {}
        cc_dir_final_state_tuples: Dict[Tuple[State, State], Tuple[State, State]] = {}
        for state_tuple in state_tuples:
            start_tuple = (state_tuple.ll_dir_start_state, state_tuple.hl_cc_start_state)
            cc_dir_start_state_tuples[start_tuple] = start_tuple
            final_tuple = (state_tuple.ll_dir_final_state, state_tuple.hl_cc_final_state)
            cc_dir_final_state_tuples[final_tuple] = final_tuple

        # Translate load and store accesses into message types
        new_access_list = []
        accesses = self.low_level.cache.init_state.access
        for access in accesses:
            for access_type in self.ll_access_map[access]:
                new_access_list.append(access_type)

        evict = self.low_level.cache.init_state.evict

        cc_dir_states = {}

        for cc_dir_state_tuple in set(cc_dir_final_state_tuples).intersection(cc_dir_start_state_tuples):
            state_str = self.new_state_name(str(cc_dir_state_tuple[0]), str(cc_dir_state_tuple[1]))
            new_state = State(state_str, new_access_list, evict)
            cc_dir_states[str(new_state)] = new_state

        return cc_dir_states


    ####################################################################################################################
    # Add looping transitions
    ####################################################################################################################
    def cc_dir_loop_transitions(self, state_map_dict: Dict[State, List[State]]) -> List[Transition]:
        all_transitions = []
        for cc_dir_state in state_map_dict:
            for mapped_single_layer_state in state_map_dict[cc_dir_state]:
                if str(mapped_single_layer_state) in self.low_level.directory.stable_state_str:
                    continue
                for transition in mapped_single_layer_state.gettransitions():
                    if transition.comm_class != CommunicationClassification.resp:
                        continue

                    # if the transition loops
                    if transition.startState == transition.finalState and not transition.access:
                        new_trans = copy.copy(transition)
                        new_state = State(str(cc_dir_state), transition.startState.access, transition.startState.evict)
                        new_trans.startState = new_state
                        new_trans.finalState = new_state
                        all_transitions.append(new_trans)

        ret_transitions = self.trans_list_hash_reduction(all_transitions)
        return ret_transitions

    @staticmethod
    def trans_list_hash_reduction(cache_transitions: List[Transition]):
        transistions = {}

        for cache_transition in cache_transitions:
            trans_hash = cache_transition.get_hash()
            if trans_hash not in transistions:
                transistions[trans_hash] = cache_transition

        return list(transistions.values())
