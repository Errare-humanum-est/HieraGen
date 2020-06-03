import time
import os
import sys

import pickle

from Parser.ClassProtoParser import ProtoParser
from DataObjects.ClassLevel import Level
from Algorithms.ProtoAlgorithm.ProtoAlgorithm import ProtoAlgorithm
from Algorithms.ProtoAlgorithm.ProtoConfig import ProtoConfig

from Monitor.MakeDir import MakeDir
from Monitor.ClassDebug import Debug


def RunProtoGen(file, filename):
    graphdbgparser = True
    graphdbgalgorithm = True

    path = os.getcwd()
    MakeDir("ProtoGen_Output")

    dbg = Debug(True)

    develop = 0
    if not develop:
        # Frontend
        dbg.pheader("PROTOGEN PARSER")
        Parser = ProtoParser(file, filename, graphdbgparser)
        if not Parser.checkAccessBehaviourDefined():
            print("Exiting.")
            sys.exit(1)
        if not Parser.checkAllStatesReachable():
            print("Exiting.")
            sys.exit(1)

        level = Level(Parser, "L1")

        dbg.pheader(dbg.spacer + "PROTOGEN ALGORITHM")

        # Saving the objects:
        with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
            pickle.dump(level, f)
    else:
        # Getting back the objects:
        with open('objs.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
            level = pickle.load(f)

    talgo = time.time()

    Algorithm = ProtoAlgorithm(level, ProtoConfig(), graphdbgalgorithm)
    dbg.pdebug("ProtoGen runtime: " + str(time.time() - talgo) + '\n')
    dbg.pheader(dbg.spacer + "PROTOGEN BACKEND")

    os.chdir(path)

    return level, Algorithm
