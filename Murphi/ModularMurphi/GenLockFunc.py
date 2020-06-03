from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenLockFunc(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)

    def gen_lock_func(self, verify_ssp):
        lock_str = "--" + __name__ + self.nl
        if verify_ssp:
            lock_str += self._stringReplKeys(self._openTemplate(self.flockfunc), [self.kmachines]) + self.nl
        return lock_str
