import os
import re
import subprocess
from typing import List

from Parser.ProtoCCcomTreeFct import *
from Monitor.ClassDebug import *

from DataObjects.ClassLevel import Level
from Murphi.ModularMurphi.MurphiModularBase import MurphiModularBase

from DataObjects.ClassMachine import Machine
from DataObjects.ClassCluster import Cluster

class Murphi(MurphiModularBase):
    TemplateDir = "MurphiTemp"

    cadrcnt = 1
    cvalmax = 1

    # Config Parameters
    cfifomax = 1
    enableFifo = 0
    corderedsz = cadrcnt * 3 * 2 * 2
    cunorderedsz = cadrcnt * 3 * 2 * 2

    def __init__(self, level, algorithm, verify_ssp):
        MurphiModularBase.__init__(self, self.TemplateDir)
        """ The following keywords need to be instance-specific. If they
            are not then verifying multiple protocols within one process
            (for example SSP + ProtoGen output) will lead to syntax errors
            in all but the very first of the generated Murphi files."""

        self.level = level
        self.parser = level.parser

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

        file_name = self.parser.getFilename().split(".")[0] + ".m"
        if verify_ssp:
            file_name = self.ssp_prefix + file_name

        murphifile = open(file_name, "w")
        self.parser = level.cache.parser

        self.memaccessdef = self.parser.getAccess()
        self.maxdeferdepth = str(2)                 # Maximum Defer Depth
        self.messageslist = level.getMsgStrings()

        #self.DCconservativeInv = algorithm.getDCconservativeInv()

        #self.defer = algorithm.testNonStalling()
        self.defer = True

        # Generate System Tuple level
        archs = [self.level.cache, self.level.directory]
        cache_machine = Machine(self.level.cache)
        directory_machine = Machine(self.level.directory)
        sys_description = Cluster((cache_machine, cache_machine, cache_machine, directory_machine), 'C1', [level])
        clusters = [sys_description]

        murphiout = ""
        self.murphi_const = self.generateConst(clusters) + self.nl
        self.murphi_types = self.gen_enum_str(clusters)
        self.murphi_objsets = self.gen_object_set_str_scalar_set(clusters)

        # TODO: BUILD A NICE NETWORK AGGREGATION
        self.muphi_networkobj = self.gen_network_str(clusters, self.cfifomax)

        self.murphi_access_type = self.gen_access_type(clusters)

        self.murphi_decl = self.gen_mach_obj_str(clusters, self.defer)
        self.murphi_lock_type = self.gen_lock_type(verify_ssp)
        self.murphi_vars = self.generate_vars(clusters, verify_ssp) + self.nl

        self.murphi_lock_func = self.gen_lock_func(verify_ssp)
        self.murphi_access_check_func = self.gen_access_func(clusters)

        self.murphi_misc_func = self.gen_network_func(clusters, self.cfifomax) + self.nl
        self.murphi_arch_func = self._generateObjFunc(clusters) + self.nl

        self.murphi_access_func = self._gen_arch_access_send_func(clusters)
        self.murphi_access_rules = self.gen_access_rules(clusters, verify_ssp)

        # NETWORK RULES
        self.murphi_fifo_rule = self.gen_fifo_rule(clusters) + self.nl
        self.murphi_netw_rule = self.gen_network_rules(clusters) + self.nl

        self.murphi_start_state = self.generate_start_state(clusters, verify_ssp) + self.nl

        self.murphi_inv = self._generateInvariants(clusters) + self.nl

        murphiout += self.murphi_const + self.murphi_types + self.murphi_objsets + self.muphi_networkobj + \
                     self.murphi_access_type + \
                     self.murphi_decl + self.murphi_lock_type + self.murphi_vars + self.murphi_lock_func + \
                     self.murphi_access_check_func + self.murphi_misc_func + \
                     self.murphi_arch_func + self.murphi_access_func + self.murphi_access_rules +\
                     self.murphi_fifo_rule + self.murphi_netw_rule + \
                     self.murphi_start_state + self.murphi_inv

        murphifile.write(murphiout)


########################################################################################################################
# RUN MURPHI
########################################################################################################################

    def runMurphi(self, verify_ssp):
        makefile = open("Makefile", "w")
        murphiname = self.parser.getFilename().split(".")[0]
        mem = 2000

        if verify_ssp:
            murphiname = self.ssp_prefix + murphiname

        template = self._openTemplate(self.ftmpmake)
        replacekeys = [murphiname]

        for ind in range(0, len(replacekeys)):
            template = self._stringRepl(template, ind, replacekeys[ind])

        makefile.write(template)
        makefile.flush()

        self._runCompilation(murphiname)

        if os.path.isfile("./" + murphiname):
            cmd = ["./" + murphiname, "-tv", "-pr", "-m", str(mem)]
            report = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
            reportfile = open(murphiname + "_results" + ".txt", "w")
            reportfile.write(report)
            reportfile.close()

            if "No error found" not in report:
                pdebug(report)

    def _runCompilation(self, murphiname):
        compile = subprocess.run(["make"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        compilefile = open(murphiname + "_compile" + ".txt", "w")
        compilefile.write(compile)
        compilefile.close()

        res = re.search(r'Makefile:[\w\s:]*\'[\w\s.]*\'\s*failed', compile)
        if res:
            pdebug(compile)
            perror("ProtoGen terminated due to Murphi compilation error")


########################################################################################################################
# CONST
########################################################################################################################

    def generateConst(self, clusters: List[Cluster]):
        return self.gen_const_str(clusters, self.enableFifo,
                                              self.cvalmax,
                                              self.cadrcnt,
                                              self.corderedsz,
                                              self.cunorderedsz)
