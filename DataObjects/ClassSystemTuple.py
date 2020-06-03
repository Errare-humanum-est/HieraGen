from typing import Tuple
from DataObjects.ClassMachine import Machine
from DataObjects.ClassArchitecture import Architecture
from Algorithms.General.Tracing.TraceTree import *

from itertools import product, permutations


class SystemTuple:
    def __init__(self, machines: Tuple[Machine, ...]):
        self.system_tuple: Tuple[Machine] = machines

    def make_set(self):
        return tuple(sorted([mach.get_mach_state_trace_id() for mach in self.system_tuple])).__hash__()

    def __str__(self):
        sort_mach = self.sort_machines_id()
        ret_str = ""
        for machine in sort_mach:
            ret_str += str(machine.get_mach_state_trace_str()) + "; "
        ret_str = ret_str[:-2]
        return ret_str

    def __hash__(self):
        return hash(self.make_set())

    def __eq__(self, other):
        if isinstance(other, SystemTuple):
            return self.make_set() == other.make_set()
        return False

    def __len__(self):
        return len(self.system_tuple)

    def get_start_state_set(self):
        return set([mach.start_state for mach in self.sort_machines_id()])

    def get_final_state_set(self):
        return set([mach.final_state for mach in self.sort_machines_id()])

    def get_reduced_set(self):
        unique_state_dict = {id(mach.cur_trace): mach for mach in self.system_tuple if mach.cur_trace}
        sorted_tuple = sorted(list(unique_state_dict.values()), key=lambda mach: mach.get_mach_state_trace_id())
        return hash(tuple(sorted(unique_state_dict.keys()))), sorted_tuple

    def get_permutation_list(self):
        pass

    def get_permutation_machines(self) -> List[Tuple[Machine]]:
        # Only identical blocks may be permutated
        arch_list = self.get_machine_architectures()
        mach_list = {arch: [] for arch in arch_list}
        for mach in self.system_tuple:
            (mach_list[mach.arch]).append(mach)

        for entry in mach_list:
            perm = list(permutations(mach_list[entry], len(mach_list[entry])))
            mach_list[entry] = perm

        new_system_tuples = []
        for raw_system_tuple in list(product(*mach_list.values())):
            new_sys_tuple = ()
            for arch_tuple in raw_system_tuple:
                new_sys_tuple += arch_tuple

            new_system_tuples.append(new_sys_tuple)

        return new_system_tuples

    def get_machine_architectures(self) -> List[Architecture]:
        arch_list = []
        for mach in self.system_tuple:
            if mach.arch not in arch_list:
                arch_list.append(mach.arch)
        return arch_list

    def get_arch_machines(self, arch) -> List[Machine]:
        arch_machines = []
        for mach in self.system_tuple:
            if mach.arch == arch:
                arch_machines.append(mach)
        return arch_machines

    def get_arch_traces(self, arch) -> List[Trace]:
        return [mach.cur_trace for mach in self.get_arch_machines(arch) if mach.cur_trace]

    def get_arch_access_trace(self, arch: Architecture = None) -> List[Trace]:
        if arch:
            mach_traces = [mach.cur_trace for mach in self.get_arch_machines(arch)]
        else:
            mach_traces = [mach.cur_trace for mach in self.system_tuple]
        return [mach_trace for mach_trace in mach_traces if mach_trace and mach_trace.access]

    def get_arch_remote_trace(self, arch: Architecture = None) -> List[Trace]:
        if arch:
            mach_traces = [mach.cur_trace for mach in self.get_arch_machines(arch)]
        else:
            mach_traces = [mach.cur_trace for mach in self.system_tuple]
        return [mach_trace for mach_trace in mach_traces if mach_trace and not mach_trace.access]

    def sort_machines_id(self) -> Tuple[Machine]:
        # Get list of architectures first:
        mach_list = list(self.system_tuple)
        mach_arch_sort = tuple(sorted(mach_list, key=lambda machine: (machine.arch.get_unique_id_str(),
                                                                id(machine.covered_traces))))
        return mach_arch_sort

    def find_traces(self, trace: Trace) -> bool:
        for mach in self.system_tuple:
            if trace == mach.cur_trace:
                return True
        return False

    def sort_and_update_system_tuple(self) -> 'SystemTuple':
        self.system_tuple = self.sort_machines_id()
        return self

    def sort_machines_state(self, state_type: str = "start_state") -> Tuple[Machine]:
        # Get list of architectures first:
        mach_list = list(self.system_tuple)
        mach_arch_sort = tuple(sorted(mach_list, key=lambda machine: (machine.arch.arch_type,
                                                                      str(getattr(machine, state_type)))))
        return mach_arch_sort

    def start_state_tuple_str(self):
        sorted_tuple = self.sort_machines_state("start_state")
        start_state_str = ""
        for mach in sorted_tuple:
            start_state_str += str(mach.start_state) + "; "

        return start_state_str[:-2]

    def final_state_tuple_str(self):
        sorted_tuple = self.sort_machines_state("final_state")
        final_state_str = ""
        for mach in sorted_tuple:
            final_state_str += str(mach.final_state) + "; "

        return final_state_str[:-2]

    def access_state_tuple_str(self):
        sorted_tuple = self.sort_machines_state("start_state")
        access_list = ""
        for mach in sorted_tuple:
            if not mach.cur_trace:
                continue
            new_access_str = '; '.join(mach.cur_trace.access)
            if new_access_str:
                access_list += new_access_str + "; "
        return access_list[:-2]

    def system_tuple_id_str(self):
        sorted_tuple = self.sort_machines_id()
        sys_id = ""
        for mach in sorted_tuple:
            sys_id += mach.arch.arch_name + "_" + mach.arch.arch_name + "; "

        return sys_id[:-2]
