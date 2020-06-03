from typing import Union, List

from Algorithms.General.Tracing.TraceTree import Trace
from DataObjects.ClassLevel import Level

from DataObjects.ClassSystemTuple import SystemTuple

"""
####################################################################################################################
##### Trace extraction functions from SystemTuple
####################################################################################################################
"""


class StateTupleBaseFunc:

    def __init__(self):
        pass

    @staticmethod
    def get_dir_trace(state_tuple: SystemTuple, level: Level) -> Union[None, Trace]:
        ll_dir_trace = state_tuple.get_arch_traces(level.directory)
        if not ll_dir_trace:
            return None
        assert len(ll_dir_trace) == 1, "Multiple directory traces not supported"
        return ll_dir_trace[0]

    @staticmethod
    def get_cache_access_trace(state_tuple: SystemTuple, level: Level) -> Union[None, Trace]:
        ll_cc_trace = state_tuple.get_arch_access_trace(level.cache)
        if not ll_cc_trace:
            return None
        assert len(ll_cc_trace) == 1, "Multiple directory traces not supported"
        return ll_cc_trace[0]

    @staticmethod
    def get_cache_remote_trace(state_tuple: SystemTuple, level: Level) -> List[Trace]:
        ll_cc_traces = list(set(state_tuple.get_arch_remote_trace(level.cache)))
        return ll_cc_traces
