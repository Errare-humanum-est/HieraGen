# Instead of having everything in the parser make for every architecture a single object that contains all
# important information

from Algorithms.General.GenStates import create_states
from Algorithms.General.GenStateSets import *
from Algorithms.HieraAlgorithm.HieraStateTupleClass.StateClassification import *
from Graphv.ProtoCCGraph import ProtoCCGraph
from Algorithms.General.GenStateSets import StateSets, extract_states_from_sets

from Algorithms.General.AuxStateHandler import AuxStateHandler

from antlr3.tree import CommonTree
from DataObjects.ClassProtoCCObject import PCCObject

from General.ArchitectureClassification import ArchitectureClassification


class Architecture(ArchitectureClassification):
    def __init__(self, parser: ProtoParser, arch_name: str,
                 transitions: [List[Transition], None] = None,
                 stable_state_str: [List[str], None] = None,
                 init_state: str = None,
                 unique_id: List[str] = None,
                 data_constant: Dict[str, CommonTree] = None,
                 data_object: PCCObject = None):

        ArchitectureClassification.__init__(self, parser, arch_name)

        # Parser variables
        self.parser: ProtoParser = parser
        self.arch_name: str = arch_name

        self.access_def: List[str] = parser.Access
        self.evict_def: List[str] = parser.Evict

        # Parser Object Description
        self.data_constant: Dict[str, CommonTree] = data_constant
        if not data_constant:
            self.data_constant: Dict[str, CommonTree] = copy.deepcopy(parser.getConstants())

        self.data_object = data_object
        if not data_object:
            self.data_object = copy.deepcopy(parser.get_mach_nodes()[arch_name])

        # Algorithm data objects
        self.transitions = transitions
        self.stable_state_str = stable_state_str

        if not transitions:
            self.transitions = parser.getArchitectures()[arch_name]

        if not stable_state_str:
            self.stable_state_str = parser.getStableStates()[arch_name]

        self.remove_state_assignments(self.transitions)

        self.initial_states: Dict[str, State] = create_states(self.transitions, self.access_def, self.evict_def)

        self.state_sets: StateSets[str, StateSet] = create_statesets(self.initial_states, self.stable_state_str)
        self.stable_states = self.state_sets.get_stable_states()

        if init_state:
            init_state_str = init_state
        else:
            init_state_str = parser.getInitStates()[arch_name]
        self.init_state = self.state_sets[init_state_str].getstablestate()

        # Variables that can externally be changed
        self.raw_traces = assign_statesets(self.state_sets, parser, arch_name, self.stable_state_str)
        self.traces: TraceSet = TraceSet(self.raw_traces)

        self.state_classification = self.state_classification_func()

        # Dict old message, new message
        self.renamed_messages: Dict[str, str] = {}

        # Murphi
        self.unique_id = [arch_name]
        if unique_id:
            self.unique_id = unique_id

    def update_trans_operation(self, cur_var: str, new_var: str):
        for transition in self.transitions:
            transition.rename_operation(cur_var, new_var)

    def update_data_operation(self, cur_var: str, new_var: str):
        AuxStateHandler.cond_operations_var_rename(self.data_object.structure.children, cur_var, new_var)

    def update_const_var_names(self):
        pass

    def update_data_and_var_names(self, add_str: str):
        old_new_var_name_dict = {}

        var_data_objects = self.data_object.get_var_object_dict()
        # Update the variable definition names
        for var_name in var_data_objects:

            # Don't rename states
            if var_name in self.initial_states:
                continue

            old_new_var_name_dict[var_name] = var_name + add_str
            AuxStateHandler.cond_operations_var_rename(var_data_objects[var_name].children,
                                                       var_name,
                                                       var_name + add_str)
        # Update the variable dictionary names
        self.data_object.variables = self.data_object.get_var_object_dict()

        # Update the variable names in the operations
        for renamed_var in old_new_var_name_dict:
            for transition in self.transitions:
                AuxStateHandler.cond_operations_var_rename(transition.operation,
                                                           renamed_var,
                                                           old_new_var_name_dict[renamed_var],
                                                           self.get_message_name_str_list())

    def update_msg_names(self, old_msg_name, new_msg_name):
        self.renamed_messages[old_msg_name] = new_msg_name
        for transition in self.transitions:
            transition.rename_inmsg_operation(old_msg_name, new_msg_name)
            transition.rename_outmsg_operation(old_msg_name, new_msg_name)

    def __str__(self):
        return self.get_arch_name()

    # MURPHI BACKEND FUNCTIONS
    def update_unique_id(self, add_str: str) -> List[str]:
        self.update_data_and_var_names(add_str)
        self.unique_id.append(add_str)
        return self.unique_id

    def get_unique_id(self) -> List[str]:
        return self.unique_id

    def get_unique_id_str(self):
        return ''.join(self.unique_id)

    def get_unique_id_level(self):
        tmp_list = copy.copy(self.unique_id)
        tmp_list.remove(self.arch_name)
        return ''.join(tmp_list)

    def get_arch_name(self) -> str:
        return self.arch_name

    def get_constants(self) -> Dict[str, CommonTree]:
        return self.data_constant

    def get_data_object(self) -> Dict[str, PCCObject]:
        return {self.get_unique_id_str(): self.data_object}

    def get_states(self) -> Dict[str, State]:
        return extract_states_from_sets(self.state_sets)

    def get_stable_states(self) -> List[State]:
        return self.stable_states

    def get_transitions(self) -> List[Transition]:
        return self.transitions

    def get_message_name_str_list(self) -> List[str]:
        msg_name_str = []
        for transition in self.transitions:
            if str(transition.inMsg):
                msg_name_str.append(str(transition.inMsg))
            msg_name_str += [str(outMsg) for outMsg in transition.outMsg if str(outMsg)]
        msg_name_str += list(self.renamed_messages.keys())
        return list(set(msg_name_str))

    def test_token(self, token: str) -> bool:
        for transition in self.transitions:
            for operation in transition.operation:
                if str(operation) == token:
                    return True
        return False

    # ALGORITHM WRITE BACK FUNCTIONS
    def state_classification_func(self) -> Dict[State, StateClassification]:
        state_classification = {}
        for state_set in self.state_sets.values():
            stable_state = state_set.getstablestate()
            state_classification[stable_state] = StateClassification(stable_state, self.traces)
        return state_classification

    def update_traces(self):
        self.raw_traces = assign_statesets(self.state_sets, self.parser, self.arch_name, self.stable_state_str)
        self._update_transitions()
        self.traces = TraceSet(self.raw_traces)

    def get_trace_by_state(self, search_state: State) -> List[Trace]:
        traces = []
        for state in self.traces.start_state_dict:
            for trace in self.traces.start_state_dict[state]:
                for transition in trace.transitions:
                    if transition.startState == search_state or transition.finalState == search_state:
                        traces.append(trace)
        return traces

    def get_trace_by_transition(self):
        return False

    def remove_state_assignments(self, transitions: List[Transition]):
        for transition in transitions:
            remove_operation = []
            for operation in transition.operation:
                tokens = operation.getChildren()
                if tokens[0].getText() == ProtoParser.State:
                    remove_operation.append(operation)

            assert len(remove_operation) <= 1, "Too many state assignments detected"

            for operation in remove_operation:
                transition.operation.remove(operation)

    def _update_transitions(self):
        for state in extract_states_from_sets(self.state_sets).values():
            for transition in state.gettransitions():
                if transition not in self.transitions:
                    self.transitions.append(transition)

    def update_transitions(self):
        self.update_traces()

    # OUTPUT FUNCTIONS
    def draw_controller(self):
        ProtoCCGraph("Spec: " + self.arch_name, self.transitions)

    def print_controller_info(self, cluster_id: str = ""):
        print(cluster_id + self.arch_name)
        ProtoCCTablePrinter().ptransitiontable(self.transitions)
