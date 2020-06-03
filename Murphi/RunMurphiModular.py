import time
import os
from psutil import virtual_memory

from typing import List

from time import sleep
sleep(0.05)

from Murphi.MurphiModular import MurphiModular
from Monitor.ClassDebug import Debug
from Monitor.MakeDir import MakeDir

from DataObjects.ClassCluster import Cluster


def RunMurphiModular(clusters: List[Cluster],
                     filename: str,
                     run_SSP: bool = True,
                     memory: int = 0,
                     dbg_enabled: bool = True):

    dbg = Debug(dbg_enabled)
    path = os.getcwd()

    if not memory:
        # Calculate the free memory in Megabyte
        memory = int(virtual_memory().free/2**20) - 8000      # Leave about 1GB of additional free memory

    MakeDir("Murphi")

    SSP_MurphiDesc = MurphiModular(clusters, True)
    MurphiDesc = MurphiModular(clusters, False)

    print("Murphi files were generated in: " + os.getcwd())

    dbg.pheader(dbg.spacer + "Murphi make and run")
    talgo = time.time()

    dbg.pheader(dbg.spacer + "Starting SSP verification" + '\n')
    time.sleep(0.005)   # The delay is only related to the output queues of the model checker and the python tool
    ssp_success = False

    if run_SSP:
        SSP_MurphiDesc.runMurphi(True, filename)

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

    if ssp_success or not run_SSP:
        dbg.pheader(dbg.spacer + "Starting full protocol verification" + '\n')
        time.sleep(0.005)
        MurphiDesc.runMurphi(False, filename, memory)
        try:
            resultsfile = open(filename.split(".")[0] + "_results.txt")
        except FileNotFoundError:
            dbg.pwarning("Results file does not exist - did it compile correctly?"
                         + "\nPlease check " + filename.split(".")[0] + "_compile.txt "
                         + "for details, and make sure your input is correctly specified.")
        else:
            result_str = resultsfile.read()
            if result_str.rfind("No error found") != -1:
                time.sleep(0.005)
                dbg.psuccess("Full protocol verified without error")
            else:
                if result_str.rfind("Closed hash table full.") != -1 or \
                        result_str.rfind("Internal Error: Too many active states.") != -1:
                    dbg.pwarning("Murphi memory full, please allocate more memory for the verification thread: \n See"
                                 + filename.split(".")[0] + "_results.txt for the Murphi output. \n")
                else:
                    dbg.pwarning("Full protocol did not verify correctly; please see "
                                 + filename.split(".")[0] + "_results.txt for the Murphi output.")
            resultsfile.close()
    else:
        dbg.pwarning("Aborting full protocol verification as SSP deemed incorrect.")
    dbg.pdebug(dbg.spacer + "Murphi runtime: " + str(time.time() - talgo) + '\n')

    # Reset the path
    os.chdir(path)
