class ProtoConfig:

    def __init__(self):
        # Options State Generation

        self.nonstalling = 1
        self.maxNestingDepthCC = 1

        # Options Cache
        self.CCconservativeInv = 0


        # Options Directory
        self.DCconservativeInv = 0
        self.maxNestingDepthDC = 0              # Currently a higher nesting depth is not working yet. Murphi backend

        # Options Access Assignment
        self.stableStatesOnly = 0

        self.conservativeAccess = 1
        self.ignoreDeferedStates = 0

        self.maxagressiveAccess = 0

        # Options Merging
        self.enableStateMerging = False
        self.maxMergingIter = 10

        self.graphexport = False


