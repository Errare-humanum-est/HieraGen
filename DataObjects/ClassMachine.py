from DataObjects.ClassArchitecture import Architecture
from Algorithms.General.Tracing.TraceTree import *


class Machine:
    def __init__(self, arch: Architecture):
        self.arch: Architecture = arch
        self.covered_traces: List[Trace] = []

        self.start_state: State = self.arch.init_state
        self.final_state: State = self.arch.init_state
        self.cur_trace: Trace = None

        # TODO: ADD LITMUS INSTRUCTION SEQUENCE HERE
        self.test_exe_sequence = None
    '''
    def _get_traces(self):
        traces = []
        for state_set in self.arch.state_sets:
            traces += create_loop_trace_tree(self.arch.state_sets[state_set].getstablestate(),
                                             self.arch.stable_state_str)
        return TraceSet(traces)
    '''

    def __str__(self):
        return str(self.arch)

    def __hash__(self):
        return hash((str(self.arch), str(self.start_state), str(self.final_state), str(self.cur_trace),
                     str(self.test_exe_sequence)))

    def update_mach_arch(self, arch: Architecture):
        self.arch = arch
        self.start_state = arch.init_state
        self.final_state = arch.init_state

    def add_trace(self, trace: Trace) -> 'Machine':
        new_machine_state = copy.copy(self)
        new_machine_state.cur_trace = trace
        new_machine_state.start_state = trace.startstate
        new_machine_state.final_state = trace.finalstate
        # Add trace to the covered traces
        if trace not in self.covered_traces:
            self.covered_traces.append(trace)
        return new_machine_state

    def add_idle(self) -> 'Machine':
        new_machine_state = copy.copy(self)
        new_machine_state.cur_trace = None
        new_machine_state.start_state = new_machine_state.final_state
        # Add trace to the covered traces
        return new_machine_state

    def get_start_state(self) -> [State, Trace]:
        if self.cur_trace:
            return self.cur_trace.startstate
        else:
            return self.start_state

    def get_final_state(self) -> [State, Trace]:
        if self.cur_trace:
            return self.cur_trace.finalstate
        else:
            return self.final_state

    def get_trace(self) -> Trace:
        return self.cur_trace

    def get_mach_state_trace_id(self) -> int:
        if self.cur_trace:
            return id(self.cur_trace)
        else:
            ret_val = 0
            if self.start_state:
                ret_val += id(self.start_state)
            if self.final_state:
                ret_val += id(self.final_state)
            return ret_val

    def get_mach_state_trace_str(self) -> str:
        if self.cur_trace:
            return str(self.cur_trace)
        else:
            ret_str = ""
            if self.start_state:
                ret_str += str(self.start_state)
                if self.final_state and self.final_state == self.start_state:
                    return ret_str
                if self.final_state:
                    ret_str += " -> "
            if self.final_state:
                ret_str += str(self.final_state)
            return ret_str

    def test_equivalence(self, mach: 'Machine') -> bool:
        if not isinstance(mach, Machine):
            return False

        if (self.start_state == mach.start_state and
                self.final_state == mach.final_state and
                self.cur_trace == mach.cur_trace):
            return True
        return False
