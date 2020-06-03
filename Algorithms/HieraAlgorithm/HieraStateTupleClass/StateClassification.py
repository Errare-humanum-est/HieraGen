from typing import List
from DataObjects.ClassState import State
from Algorithms.General.Tracing.TraceTree import TraceSet
from Algorithms.General.GenStateSets import StateSets


class StateClassification:

    def __init__(self, state: State, traces: TraceSet):
        self.state: State = state

        self.enter_access: List[str] = []   # Accesses whose traces can lead to state
        self.immed_access: List[str] = []   # Accesses possible in state
        self.request_access: List[str] = [] # Accesses that trigger requests
                                            # (actually not necessary since complementary to immed_access

        self.enter_evict: List[str] = []   # Accesses whose traces can lead to state
        self.immed_evict: List[str] = []   # Accesses possible in state
        self.request_evict: List[str] = [] # Accesses that trigger requests
                                            # (actually not necessary since complementary to immed_access

        self.add_enter_access(state, traces)
        self.add_immed_request_access(state)

    def __str__(self):
        return str(self.state)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: 'StateClassification'):
        if isinstance(other, StateClassification):
            #if set(self.enter_access) == set(other.enter_access) and set(self.immed_access) == set(other.immed_access):
            if set(self.immed_access) == set(other.immed_access):
                return True
        return False

    def __le__(self, other: 'StateClassification'):
        if isinstance(other, StateClassification):
            # e.g. load <= store and no_evict<=evict
            if self._get_index(self.immed_access) <= self._get_index(other.immed_access):
                # and self._get_index(self.immed_evict) <= self._get_index(other.immed_evict):
                return True
        return False

    # Get the maximum index of permitted accesses
    def _get_index(self, access_list: List[str]) -> int:
        # return 0 if there is no access at all
        max_ind = [0]
        for access in access_list:
            max_ind.append(self.state.access.index(access)+1)
        return max(max_ind)

    def add_enter_access(self, state: State, traces: TraceSet) -> None:
        if state not in traces.final_state_dict:
            return

        enter_traces = traces.final_state_dict[state]

        for entry in enter_traces:
            for access in entry.access:
                if access:
                    if access in state.get_access_str() and access not in self.enter_access:
                        self.enter_access.append(access)
                    elif access in state.get_evict_str() and access not in self.enter_evict:
                        self.enter_evict.append(access)
                    else:
                        assert "Unrecognized access"

    def add_immed_request_access(self, state: State) -> None:
        for transition in state.gettransitions():
            # If an access can be performed without awaiting a response, important not request,
            # it can still make a request
            if transition.getaccess() in state.get_access_str():
                if transition.getoutmsg():
                    self.request_access.append(transition.getaccess())
                else:
                    self.immed_access.append(transition.getaccess())

            elif transition.getaccess() in state.get_evict_str():
                if transition.getoutmsg():
                    self.request_evict.append(transition.getaccess())
                else:
                    self.immed_evict.append(transition.getaccess())
            else:
                assert "Unrecognized access"


class StateSetClassification:

    def __init__(self, statesets: StateSets, traces: TraceSet):
        self.state_classification = {}
        for stateset in statesets.values():
            stable_state = stateset.getstablestate()
            self.state_classification[stable_state] = StateClassification(stable_state, traces)






