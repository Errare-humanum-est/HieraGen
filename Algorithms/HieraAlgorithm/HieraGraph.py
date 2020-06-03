from typing import List

from DataObjects.ClassLevel import Level
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple
from Algorithms.HieraAlgorithm.HieraStateTupleClass.HieraStateTuple import HieraStateTuple

from graphviz import Digraph


class HieraGraph:
    def __init__(self, init_tuple: HieraStateTuple, low_level: Level, high_level: Level):
        self.init_tuple = init_tuple
        self.low_level = low_level
        self.high_level = high_level

    ####################################################################################################################
    # Drawing functions
    ####################################################################################################################

    def draw_system_tuples(self, state_tuples: List[HieraStateTuple]):
        self._draw_system_tuples(state_tuples, self._draw_assymmetric_system_tuple)

    def draw_symmetric_system_tuples(self, state_tuples: List[HieraStateTuple]):
        self._draw_system_tuples(state_tuples, self._draw_symmetric_system_tuple)

    def _draw_system_tuples(self, state_tuples: List[HieraStateTuple], edge_gen_func):
        edges = {}
        graph = Digraph(comment=self.low_level.directory.arch_type + " | " + self.high_level.cache.arch_type,
                        engine='dot')

        prev_tuples = [self.init_tuple]
        next_tuples = []

        while prev_tuples:
            for state_tuple in state_tuples:
                if state_tuple.prev_tuple in prev_tuples:
                    next_tuples.append(state_tuple)

            for next_tuple in next_tuples:
                edge = edge_gen_func(next_tuple)
                if str(edge) not in edges:
                    edges[str(edge)] = edge
                    graph.edge(*edge[0],
                               label=edge[1])

            prev_tuples = next_tuples
            next_tuples = []

        graph.render('level_state_tuples/' + str(self.low_level.directory) + " | " + str(self.high_level.cache) + '.gv',
                     view=True)

    @staticmethod
    def _draw_assymmetric_system_tuple(tuple):
        return [(tuple.draw_str_start_state(), tuple.draw_str_final_state()), tuple.str_access_trace()]

    @staticmethod
    def _draw_symmetric_system_tuple(tuple):
        return [(tuple.symmetric_str_start_state(),
                 tuple.symmetric_str_final_state()),
                tuple.symmetric_str_access_trace()]

    def _draw_dir_cc_tuples(self, state_tuples: List[CcDirStateTuple]):
        edges = {}
        graph = Digraph(comment=self.low_level.directory.arch_type + " | " + self.high_level.cache.arch_type,
                        engine='dot')

        for state_tuple in state_tuples:
            edge = [(state_tuple.draw_str_start_state(), state_tuple.draw_str_final_state())]
            if str(edge) not in edges:
                edges[str(edge)] = edge
                graph.edge(*edge[0])

        graph.render('level_state_tuples/' + str(self.low_level.directory) + " | " + str(self.high_level.cache) + '.gv',
                     view=True)
