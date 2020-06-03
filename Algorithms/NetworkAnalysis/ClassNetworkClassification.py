from typing import List, Dict

from DataObjects.ClassTransition import Transition
from antlr3.tree import CommonTree
from Parser.ClassProtoParser import ProtoParser

from Algorithms.NetworkAnalysis.ClassNetwork import ClassNetwork
from DataObjects.ClassCommClassification import CommunicationClassification


class ClassNetworkClassification:

    def __init__(self, parser: ProtoParser, transitions: List[Transition]):
        self.networks:  Dict[str, ClassNetwork] = self.generate_network_objects(parser.getNetwork())
        self.req_networks: List[str] = self.generate_network_request_class(transitions)

        # Automatic virtual channel assignment can be implemented here. Possibly reuse model checker features

    @staticmethod
    def generate_network_objects(network_specs: List[CommonTree]) -> Dict[str, ClassNetwork]:
        network_dict: Dict[str, ClassNetwork] = {}
        for network_spec in network_specs:
            for network_node in network_spec.children:
                network = ClassNetwork(network_node)
                network_dict[str(network)] = network
        return network_dict

    @staticmethod
    # Map transitions related to access to the network
    def generate_network_request_class(transitions: List[Transition]):
        req_networks = []
        for transition in transitions:
            if transition.comm_class == CommunicationClassification().req:
                if transition.access in ProtoParser.Accesses:
                    for outmsg in transition.outMsg:
                        req_networks.append(outmsg.vc)
        return list(set(req_networks))

