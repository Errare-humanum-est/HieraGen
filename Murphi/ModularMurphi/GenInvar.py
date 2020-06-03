from typing import List

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler

from DataObjects.ClassCluster import Cluster


class GenInvar(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)

    def _generateInvariants(self, clusters: List[Cluster], enabled: bool = True):
        invstr = "--" + __name__ + self.nl
        if enabled:
            invstr += self._genInvariantSW()
            invstr += self._genInvariantEW()

        return invstr

    def _genInvariantSW(self):
        return self._stringReplKeys(self._openTemplate(self.faccesscheckinvSW), [self.kaddress]) + self.nl

    def _genInvariantEW(self):
        return self._stringReplKeys(self._openTemplate(self.faccesscheckinvEW), [self.kaddress]) + self.nl

