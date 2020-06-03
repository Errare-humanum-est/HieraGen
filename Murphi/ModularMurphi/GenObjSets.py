from typing import List

from DataObjects.ClassCluster import Cluster

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenObjectSets(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.kmachnames = []

    def gen_object_set_str_scalar_set(self, clusters: List[Cluster]):
        obj_str = "--" + __name__ + self.nl
        obj_str += self.gen_address_scalarset()
        obj_str += self.gen_static_obj() + self.nl
        obj_str += self.gen_mach_objset(clusters)
        return obj_str + self.nl

    def gen_object_set_str_val_range(self, clusters: List[Cluster]):
        obj_str = "--" + __name__ + self.nl
        obj_str += self.gen_address_val_range()
        obj_str += self.gen_static_obj() + self.nl
        obj_str += self.gen_mach_objset(clusters)
        return obj_str + self.nl

    def gen_static_obj(self):
        typestr = ""
        typestr += self.kcacheval + ": " + "0.." + self.cvalcntid + self.end
        return typestr

    def gen_address_scalarset(self):
        return self._makescalarset(self.kaddress, self.cadrcntid)

    def gen_address_val_range(self):
        return self.kaddress + ": " + "0.." + self.cadrcntid + self.end

    def gen_mach_objset(self, clusters: List[Cluster]):
        machinetypes = []

        typestr = ""
        for cluster in clusters:
            machines = set(cluster.system_tuple)

            level_mach_types = []
            for machine in machines:
                mach_cnt = cluster.system_tuple.count(machine)
                mach_obj_set = self.SetKey + machine.arch.get_unique_id_str()
                if mach_obj_set not in machinetypes:
                    if mach_cnt > 1:
                        typestr += self._makescalarset(mach_obj_set, str(mach_cnt))
                    elif mach_cnt == 1:
                        typestr += self._makeenum(mach_obj_set, machine.arch.get_unique_id_str())
                    else:
                        assert "Error"

                level_mach_types.append(mach_obj_set)

            typestr += self.typeMachineUnion(level_mach_types, cluster.cluster_id)
            machinetypes += level_mach_types

        # Check for duplicated names
        #assert not [x for n, x in enumerate(machinetypes) if x in machinetypes[:n]], "Error, Duplicated namespace"

        typestr += self.typeMachineUnion(list(set(machinetypes)))

        # Creates the global machine type variable
        self.kmachnames = sorted(machinetypes)
        return typestr

    def typeMachineUnion(self, machinetypes: List[str], cluster: str = ""):
        return cluster + self._makeunion(self.kmachines, machinetypes)

    ####################################################################################################################
    # SET TYPES
    ####################################################################################################################
    def _makeunion(self, typename, elements):
        elmstr = ""
        for ind in range(0, len(elements)-1):
            elmstr += elements[ind] + ", "

        elmstr += elements[-1]

        return typename + ": " + "union{" + elmstr + "};" + self.nl

    def _makeenum(self, typename, machineid):
        return typename + ": " + "enum{" + machineid + "};" + self.nl

    def _makescalarset(self, typename, setsize):
        return typename + ": " + "scalarset(" + setsize + ");" + self.nl

    def _makerange(self, typename, maxval):
        return typename + ": " + "0.." + maxval + ";" + self.nl
