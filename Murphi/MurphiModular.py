import os
import re
import subprocess
from typing import List

from DataObjects.ClassCluster import Cluster
from Murphi.ModularMurphi.MurphiModularBase import MurphiModularBase


class MurphiModular(MurphiModularBase):
    TemplateDir = "MurphiTemp"

    cadrcnt = 1
    cvalmax = 1

    # Config Parameters
    cfifomax = 1
    enableFifo = 0
    corderedsz = cadrcnt * 3 * 2
    cunorderedsz = cadrcnt * 3 * 2

    def __init__(self, clusters: List[Cluster], verify_ssp):
        MurphiModularBase.__init__(self, self.TemplateDir)
        """ The following keywords need to be instance-specific. If they
            are not then verifying multiple protocols within one process
            (for example SSP + ProtoGen output) will lead to syntax errors
            in all but the very first of the generated Murphi files."""

        self.name = "HIR_TEST"

        self.kmachnames = []

        self.BaseMsg = [self.madr, self.mtype, self.msrc, self.mdst]
        self.SuperMsg = []

        self.Vectordef = []
        self.Vectormap = {}
        self.Vectorassign = {}
        self.GlobalInit = {}
        self.Messageassignmap = {}

        self.ONetworks = []
        self.UNetworks = []

        parser = clusters[0].system_tuple[0].arch.parser

        file_name = parser.getFilename().split(".")[0] + ".m"
        if verify_ssp:
            file_name = self.ssp_prefix + file_name

        murphifile = open(file_name, "w")

        self.memaccessdef = parser.getAccess()
        self.maxdeferdepth = str(0)

        # Maximum Defer Depth
        self.messageslist = []
        for cluster in clusters:
            for level in cluster.levels:
                self.messageslist += level.getMsgStrings()

        self.messageslist= list(set(self.messageslist))

        murphiout = ""

        # TODO: BUILD A NICE NETWORK AGGREGATION
        self.muphi_networkobj = self.gen_network_str(clusters, self.cfifomax)

        self.CPUs = 2
        self.INSTR = 2

        murphiout += (self.generateConst(clusters) +
                     self.gen_enum_str(clusters) +
                     self.gen_object_set_str_scalar_set(clusters) +
                     self.muphi_networkobj +
                     self.gen_access_type(clusters) +
                     self.gen_mach_obj_str(clusters) +
                     self.gen_lock_type(verify_ssp) +
                     self.generate_vars(clusters, verify_ssp) +
                     self.gen_lock_func(verify_ssp) +
                     self.gen_access_func(clusters) +
                     self.gen_network_func(clusters, self.cfifomax) +
                     self.gen_mod_state_func(clusters) +
                     self._generateObjFunc(clusters) +
                     self._gen_arch_access_send_func(clusters) +
                     self.gen_access_rules(clusters, verify_ssp) +
                     self.gen_fifo_rule(clusters) +
                     self.gen_network_rules(clusters) +
                     self.generate_start_state(clusters, verify_ssp) +
                     self._generateInvariants(clusters, True))

        murphifile.write(murphiout)


########################################################################################################################
# RUN MURPHI
########################################################################################################################

    def runMurphi(self, verify_ssp, filename, memory: int = 4000):
        makefile = open("Makefile", "w")
        murphiname = filename.split(".")[0]
        compaction = "-b"

        if verify_ssp:
            murphiname = self.ssp_prefix + murphiname

        replacekeys = [murphiname, compaction]
        template = self._stringReplKeys(self._openTemplate(self.ftmpmake), replacekeys)

        makefile.write(template)
        makefile.flush()

        self._runCompilation(murphiname)

        if os.path.isfile("./" + murphiname):
            cmd = ["./" + murphiname, "-tv", "-pr", "-m", str(memory)]
            report = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
            reportfile = open(murphiname + "_results" + ".txt", "w")
            reportfile.write(report)
            reportfile.close()

            if "No error found" not in report:
                self.pdebug(report)


    def run_default_murhpi(self):
        pass

    def run_hash_murphi(self):
        pass

        '''        
        # Continous Murphi Run output stream
        if os.path.isfile("./" + murphiname):
            cmd = ["./" + murphiname, "-tv", "-pr", "-m", str(mem)]
            reportfile = open(murphiname + "_results" + ".txt", "w")
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # Poll process for new output until finished
            while True:
                nextline = process.stdout.readline().decode("utf-8")
                reportfile.write(nextline)
                if nextline == '' and process.poll() is not None:
                    break
                print(nextline)

            output = process.communicate()[0]

            #report = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
            reportfile.close()
            reportfile = open(murphiname + "_results" + ".txt", "r")
            report = reportfile.read()

            if "No error found" not in report:
                pdebug(report)
        '''

    def _runCompilation(self, murphiname):
        compile = subprocess.run(["make"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        compilefile = open(murphiname + "_compile" + ".txt", "w")
        compilefile.write(compile)
        compilefile.close()

        res = re.search(r'Makefile:[\w\s:]*\'[\w\s.]*\'\s*failed', compile)
        if res:
            self.pdebug(compile)
            self.perror("ProtoGen terminated due to Murphi compilation error")


########################################################################################################################
# CONST
########################################################################################################################

    def generateConst(self, clusters: List[Cluster]):
        return self.gen_const_str(clusters, self.enableFifo,
                                              self.cvalmax,
                                              self.cadrcnt,
                                              self.corderedsz,
                                              self.cunorderedsz)
