from typing import Union

from DataObjects.ClassState import State
from Algorithms.General.Tracing.TraceTree import Trace
from DataObjects.ClassStateTuple import StateTuple


class HieraStateTuple(StateTuple):

    def __init__(self, state_tuple: StateTuple = None,
                 hl_cc: [State, Trace, None] = None,
                 ll_cc_dir: [State, Trace, None] = None):
        StateTuple.__init__(self, state_tuple.get_ll_cc(), state_tuple.get_ll_dir(),
                            state_tuple.get_ll_rm(), state_tuple.prev_tuple)

        self.ll_cc_dir_start_state: State = None
        self.ll_cc_dir_final_state: State = None
        self.ll_cc_dir_trace: Trace = None

        self.hl_cc_start_state: State = None
        self.hl_cc_final_state: State = None
        self.hl_cc_trace: Trace = None

        self.update_hl_cc(hl_cc)
        self.update_ll_cc_dir(ll_cc_dir)

    def __str__(self):
        retstr = self._str_cond(self.ll_cc_start_state, self.ll_cc_final_state, self.ll_cc_trace) + "; "
        retstr += "\"" + self._str_cond(self.ll_cc_dir_start_state, self.ll_cc_dir_final_state, self.ll_cc_dir_trace) + "\"; "
        retstr += self._str_cond(self.ll_dir_start_state, self.ll_dir_final_state, self.ll_dir_trace) + "; "
        retstr += self._str_cond(self.hl_cc_start_state, self.hl_cc_final_state, self.hl_cc_trace)

        return retstr

    def __hash__(self):
        return hash((self.ll_cc_start_state, self.ll_cc_final_state, self.ll_cc_trace,
                     self.ll_cc_dir_start_state, self.ll_cc_dir_final_state, self.ll_cc_dir_trace,
                     self.ll_dir_start_state, self.ll_dir_final_state, self.ll_dir_trace,
                     self.hl_cc_start_state, self.hl_cc_final_state, self.hl_cc_trace))

    def __eq__(self, other: 'HieraStateTuple'):
        if isinstance(other, HieraStateTuple):
            # Only ll_cc_dir, ll_dir and hl_cc are relevant
            # However, here we do a complete equality check
            if StateTuple.__eq__(self, other) and \
                    self.ll_cc_dir_start_state == other.ll_cc_dir_start_state and \
                    self.ll_cc_dir_final_state == other.ll_cc_dir_final_state and \
                    self.ll_cc_dir_trace == other.ll_cc_dir_trace and \
                    \
                    self.hl_cc_start_state == other.hl_cc_start_state and \
                    self.hl_cc_final_state == other.hl_cc_final_state and \
                    self.hl_cc_trace == other.hl_cc_trace:
                return True
        return False

    def update_ll_cc_dir(self, ll_cc: [State, Trace]):
        if isinstance(ll_cc, State):
            self.ll_cc_dir_start_state = ll_cc
            self.ll_cc_dir_final_state = ll_cc
        elif isinstance(ll_cc, Trace):
            self.ll_cc_dir_start_state = ll_cc.startstate
            self.ll_cc_dir_final_state = ll_cc.finalstate
            self.ll_cc_dir_trace = ll_cc
        else:
            assert "Unknown data type @ ll_cc_dir"

    def update_hl_cc(self, hl_cc: [State, Trace]):
        if isinstance(hl_cc, State):
            self.hl_cc_start_state = hl_cc
            self.hl_cc_final_state = hl_cc
        elif isinstance(hl_cc, Trace):
            self.hl_cc_start_state = hl_cc.startstate
            self.hl_cc_final_state = hl_cc.finalstate
            self.hl_cc_trace = hl_cc
        else:
            assert "Unknown data type @ hl_cc"

    def get_ll_cc_dir(self) -> Union[State, Trace]:
        if self.ll_cc_dir_trace:
            return self.ll_cc_dir_trace
        else:
            return self.ll_cc_dir_final_state

    def get_hl_cc(self) -> Union[State, Trace]:
        if self.hl_cc_trace:
            return self.hl_cc_trace
        else:
            return self.hl_cc_final_state

    def test_complete(self):
        if self.ll_cc_final_state and self.ll_cc_trace and self.ll_dir_final_state and self.ll_dir_trace and \
                self.hl_cc_final_state and self.hl_cc_trace:
            return 1
        return 0

    # Drawing
    def str_start_state(self) -> str:
        ll_sys = StateTuple.str_start_state(self)
        return ll_sys + "; " + str(self.hl_cc_start_state)

    def str_final_state(self) -> str:
        ll_sys = StateTuple.str_final_state(self)
        return ll_sys + "; " + str(self.hl_cc_final_state)

    def symmetric_str_start_state(self) -> str:
        return str(self.ll_dir_start_state) + "; " + str(self.hl_cc_start_state)

    def symmetric_str_final_state(self) -> str:
        return str(self.ll_dir_final_state) + "; " + str(self.hl_cc_final_state)
