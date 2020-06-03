import sys
import time
import os
import pickle

from Algorithms.General.GenStateSets import *

from Algorithms.HieraAlgorithm.HieraAlgorithm import HieraGen

from Algorithms.ProtoAlgorithm.ProtoAlgorithm import ProtoAlgorithm
from Algorithms.ProtoAlgorithm.ProtoConfig import ProtoConfig

from DataObjects.ClassLevel import Level
from DataObjects.ClassCluster import Cluster

from DataObjects.ClassMachine import Machine

from Monitor.MakeDir import MakeDir
from Monitor.ClassDebug import Debug

from Murphi.RunMurphiModular import RunMurphiModular

start_time = time.time()

spacer = "\n\n\n"
graphdbgParser = False
graphdbgAlgorithm = True

graphdbgparser = False

dev_parser = 1
dev_make_clusters = 1
dev_hgen = 1
dev_pgen = 1
dev_override_backend = 1

dbg = Debug(True)

if len(sys.argv[1:]) == 0:
    os.chdir('../..')
    os.chdir(os.getcwd() + "/Protocols/")
else:
    assert len(sys.argv[1:]) == 1, "Too many arguments"
    filename = sys.argv[1]

filename1 = "MOESI.pcc"
filename2 = "MOESI.pcc"

# Save default path
path = os.getcwd()

if dev_parser:

    # TEST MSI AND MESI
    file1 = open(filename1).read()
    file2 = open(filename2).read()
    MakeDir("HIR_" + filename1.split(".")[0] + "_&_" + filename2.split(".")[0])

    # Frontend
    Parser1 = ProtoParser(file1, filename1, graphdbgparser)
    if not Parser1.checkAccessBehaviourDefined():
        print("Exiting.")
        sys.exit(1)
    if not Parser1.checkAllStatesReachable():
        print("Exiting.")
        sys.exit(1)

    Parser2 = ProtoParser(file2, filename2, graphdbgparser)
    if not Parser2.checkAccessBehaviourDefined():
        print("Exiting.")
        sys.exit(1)
    if not Parser2.checkAllStatesReachable():
        print("Exiting.")
        sys.exit(1)

    dbg.pheader("Parsing Complete")

    # Generate cache and directory controllers
    lvl1 = Level(Parser1, "L1", filename1)
    lvl2 = Level(Parser2, "L2", filename2)

    dbg.pheader("Parsing Complete")
    dbg.pdebug("Runtime: " + str(time.time() - start_time))
    start_time = time.time()

    # Saving the objects:
    with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([lvl1, lvl2], f)

else:
    MakeDir("HIR_" + filename1.split(".")[0] + "_&_" + filename2.split(".")[0])

    if dev_hgen or dev_pgen:
        # Getting back the objects:
        with open('objs.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
            lvl1, lvl2 = pickle.load(f)

dbg.pheader("Level Generation Complete")
dbg.pdebug("Runtime: " + str(time.time() - start_time))
start_time = time.time()

dbg.pheader("Flat Protocol ProtoGen Concurrency Generation Complete")
dbg.pdebug("Runtime: " + str(time.time() - start_time))
start_time = time.time()

dbg.pheader("Hierachical Controller SSP Generation Complete")
dbg.pdebug("Runtime: " + str(time.time() - start_time))

start_time = time.time()

graphdbgalgorithm = 0

if dev_make_clusters:
    # Generate System Tuple level 1
    cache_machine = Machine(lvl1.cache)
    L1_directory_machine = Machine(lvl1.directory)
    cluster_1 = Cluster((cache_machine, cache_machine, L1_directory_machine), 'C1', [lvl1])

    # Generate Level 2
    cache_machine = Machine(lvl2.cache)
    cache_machine2 = Machine(lvl2.cache)
    directory_machine = Machine(lvl2.directory)
    # Single remote directory
    cluster_2 = Cluster((cache_machine, cache_machine2, directory_machine), 'C2', [lvl2])
else:
    cluster_1 = None
    cluster_2 = None

if dev_hgen:
    # First run HieraGen
    h_gen = HieraGen(lvl1, lvl2, True)

    with open('h_gen.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(h_gen, f)
else:
    if dev_pgen:
        with open('h_gen.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
            h_gen = pickle.load(f)

if dev_pgen:
    config = ProtoConfig()

    ProtoAlgorithm(h_gen.high_level, config, True)
    high_level = h_gen.high_level

    # Then run ProtoGen
    ProtoAlgorithm(lvl1, ProtoConfig())
    ProtoAlgorithm(lvl2, ProtoConfig())
    with open('p_gen.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([high_level, lvl1, lvl2], f)
else:
    if dev_make_clusters:
        with open('p_gen.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
            high_level, lvl1, lvl2 = pickle.load(f)

if dev_make_clusters:
    cluster_1.replace_arch(lvl1.directory, high_level.cache)
    cluster_2.replace_arch(lvl2.cache, high_level.cache)
    with open('cluster.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([cluster_1, cluster_2], f)
else:
    with open('cluster.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
        cluster_1, cluster_2 = pickle.load(f)

    dbg.pheader("Cluster Generation Complete")
    dbg.pdebug("Runtime: " + str(time.time() - start_time))
    start_time = time.time()


if dev_make_clusters or dev_override_backend:
    RunMurphiModular([cluster_1, cluster_2], filename1, False, 8000)



