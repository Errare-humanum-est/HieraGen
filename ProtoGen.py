import sys

from Murphi.RunMurphiSingle import *
from Murphi.RunMurphiModular import RunMurphiModular
from Algorithms.ProtoAlgorithm.RunProtoGen import RunProtoGen

spacer = "\n\n\n"
graphdbgParser = 0
graphdbgAlgorithm = 0


def run_next(filename, path):
    os.chdir(path)
    file = open(filename).read()
    MakeDir(filename.split(".")[0])

    level, Algorithm = RunProtoGen(file, filename)

    # Generate System Tuple level 1
    cache_machine = Machine(level.cache)
    L1_directory_machine = Machine(level.directory)
    cluster_1 = Cluster((cache_machine, cache_machine, cache_machine, L1_directory_machine), 'C1', [level])
    RunMurphiModular([cluster_1], filename, False, 4000)


path = os.getcwd()+"/Protocols/"

# Reply forwarding protocols
run_next("MI.pcc", path)
run_next("MSI.pcc", path)
run_next("MESI.pcc", path)
run_next("MOSI.pcc", path)
run_next("MOESI.pcc", path)


print("ProtoGen complete")


