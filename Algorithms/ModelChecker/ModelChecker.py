from copy import copy
from graphviz import Digraph
from typing import List, Tuple, Dict
from DataObjects.ClassState import State
from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassMachine import Machine
from DataObjects.ClassSystemTuple import SystemTuple

from Parser.ForkTree import ForkTree
from Algorithms.General.Tracing.TraceNode import TraceNodeObj

from itertools import permutations


class ModelChecker:
    def __init__(self, archs: List[Architecture], longest_trace: bool = True, handle_evicts: bool = True):
        self.archs: List[Architecture] = archs

        self.allowed_state_tuples: Dict[SystemTuple, SystemTuple] = {}
        self.forbidden_state_tuples: Dict[SystemTuple, SystemTuple] = {}

        # Iteration count
        self.search_iterations = 0

        # Options
        self.longest_trace = longest_trace  # Only selects the longest trace if multiple actions compete
        self.handle_evicts = handle_evicts  # Only if enabled evict accesses are being served



    def set_longest_trace(self, longest_trace: bool = True):
        self.longest_trace = longest_trace

    def set_handle_evicts(self, handle_evicts: bool = True):
        self.handle_evicts = handle_evicts

    def single_cache_directory_state_space(self) -> List[SystemTuple]:
        state_tuples = []

        evict_state_tuples = []
        safe_tuple_upper_bound = None

        if self.handle_evicts:
            evict_state_tuples = self.gen_mc_sd_state_space()
            safe_tuple_upper_bound = len(evict_state_tuples[0]) - 1

        # The safe state tuples do not include evictions and are always safe
        safe_state_tuples = self.gen_mc_sd_state_space(False, safe_tuple_upper_bound)
        for state_tuple in safe_state_tuples:
            self.allowed_state_tuples[state_tuple] = state_tuple

        self.search_iterations = len(safe_state_tuples) - 1

        # Build evict tree to include system state tuples that are only reachable through evictions
        if self.handle_evicts:
            state_tuples = self.build_evict_tree(evict_state_tuples)

        return state_tuples

    # Generate state space for a single directory and for multiple caches
    def gen_mc_sd_state_space(self, handle_evicts: bool = True, loop_count: int = None) -> List[SystemTuple]:
        ind_iter = 0
        old_complete_cnt = 0
        state_tuples = []
        old_reduced_set_tuples = {}

        if loop_count is not None:
            assert loop_count != 0, "The iteration loop count must be at least one"

        while True:
            init_tuple = SystemTuple(self.gen_mult_cc_single_dc(ind_iter))

            machine_state_tuple_dict = self.single_access_new_state_tuples(init_tuple, handle_evicts)

            new_complete_cnt = self.check_machine_completion(init_tuple)
            new_reduced_set_tuples = dict([state_tuple.get_reduced_set()
                                           for state_tuple in machine_state_tuple_dict.values()])

            # Compare state space based on trace coverage and more important sets of different state space combinations!
            if (new_complete_cnt == old_complete_cnt and
                set(new_reduced_set_tuples.keys()) == set(old_reduced_set_tuples.keys())) and \
                    loop_count is None:
                # Remove the init tuple from the state space as it is only a dummy start point
                # and does not contain actual traces
                #state_tuples.pop(0)
                return state_tuples

            # Save the additional state space
            state_tuples = [init_tuple] + list(machine_state_tuple_dict.values())
            # Add cache
            ind_iter += 1

            old_complete_cnt = new_complete_cnt
            old_reduced_set_tuples = new_reduced_set_tuples

            if loop_count is not None and ind_iter >= loop_count:
                # Remove the init tuple from the state space as it is only a dummy start point
                # and does not contain actual traces
                #state_tuples.pop(0)
                return state_tuples

    def check_machine_completion(self, system_tuple: SystemTuple) -> int:
        archs = []
        machines = []
        for machine in system_tuple.system_tuple:
            if machine.arch not in archs:
                archs.append(machine.arch)
                machines.append(machine)

        trace_cnt = 0
        for machine in machines:
            trace_cnt += len(machine.covered_traces)

        return trace_cnt

    def gen_mult_cc_single_dc(self, ind_iter=0):
        mach_list = []
        for arch in self.archs:
            mach_list.append(Machine(arch))

        mach_comb = []
        for ind in range(0, ind_iter + 1):
            mach_comb.append(copy(mach_list[0]))

        mach_comb.append(mach_list[1])
        mach_comb = tuple(mach_comb)

        return mach_comb

    def single_access_new_state_tuples(self, initial_tuple: SystemTuple, handle_evicts: bool = True) \
            -> Dict[int, SystemTuple]:
        cur_tuples = [initial_tuple]
        next_tuples = {}
        state_tuples = {}

        # Make new tuple for system state [ll_CC_State, Dir_State, hl_CC_State]
        while cur_tuples:
            for cur_tuple in cur_tuples:
                # Permutate tuple
                pre_perm_list = list(permutations(cur_tuple.system_tuple))

                # Reduce permutation list
                perm_list = self.reduce_permutation_states(pre_perm_list)

                for perm in perm_list:
                    # Execute accesses
                    next_tuples.update(self.single_access_find_next_tuple(perm, handle_evicts))

            cur_tuples = []
            for next_tuple in next_tuples:
                if next_tuple not in state_tuples:
                    cur_tuples.append(next_tuples[next_tuple])
                    state_tuples[next_tuple] = next_tuples[next_tuple]
            next_tuples = {}

        return state_tuples

    def single_access_find_next_tuple(self, cur_tuple: Tuple[Machine], handle_evicts: bool = True):
        # If no access can be found this is not as bad as if multiple accesses cannot be served
        new_tuples = {}
        new_traces = []
        request_machine: Machine = cur_tuple[0]
        remote_machines: List[Machine] = cur_tuple[1:]

        # self.debug_assert(cur_tuple)

        for trace in request_machine.arch.traces.start_state_dict[request_machine.final_state]:
            if not trace.access:
                continue
            else:
                evict_exists = 0
                for access in trace.access:
                    if access in request_machine.arch.evict_def and not handle_evicts:
                        evict_exists = 1
                        break
                if evict_exists:
                    continue

            trace_tree = ForkTree()
            basenode = trace_tree.insertnode(TraceNodeObj(request_machine, trace))
            nextlist = self.find_next_trace_nodes([basenode], remote_machines)

            while nextlist:
                endnodes = []
                for nextnode in nextlist:
                    endnodes += trace_tree.append_data_list(nextnode[1], nextnode[0])

                nextlist = []
                for node in endnodes:
                    nextlist += self.find_next_trace_nodes([node], remote_machines)

            new_traces += self.validate_traces(trace_tree.gettraces())

        if self.longest_trace:
            longest_new_traces = self.find_longest_traces(new_traces)
            # Register transactions taken
            self.make_new_system_tuple(cur_tuple, [x for x in new_traces if x not in longest_new_traces])
            new_traces = longest_new_traces

        new_system_tuples = self.make_new_system_tuple(cur_tuple, new_traces)

        for new_system_tuple in new_system_tuples:
            new_tuples[new_system_tuple.__hash__()] = new_system_tuple

        return new_tuples

    def debug_assert(self, machines: Tuple[Machine]):
        # Tuple size
        if len(machines) != 3:
            return

        if set([str(machine.final_state) for machine in machines]) == {'I', 'S', 'I'}:
            print('FOUND')

    def find_next_trace_nodes(self, nodes: List[TraceNodeObj],
                              remote_machines: List[Machine]) -> List[Tuple[TraceNodeObj, List[List[TraceNodeObj]]]]:
        next_nodes = []

        for node in nodes:
            nextlist = []
            prev_machines = [node.data.state]
            prev_traces = [node.data.transition]
            cur_node = node
            while cur_node.predecessor:
                prev_machines.append(cur_node.predecessor.data.state)
                prev_traces.append(cur_node.predecessor.data.transition)
                cur_node = cur_node.predecessor

            outmsg_list = [str(outmsg) for trace in prev_traces for outmsg in trace.outmsg]
            inmsg_list = [str(inmsg) for trace in prev_traces for inmsg in trace.inmsg]

            pending_mach = set(remote_machines) - set(prev_machines)

            # trace is complete
            if set(inmsg_list) == set(outmsg_list):
                continue

            # while new traces are found
            for machine in pending_mach:
                for trace in machine.arch.traces.start_state_dict[machine.final_state]:
                    # No parallel accesses allowed!
                    if trace.access:
                        continue
                    trace_in_msg_list = [str(in_msg) for in_msg in trace.inmsg]
                    if set(trace_in_msg_list).intersection(set(outmsg_list)):
                        new_trace_object = TraceNodeObj(machine, trace)
                        nextlist.append(new_trace_object)

            # Cluster machines based on transition ids
            cluster_nextlist = {}
            for trace_node in nextlist:
                if id(trace_node.transition) in cluster_nextlist:
                    cluster_nextlist[id(trace_node.transition)].append(trace_node)
                else:
                    cluster_nextlist[id(trace_node.transition)] = [trace_node]

            clusters = list(cluster_nextlist.values())

            next_nodes.append((node, clusters))

        return next_nodes

    @staticmethod
    def validate_traces(traces: List[List[TraceNodeObj]]) -> List[List[TraceNodeObj]]:
        validated_traces = []
        for trace in traces:
            prev_machines = []
            prev_traces = []
            for node in trace:
                prev_machines.append(node.state)
                prev_traces.append(node.transition)
            outmsg_list = [str(outmsg) for trace in prev_traces for outmsg in trace.outmsg]
            inmsg_list = [str(inmsg) for trace in prev_traces for inmsg in trace.inmsg]

            if set(inmsg_list) != set(outmsg_list):
                continue
            validated_traces.append(trace)
        return validated_traces

    @staticmethod
    def find_longest_traces(traces: List[List[TraceNodeObj]]):
        trace_access_map = {}
        for trace in traces:
            access = trace[-1].transition.access[0]
            if access in trace_access_map:
                if len(trace_access_map[access][0]) < len(trace):
                    trace_access_map[access] = [trace]
                elif len((trace_access_map[access])[0]) == len(trace):
                    trace_access_map[access].append(trace)
            else:
                trace_access_map[access] = [trace]

        return [trace for access in trace_access_map for trace in trace_access_map[access]]

    @staticmethod
    def make_new_system_tuple(cur_tuple: Tuple[Machine],
                              traces: List[List[TraceNodeObj]]):
        system_tupels = []
        for trace in traces:
            prev_machines = []
            prev_traces = []
            for node in trace:
                prev_machines.append(node.state)
                prev_traces.append(node.transition)
            outmsg_list = [str(outmsg) for trace in prev_traces for outmsg in trace.outmsg]
            inmsg_list = [str(inmsg) for trace in prev_traces for inmsg in trace.inmsg]

            if set(inmsg_list) != set(outmsg_list):
                continue

            mach_copies = []
            for machine, mach_trace in zip(prev_machines, prev_traces):
                mach_copies.append(machine.add_trace(mach_trace))

            mach_idle = []
            # Process idle machines
            for machine in list(set(cur_tuple) - set(prev_machines)):
                mach_idle.append(machine.add_idle())

            system_tupels.append(SystemTuple(tuple(mach_copies + mach_idle)))

        return system_tupels

    # Reduce permutation start state
    @staticmethod
    def reduce_permutation_states(tuple_list: List[Tuple[Machine]]):
        start_states: List[State] = []
        reduced_tuple_list: List[Tuple[Machine]] = []
        for system_tuple in tuple_list:
            start_state = system_tuple[0].final_state
            if start_state not in start_states:
                start_states.append(system_tuple[0].final_state)
                reduced_tuple_list.append(system_tuple)

        return reduced_tuple_list

    def build_evict_tree(self, system_tuple_list: List[SystemTuple]) -> List[SystemTuple]:
        evicts = []
        for arch in self.archs:
            for evict in arch.evict_def:
                if evict not in evicts:
                    evicts.append(evict)

        # Trace to make evict tree, the list should be ordered in a way that all evictions are anyway leading to previous
        # evict states (Single for loop over all states sufficient, but check if all evict traces have been covered
        # The init tuple is always safe

        assert system_tuple_list, "No system tuple found by model checker"

        safe_states = [system_tuple_list[0].get_final_state_set()] + \
                      [system_tuple.get_final_state_set() for system_tuple in self.allowed_state_tuples.values()]
        cur_len = 0
        while cur_len < len(safe_states):
            cur_len = len(safe_states)
            for state_tuple in system_tuple_list:
                for access_trace in state_tuple.get_arch_access_trace():
                    for access in access_trace.access:
                        if access in evicts:
                            if state_tuple.get_final_state_set() in safe_states:
                                if state_tuple.get_start_state_set() not in safe_states:
                                    safe_states.append(state_tuple.get_start_state_set())
                            # If no interaction with the directory is required, it is also a safe trace as it is atomic
                            elif not access_trace.outmsg:
                                if state_tuple.get_start_state_set() in safe_states:
                                    if state_tuple.get_final_state_set() not in safe_states:
                                        safe_states.append(state_tuple.get_final_state_set())

        for system_tuple in system_tuple_list:
            if system_tuple.get_start_state_set() in safe_states and \
                    system_tuple.get_final_state_set() in safe_states:
                self.allowed_state_tuples[system_tuple] = system_tuple
            else:
                self.forbidden_state_tuples[system_tuple] = system_tuple

        return list(self.allowed_state_tuples.values())

    def draw_allowed_system_tuples(self):
        self.draw_system_tuples(list(self.allowed_state_tuples.values()))

    @staticmethod
    def draw_system_tuples(system_tuple_list: List[SystemTuple]):

        for system_tuple in system_tuple_list:
            system_tuple.get_permutation_machines()

        if system_tuple_list:
            name = "SystemTupleOutput"
        else:
            return
        graph = Digraph(comment=name, engine='dot')

        state_tuples = {}
        for state_tuple in system_tuple_list:
            tuple_id = (state_tuple.start_state_tuple_str(),
                        state_tuple.final_state_tuple_str(),
                        state_tuple.access_state_tuple_str())
            state_tuples[tuple_id] = state_tuple

        for state_tuple in state_tuples.values():
            graph.edge(state_tuple.start_state_tuple_str(),
                       state_tuple.final_state_tuple_str(),
                       label=state_tuple.access_state_tuple_str())

        graph.render('level_state_tuples/' + name + '.gv', view=True)
