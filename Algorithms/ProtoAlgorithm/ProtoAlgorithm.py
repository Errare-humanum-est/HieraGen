import time

from typing import Tuple, List, Dict

from Algorithms.General.GenStateSets import extract_states_from_sets, StateSet, StateSets
from Algorithms.General.MergeStates import MergeStates

from Algorithms.General.Tracing.TraceTree import Trace
from DataObjects.ClassLevel import Level
from DataObjects.ClassArchitecture import Architecture

from Monitor.ProtoCCTable import *

from Graphv.ProtoCCGraph import ProtoCCGraph

from Algorithms.ProtoAlgorithm.ProtoStalling import ProtoStalling
from Algorithms.ProtoAlgorithm.ProtoNonStalling import ProtoNonStalling
from Algorithms.ProtoAlgorithm.ProtoDir import ProtoDir
from Algorithms.ProtoAlgorithm.ProtoAccessAssign import ProtoAccessAssign

from Monitor.ClassDebug import Debug


class ProtoAlgorithm(ProtoStalling, ProtoNonStalling, ProtoDir, ProtoAccessAssign, Debug):

    def __init__(self, level: Level, config, dbg_term: bool = False, dbg_graph: bool = False):

        ProtoStalling.__init__(self)
        ProtoNonStalling.__init__(self)
        ProtoDir.__init__(self)
        ProtoAccessAssign.__init__(self)
        Debug.__init__(self, dbg_term)
        self.dbg_graph = dbg_graph

        self.debug_all_generated_states = []

        self.level = level

        self.parser = level.parser

        self.datamsgs = level.parser.getDataMsgTypes()

        self.access = level.parser.getAccess()
        self.evict = level.parser.getEvict()

        self.archProtoGen = {}
        self.renamedMessages = level.renamedMessages
        self.hiddenChangeStates = level.hiddenChangeStates

        self.cacheStateSets = []

        self.progressMessages = level.progressMessages

        """ PROTOGEN OPTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        # Options Cache
        self.CCconservativeInv = config.CCconservativeInv
        self.nonstalling = config.nonstalling

        self.maxNestingDepthCC = config.maxNestingDepthCC

        # Options Directory
        self.DCconservativeInv = config.DCconservativeInv
        self.maxNestingDepthDC = config.maxNestingDepthDC

        # Options Access Assignment
        self.stableStatesOnly = config.stableStatesOnly

        self.conservativeAccess = config.conservativeAccess
        self.ignoreDeferedStates = config.ignoreDeferedStates

        self.maxagressiveAccess = config.maxagressiveAccess

        # Options Merging
        self.enableStateMerging = config.enableStateMerging
        self.maxMergingIter = config.maxMergingIter
        self.MergeStates = MergeStates(self.maxMergingIter, self.access, self.evict)

        self._ProcessArch()


    def _ProcessArch(self):

        self.pheader("Caches")
        self.pdebug(str(self.level.cache))

        self.pheader("Directories")
        self.pdebug(str(self.level.directory))

        # Cache
        arch_name = str(self.level.cache)

        talgo = time.time()
        self.pheader("\nArchitecture: " + arch_name)

        stablestates = [str(state) for state in self.level.cache.stable_states]
        state_sets = self.level.cache.state_sets

        self._ProtoGenV2(self.level.cache, state_sets, self.maxNestingDepthCC)

        self._AssignAccess(state_sets, stablestates)

        if self.enableStateMerging:
            print("State reduction function enabled")
            self.MergeStates.merge_states(state_sets)
        else:
            print("State reduction function disabled")

        self.pdebug("Runtime: " + arch_name + " = " + str(time.time() - talgo))

        self.level.cache.update_transitions()
        statedict = extract_states_from_sets(state_sets)

        self._pTransitions(arch_name, statedict)
        # Run ProtoGen
        if self.dbg_graph:
            self._dArch(arch_name, statedict)

        self.cacheStateSets += list(state_sets.values())

        self.archProtoGen.update({arch_name: statedict})

        self.level.cache.update_transitions()

        # Directory
        arch_name = str(self.level.directory)
        talgo = time.time()
        self.pheader("\nArchitecture: " + arch_name)

        # General directory pre processing
        stablestates = [str(state) for state in self.level.directory.stable_states]
        state_sets = self.level.directory.state_sets

        # ProtoGen
        self._ProtoGenAlgorithm(self.level.directory, state_sets, stablestates, self.maxNestingDepthDC, self._DirectoryDefer)

        #self.merge_states(state_sets)

        self.pdebug("Runtime: " + arch_name + " = " + str(time.time() - talgo))

        self.level.directory.update_transitions()
        statedict = extract_states_from_sets(state_sets)

        self._pTransitions(arch_name, statedict)
        if self.dbg_graph:
            self._dArch(arch_name, statedict)

        self.archProtoGen.update({arch_name: statedict})
        self.pdebug("")

    def _ProtoGenAlgorithm(self, arch: Architecture, state_sets, stablestates, maxdepth, deferfunc):
        newstates = 1
        nestingdepth = 0
        while newstates and nestingdepth < maxdepth:
            newstates = self._GenerateTransientStates(arch, state_sets, stablestates, deferfunc)
            # Update the traces
            arch.update_traces()
            nestingdepth += 1

        #self._AppendDefferedMessages(state_sets, stablestates)

    ########################################################################################################################
    # PUBLIC FUNCTIONS
    ########################################################################################################################
    def getArchStates(self):
        return self.archProtoGen

    def getCacheStates(self):
        return self.level.getCacheStates()

    def getDirStates(self):
        return self.level.getDirStates()

    def getMaxNestingDepth(self):
        return 0

    def getDCconservativeInv(self):
        return self.DCconservativeInv

    ########################################################################################################################
    # DEBUG
    ########################################################################################################################

    def _dArch(self, arch, statedict):
        if self.dbg:
            ProtoCCGraph("Spec: " + arch, self._pGetTransitions(statedict))

    def _pTransitions(self, arch, statedict):
        if self.dbg:
            transitions = self._pGetTransitions(statedict)
            ProtoCCTablePrinter().ptransitiontable(transitions)

    def _pGetTransitions(self, statedict):
        transitions = []
        for state in statedict:
            transitions += statedict[state].gettransitions()

        transitions = sorted(transitions, key=lambda transition: (transition.getstartstate().getstatename(),
                                                                  transition.getfinalstate().getstatename(),
                                                                  transition.getguard(),
                                                                  transition.getcond()))
        return transitions

########################################################################################################################
#   ProtoGen V2
########################################################################################################################

    def stable_state_trace_map(self, arch: Architecture, state_sets: StateSets) -> \
            Tuple[Dict[StateSet, List[Trace]], Dict[StateSet, List[Trace]]]:
        start_state_set_to_access_trace_list_map: Dict[StateSet, List[Trace]] = {}
        start_state_set_to_remote_trace_list_map: Dict[StateSet, List[Trace]] = {}
        for state_set in state_sets:
            access_traces, remote_traces = self.classify_traces_start_state(arch, state_sets[state_set])
            start_state_set_to_access_trace_list_map[state_sets[state_set]] = access_traces
            start_state_set_to_remote_trace_list_map[state_sets[state_set]] = remote_traces

        return start_state_set_to_access_trace_list_map, start_state_set_to_remote_trace_list_map


    def _ProtoGenV2(self, arch: Architecture, state_sets: StateSets, maxdepth: int):

        # Make trace trees
        start_state_set_to_access_trace_list_map, start_state_set_to_remote_trace_list_map = \
            self.stable_state_trace_map(arch, state_sets)

        # Stalling
        newstates = True
        nestingdepth = 0
        while newstates and nestingdepth < 2:
            newstates = False

            for state_set in state_sets:
                ret_val = self.concurrent_start_state_set_states(arch,
                                                                 state_sets[state_set],
                                                                 start_state_set_to_remote_trace_list_map)
                newstates = newstates or ret_val

            nestingdepth += 1
            arch.update_traces()


        # Non-stalling
        enabled = False
        newstates = True
        nestingdepth = 0
        while newstates and nestingdepth < maxdepth and (self.nonstalling or enabled):
            newstates = False

            for state_set in state_sets:
                ret_val = self.concurrent_end_state_set_states(arch,
                                                                 state_sets[state_set],
                                                                 start_state_set_to_remote_trace_list_map)
                newstates = newstates or ret_val

            nestingdepth += 1
            arch.update_traces()


