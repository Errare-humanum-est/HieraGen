from typing import Tuple, List
from DataObjects.ClassMachine import Machine
from DataObjects.ClassLevel import Level
from DataObjects.ClassArchitecture import Architecture

from DataObjects.ClassSystemTuple import SystemTuple


class Cluster(SystemTuple):

    def __init__(self, machines: Tuple[Machine, ...], cluster_id: str, levels: List[Level]):
        SystemTuple.__init__(self, machines)
        self.levels: List[Level] = levels
        self.cluster_id = cluster_id

        # Mapping of machine_name to unique id
        self.name_space = {}

        # The arch_id of every machine in a cluster is extended by the cluster id label
        # Update the machine names in the cluster
        if cluster_id:
            for level in levels:
                level.update_mach_name_operation_append(cluster_id)

    def replace_arch(self, old_arch: Architecture, new_arch: Architecture):
        # Then replace the directory
        found_once = 0
        for machine in self.system_tuple:
            machine.arch.update_trans_operation(old_arch.get_unique_id_str(), new_arch.get_unique_id_str())
            if machine.arch == old_arch and not found_once:
                machine.update_mach_arch(new_arch)
                found_once = 1
        assert found_once, "Could not find architecture to replace in cluster"




