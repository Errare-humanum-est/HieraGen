import time
import os

from time import sleep
sleep(0.05)

from Murphi.MurphiModular import MurphiModular
from Monitor.ClassDebug import Debug
from Monitor.MakeDir import MakeDir

from DataObjects.ClassLevel import Level
from DataObjects.ClassMachine import Machine
from DataObjects.ClassCluster import Cluster


def RunMurphi(level: Level, filename: str, dbg_enabled: bool = True):
    dbg = Debug(dbg_enabled)
    path = os.getcwd()

    MakeDir("Murphi")

    # Generate System Tuple level
    archs = [level.cache, level.directory]
    cache_machine = Machine(level.cache)
    directory_machine = Machine(level.directory)
    sys_description = Cluster((cache_machine, cache_machine, cache_machine, directory_machine), 'C1', [level])
    clusters = [sys_description]

    SSP_MurphiDesc = MurphiModular(clusters, True)
    MurphiDesc = MurphiModular(clusters, False)

    print("Murphi files were generated in: " + os.getcwd())

    dbg.pheader(dbg.spacer + "Murphi make and run")
    talgo = time.time()

    dbg.pheader(dbg.spacer + "Starting SSP verification" + '\n')
    time.sleep(0.005)   # The delay is only related to the output queues of the model checker and the python tool
    #SSP_MurphiDesc.runMurphi(True, filename)
    #ssp_success = False
    ssp_success = True

    try:
        resultsfile = open("SSP_" + filename.split(".")[0] + "_results.txt")
    except FileNotFoundError:
        dbg.pwarning("SSP results file does not exist - did it compile correctly?"
                     + "\nPlease check SSP_" + filename.split(".")[0] + "_compile.txt"
                     + " for details, and make sure your input is correctly specified.")
    else:
        if "No error found" in resultsfile.read():
            time.sleep(0.005)
            dbg.psuccess("SSP verified without error")
            ssp_success = True
        else:
            dbg.pwarning("SSP did not verify correctly; please see SSP_"
                     + filename.split(".")[0] + "_results.txt for the Murphi output.")
        resultsfile.close()
    if ssp_success:
        dbg.pheader(dbg.spacer + "Starting full protocol verification" + '\n')
        time.sleep(0.005)
        MurphiDesc.runMurphi(False, filename)
        try:
            resultsfile = open(filename.split(".")[0] + "_results.txt")
        except FileNotFoundError:
            dbg.pwarning("Results file does not exist - did it compile correctly?"
                         + "\nPlease check " + filename.split(".")[0] + "_compile.txt "
                         + "for details, and make sure your input is correctly specified.")
        else:
            if "No error found" in resultsfile.read():
                time.sleep(0.005)
                dbg.psuccess("Full protocol verified without error")
            else:
                dbg.pwarning("Full protocol did not verify correctly; please see "
                             + filename.split(".")[0] + "_results.txt for the Murphi output.")
            resultsfile.close()
    else:
        dbg.pwarning("Aborting full protocol verification as SSP deemed incorrect.")
    dbg.pdebug(dbg.spacer + "Murphi runtime: " + str(time.time() - talgo) + '\n')

    os.chdir(path)
