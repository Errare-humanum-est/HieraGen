from DataObjects.ClassState import State
from Algorithms.General.Tracing.TraceTree import Trace


class CcDirStateTuple:

    def __init__(self, ll_dir: [State, Trace, None] = None,
                 hl_cc: [State, Trace, None] = None,
                 ll_proxy: [State, Trace, None] = None,
                 ll_access_cc: [Trace, None] = None):

        self.ll_dir_start_state: State = None
        self.ll_dir_final_state: State = None
        self.ll_dir_trace: Trace = None

        self.ll_proxy_start_state: State = None
        self.ll_proxy_final_state: State = None
        self.ll_proxy_trace: Trace = None

        self.hl_cc_start_state: State = None
        self.hl_cc_final_state: State = None
        self.hl_cc_trace: Trace = None

        self.ll_access_cc_trace: Trace = ll_access_cc

        self.update_hl_cc(hl_cc)
        self.update_ll_cc_dir(ll_proxy)
        self.update_ll_dir(ll_dir)

    def __str__(self):
        retstr = self._str_cond(self.ll_dir_start_state, self.ll_dir_final_state, self.ll_dir_trace) + "; "
        retstr += "\"" + self._str_cond(self.ll_proxy_start_state, self.ll_proxy_final_state, self.ll_proxy_trace) + \
                  "\"; "
        retstr += self._str_cond(self.hl_cc_start_state, self.hl_cc_final_state, self.hl_cc_trace)

        return retstr

    @staticmethod
    def _str_cond(start_state, end_state, trace) -> str:
        if trace:
            str_trace = ""
            for node in trace.trace:
                if not node.transition:
                    str_trace += str(node.state) + " --> "
            return str_trace + str(end_state)

        else:
            if start_state != end_state:
                return str(start_state) + " --> " + str(end_state)
            else:
                return str(end_state)

    def __hash__(self):
        return hash((self.ll_dir_start_state, self.ll_dir_final_state, self.ll_dir_trace,
                     self.ll_proxy_start_state, self.ll_proxy_final_state, self.ll_proxy_trace,
                     self.hl_cc_start_state, self.hl_cc_final_state, self.hl_cc_trace))

    def __eq__(self, other: 'CcDirStateTuple'):
        if isinstance(other, CcDirStateTuple):
            # Only ll_cc_dir, ll_dir and hl_cc are relevant
            # However, here we do a complete equality check
            if self.ll_dir_start_state == other.ll_dir_start_state and \
                    self.ll_dir_final_state == other.ll_dir_final_state and \
                    self.ll_dir_trace == other.ll_dir_trace and \
                    \
                    self.ll_proxy_start_state == other.ll_proxy_start_state and \
                    self.ll_proxy_final_state == other.ll_proxy_final_state and \
                    self.ll_proxy_trace == other.ll_proxy_trace and \
                    \
                    self.hl_cc_start_state == other.hl_cc_start_state and \
                    self.hl_cc_final_state == other.hl_cc_final_state and \
                    self.hl_cc_trace == other.hl_cc_trace:
                return True
        return False

    def update_ll_dir(self, ll_cc: [State, Trace]):
        if isinstance(ll_cc, State):
            self.ll_dir_start_state = ll_cc
            self.ll_dir_final_state = ll_cc
        elif isinstance(ll_cc, Trace):
            self.ll_dir_start_state = ll_cc.startstate
            self.ll_dir_final_state = ll_cc.finalstate
            self.ll_dir_trace = ll_cc
        else:
            assert "Unknown data type @ ll_cc_dir"

    def update_ll_cc_dir(self, ll_cc: [State, Trace]):
        if isinstance(ll_cc, State):
            self.ll_proxy_start_state = ll_cc
            self.ll_proxy_final_state = ll_cc
        elif isinstance(ll_cc, Trace):
            self.ll_proxy_start_state = ll_cc.startstate
            self.ll_proxy_final_state = ll_cc.finalstate
            self.ll_proxy_trace = ll_cc
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

    # Drawing
    def draw_str_start_state(self) -> str:
        return str(self.ll_dir_start_state) + "; " + str(self.hl_cc_start_state)

    def draw_str_final_state(self) -> str:
        return str(self.ll_dir_final_state) + "; " + str(self.hl_cc_final_state)

    # Drawing
    def str_start_state(self) -> str:
        return str(self.ll_dir_start_state) + str(self.hl_cc_start_state)

    def str_final_state(self) -> str:
        return str(self.ll_dir_final_state) + str(self.hl_cc_final_state)
