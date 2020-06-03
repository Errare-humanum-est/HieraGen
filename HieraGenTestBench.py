import sys
import os
import time

from Monitor.MakeDir import MakeDir

from Parser.ClassProtoParser import ProtoParser
from DataObjects.ClassLevel import Level
from DataObjects.ClassCluster import Cluster
from DataObjects.ClassMachine import Machine

from Algorithms.HieraAlgorithm.HieraAlgorithm import HieraGen

from Algorithms.ProtoAlgorithm.ProtoAlgorithm import ProtoAlgorithm
from Algorithms.ProtoAlgorithm.ProtoConfig import ProtoConfig

from Murphi.RunMurphiModular import RunMurphiModular

from Monitor.ClassDebug import Debug

test_cases = [
    ["MSI.pcc", "MI.pcc"],
    ["MI.pcc", "MSI.pcc"],
    ["MSI.pcc", "MSI.pcc"],
    ["MESI.pcc", "MSI.pcc"],
    ["MESI.pcc", "MESI.pcc"],
    ["MOSI.pcc", "MSI.pcc"],
    ["MOSI.pcc", "MOSI.pcc"],
    ["MOESI.pcc", "MOESI.pcc"],
]

# Configure the test run cache counts
L1_cache_count = 2
L2_cache_count = 2

start_time = time.time()

# Change path to the protocol directory path
os.chdir(os.getcwd() + "/Protocols/")
# Save default path
path = os.getcwd()

dbg = Debug(True)

for test_case in test_cases:
    dbg.psection("\n NEXT TEST CASE \n")

    file1 = open(test_case[0]).read()
    file2 = open(test_case[1]).read()

    print(test_case[0].split(".")[0] + "_&_" + test_case[1].split(".")[0])

    MakeDir("HIR_" + test_case[0].split(".")[0] + "_&_" + test_case[1].split(".")[0])

    # Parse the input files
    ParserLL = ProtoParser(file1, test_case[0])
    ParserHL = ProtoParser(file2, test_case[1])

    # Generate cache and directory controllers
    lvl1 = Level(ParserLL, "L1", test_case[0])
    lvl2 = Level(ParserHL, "L2", test_case[1])

    # Generate System Tuple level 1
    cache_machine_ll = Machine(lvl1.cache)
    cache_tuple_ll = tuple(cache_machine_ll for ind in range(0, L1_cache_count))
    L1_directory_machine = Machine(lvl1.directory)
    cluster_1 = Cluster(cache_tuple_ll + (L1_directory_machine, ), 'C1', [lvl1])

    # Generate Level 2
    cache_machine = Machine(lvl2.cache)             # This is the cache part of the cache/dir controller
    cache_machine_hl = Machine(lvl2.cache)
    cache_tuple_hl = tuple(cache_machine_hl for ind in range(0, L2_cache_count))
    directory_machine = Machine(lvl2.directory)
    # Single remote directory
    cluster_2 = Cluster(cache_tuple_hl + (cache_machine, directory_machine), 'C2', [lvl2])

    # Run HieraGen
    # First run HieraGen
    dbg.pheader("HIERAGEN OUTPUT:")
    h_gen = HieraGen(lvl1, lvl2, dbg.dbg)

    # Run ProtoGen for hierachical controller
    config = ProtoConfig()
    dbg.pheader("HIERAGEN CONCURRENT CONTROLLER OUTPUT:")
    ProtoAlgorithm(h_gen.high_level, config, dbg.dbg)
    high_level = h_gen.high_level

    # Then Run ProtoGen for the ll and hl cache and directory controllers
    dbg.pheader("LOWER LEVEL CACHE CONCURRENT CONTROLLER OUTPUT:")
    ProtoAlgorithm(lvl1, ProtoConfig(), dbg.dbg)
    dbg.pheader("HIGHER LEVEL CACHE & DIRECTORY CONCURRENT CONTROLLER OUTPUT:")
    ProtoAlgorithm(lvl2, ProtoConfig(), dbg.dbg)

    # Combine clusters
    # by replacing directory of lower level with dir/cache and the designated cache of the higher level
    cluster_1.replace_arch(lvl1.directory, high_level.cache)
    cluster_2.replace_arch(lvl2.cache, high_level.cache)

    # Run the Murphi model checker verification
    RunMurphiModular([cluster_1, cluster_2], test_case[0], False, 8000)

    dbg.pdebug("HIR_" + test_case[0].split(".")[0] + "_&_" + test_case[1].split(".")[0] +
           " Runtime: " + str(time.time() - start_time))

    # Reset the path
    os.chdir(path)
