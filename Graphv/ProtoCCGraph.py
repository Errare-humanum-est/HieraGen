import os
from graphviz import Digraph
from Monitor.ProtoCCTable import ProtoCCTablePrinter


class ProtoCCGraph:

    EdgeFontSizeInt = '10'
    EdgeFontSizeLoop = '8'
    NodeFontSizeLoop = '12'
    TextFontSize = '15'

    def __init__(self, header, transitions, option=0):
        # Compass points currently not used, as not more than 4 loops were observed
        # CompassPoints=["n","ne","e","se","s","sw","w","nw","c","_"]

        # Create FSM graphs
        self.graph = Digraph(header, filename=(header + '.gv'), engine='dot')
        # Use Splines and resolve Node overlapping
        self.graph.attr(splines='true')
        # Graph direction
        self.graph.attr(rankdir='LR')  # 'LR'
        # Internode and edge spacing

        if option == 0:
            self.graph.attr(nodesep='0.4', ranksep='2')
            self.graph.attr(ratio='0.5')
        else:
            self.graph.attr(nodesep='0.1', ranksep='0.3')
            self.graph.attr(ratio='0.2')

        # Label[RespMsg,FinalState]
        self.graph.attr(label=header, fontsize=self.TextFontSize)

        self._ptransitions(transitions)

        self.graph.view(header, os.getcwd(), False)

    def _ptransitions(self, transitions, color='black'):
        for entry in transitions:
            start_state, final_state, access, p_in_msg, p_out_msg, p_cond = ProtoCCTablePrinter.outtransition(entry)
            
            guardstr = ""
            if access:
                guardstr += "*" + access
            if p_in_msg:
                if access:
                    guardstr += "; "
                guardstr += "<" + p_in_msg
            if p_cond:
                guardstr += "; (" + p_cond + ") "
            if p_out_msg:
                guardstr += "; >" + p_out_msg

            self.graph.edge(start_state,
                            final_state,
                            guardstr,
                            fontsize=self.EdgeFontSizeInt,
                            fontcolor=color
                            )
