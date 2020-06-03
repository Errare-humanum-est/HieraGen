from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenLockType(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)

    def gen_lock_type(self, verify_ssp):
        lock_str = "--" + __name__ + self.nl
        if verify_ssp:
            lock_str += self._openTemplate(self.flockdef) + self.nl
        return lock_str
