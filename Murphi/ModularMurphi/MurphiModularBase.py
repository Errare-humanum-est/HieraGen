from Murphi.ModularMurphi.MurphiGlobalVariables import GlobalVariables
from Murphi.ModularMurphi.GenConst import GenConst
from Murphi.ModularMurphi.GenEnums import GenEnums
from Murphi.ModularMurphi.GenObjSets import GenObjectSets
from Murphi.ModularMurphi.GenNetworkObj import GenNetworkObj
from Murphi.ModularMurphi.GenAccessType import GenAccessType
from Murphi.ModularMurphi.GenMachObj import GenMachObj
from Murphi.ModularMurphi.GenLockType import GenLockType
from Murphi.ModularMurphi.GenVars import GenVars
from Murphi.ModularMurphi.GenLockFunc import GenLockFunc
from Murphi.ModularMurphi.GenNetworkFunc import GenNetworkFunc
from Murphi.ModularMurphi.GenAccessFunc import GenAccessFunc
from Murphi.ModularMurphi.GenFSMFuncObj import GenFSMFuncObj
from Murphi.ModularMurphi.GenAccessRuleset import GenAccessRuleset
from Murphi.ModularMurphi.GenAccessSendFunc import GenAccessSendFunc
from Murphi.ModularMurphi.GenModStateFunc import GenModStateFunc

from Murphi.ModularMurphi.GenNetworkRules import GenNetworkRules
from Murphi.ModularMurphi.GenStartStates import GenStartStates
from Murphi.ModularMurphi.GenInvar import GenInvar

from Monitor.ClassDebug import Debug

class MurphiModularBase(GlobalVariables,
                        GenConst,
                        GenEnums,
                        GenObjectSets,
                        GenNetworkObj,
                        GenAccessType,
                        GenMachObj,
                        GenLockType,
                        GenVars,
                        GenLockFunc,
                        GenNetworkFunc,
                        GenAccessFunc,
                        GenFSMFuncObj,

                        GenAccessRuleset,
                        GenAccessSendFunc,
                        GenModStateFunc,

                        GenNetworkRules,
                        GenStartStates,
                        GenInvar,

                        Debug
                        ):

    def __init__(self, template_dir, debug_enable: bool = False):
        GlobalVariables.__init__(self)
        Debug.__init__(self, debug_enable)

        GenConst.__init__(self, template_dir)
        GenEnums.__init__(self, template_dir)
        GenObjectSets.__init__(self, template_dir)
        GenNetworkObj.__init__(self, template_dir)
        GenAccessType.__init__(self, template_dir)
        GenMachObj.__init__(self, template_dir)
        GenLockType.__init__(self, template_dir)
        GenVars.__init__(self, template_dir)
        GenLockFunc.__init__(self, template_dir)
        GenNetworkFunc.__init__(self, template_dir)
        GenAccessFunc.__init__(self, template_dir)
        GenFSMFuncObj.__init__(self, template_dir)

        GenAccessRuleset.__init__(self, template_dir)
        GenAccessSendFunc.__init__(self, template_dir)

        GenModStateFunc.__init__(self, template_dir)

        GenNetworkRules.__init__(self, template_dir)
        GenStartStates.__init__(self, template_dir)
        GenInvar.__init__(self, template_dir)
