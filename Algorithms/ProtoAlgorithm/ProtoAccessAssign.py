from Algorithms.General.Tracing.TraceTree import create_trace_tree
from Algorithms.General.GenStateSets import extract_states_from_sets

from Algorithms.General.GenStateSets import get_stable_states
from Algorithms.ProtoAlgorithm.ProtoBase import ProtoBase


class ProtoAccessAssign(ProtoBase):

    def __init__(self):
        ProtoBase.__init__(self)
        self.stableStatesOnly = True
        self.conservativeAccess = True
        self.ignoreDeferedStates = False
        self.datamsgs = False
        pass

    ####################################################################################################################
    # 7) TRANSIENT STATE MEMORY ACCESS
    ####################################################################################################################
    def _AssignAccess(self, statesets, stablestates):
        if not self.stableStatesOnly:

            accessdict = {}

            for stateset in statesets.values():

                traces = create_trace_tree(stateset.getstablestate(), stablestates)

                for trace in traces:
                    hasdata = 0
                    lostdata = 0
                    startaccess = trace[len(trace) - 1].get_state().getaccesshit()
                    if len(startaccess):
                        hasdata = 1
                    finalaccess = trace[0].get_state().getaccesshit()

                    for ind in range(len(trace) - 2, 0, -1):
                        state = trace[ind].get_state()

                        startstatesets = state.getstartstatesets()
                        endstatesets = state.getendstatesets()

                        prevdata = hasdata
                        hasdata = self._DetermineHasData(hasdata,
                                                         trace[ind].get_transition(),
                                                         startstatesets,
                                                         endstatesets)

                        # Determine if there was a downgrade once
                        if prevdata and not hasdata:
                            lostdata = 1

                        # Options
                        if self.conservativeAccess and hasdata and not lostdata:
                            if not self.ignoreDeferedStates or not state.getdefermessages():
                                self._ConservativeAccess(accessdict, state, startaccess, finalaccess)
                        # else:

            for state in accessdict:
                access = accessdict[state]
                for entry in access[0]:
                    # If state has not data, there cannot be any acccess, even if possible by
                    if access[1]:
                        if not state.gettransitionbyguard(entry.getguard()):
                            state.addtransitions(self._CopyModifyTransition(entry, state, state))

    def _ConservativeAccess(self, accessdict, state, startaccess, finalaccess):
        if len(startaccess) < len(finalaccess):
            newaccess = startaccess
        else:
            newaccess = finalaccess

        if state in accessdict:
            curaccess = accessdict[state][0]
            curhasdata = accessdict[state][1]

            if curhasdata:
                if len(curaccess) < len(newaccess):
                    accessdict.update({state: [newaccess, 1]})
        else:
            accessdict.update({state: [newaccess, 1]})

    def _DetermineHasData(self, hasdata, transition, startstatesets, endstatesets):
        if startstatesets:
            minaccess = self._DetermineEndMinAccess(startstatesets)

            if not minaccess:
                hasdata = 0
        else:
            endminaccess = self._DetermineEndMinAccess(endstatesets)
            if endminaccess and not hasdata:
                inobj = transition.getinmsg()
                if isinstance(inobj, str):
                    return hasdata
                if inobj.getmsgobj() in self.datamsgs:
                    hasdata = 1

        return hasdata

    @staticmethod
    def _DetermineEndMinAccess(statesets):
        minaccessset = []
        for stateset in statesets:
            stablestate = stateset.getstablestate()
            access = stablestate.getaccesshit()

            if access:
                if not minaccessset:
                    minaccessset = access

                if len(access) < len(minaccessset):
                    minaccessset = access

        return minaccessset

    # def _InheritIntersectAccess(self, statesets):

    def _InheritAccessFromSet(self, statesets):
        states = extract_states_from_sets(statesets)
        states = list(states.values())
        stablestates = get_stable_states(statesets)

        for state in stablestates:
            states.remove(state)

        for state in states:
            startstablestates = state.getstartstatesets()
            endstablestates = state.getendstatesets()

            minaccessset = []
            for stateset in endstablestates:
                stablestate = stateset.getstablestate()
                access = stablestate.getaccesshit()

                if access:
                    if not minaccessset:
                        minaccessset = access

                    if len(access) < len(minaccessset):
                        minaccessset = access

            for stateset in startstablestates:
                stablestate = stateset.getstablestate()
                access = stablestate.getaccesshit()

                if len(access) < len(minaccessset):
                    minaccessset = access

            if minaccessset:
                for access in minaccessset:
                    state.addtransitions(self._CopyModifyTransition(access, state, state))

                # While deferred response access is not changed..., keep memory accesses

