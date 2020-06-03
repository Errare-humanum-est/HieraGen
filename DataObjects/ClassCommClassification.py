import enum
from typing import List

from Parser.ClassProtoParser import ProtoParser
from DataObjects.ClassTransaction import Transaction, Transition


class CommunicationClassification:

    undef = "undefined"

    local = "local"

    req = "request"

    rem = "remote"
    rem_req = "remote_request"          # Currently no distinction between remote_request and remote_response
    rem_resp = "remote_response"

    rem_summary = (rem, rem_req, rem_resp)

    resp = "response"
    resp_req = "response_request"
    resp_resp = "response_response"     # Currently no distinction between response_request and response_response

    resp_summary = (resp, resp_resp)

    def classify_parser(self, parser: ProtoParser):

        for arch_node in parser.archNode.values():
            for transaction in arch_node:
                self.classify_transaction(transaction, parser.Accesses)

    def classify_transaction(self, transaction: Transaction, accesses: List[str]):
        traces = transaction.TransTree.gettraces()
        for trace in traces:
            self.classify_transitions(trace, accesses)

    def classify_transitions(self, transitions: List[Transition], accesses: List[str]):
        remote_class = False

        for ind in range(0, len(transitions)):
            if ind == len(transitions)-1:
                self.first_transition(transitions[ind], accesses, remote_class)
            else:
                remote_class = remote_class or self.trail_transitions(transitions[ind])

    def trail_transitions(self, transition: Transition) -> bool:
        if transition.getinmsg():
            if transition.getoutmsg():
                self.check_and_set_trans_class(transition, self.resp_resp)
                return True
            else:
                self.check_and_set_trans_class(transition, self.resp)
                return False
        else:
            assert 0, "Unexpected communication behaviour"

    def first_transition(self, transition: Transition, accesses: List[str], remote_class=False):

        if transition.getaccess() in accesses and not transition.getinmsg():
            if transition.getoutmsg():
                self.check_and_set_trans_class(transition, self.req)
            else:
                transition.comm_class = self.local

        elif transition.getinmsg():
            if not transition.getoutmsg():
                self.check_and_set_trans_class(transition, self.rem)
            else:
                if not remote_class:
                    self.check_and_set_trans_class(transition, self.rem_resp)
                else:
                    self.check_and_set_trans_class(transition, self.rem_req)

        else:
            assert 0, "Unexpected communication behaviour"

    def check_and_set_trans_class(self, transition: Transition, classification: str):
        if not transition.comm_class:
            transition.comm_class = classification
            return
        assert transition.comm_class == classification, "Communication classification mismatch: " + \
                                                        transition.comm_class + " and " + classification
