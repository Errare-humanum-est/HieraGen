from DataObjects.ClassMessage import Message
from Parser.ProtoCCcomTreeFct import objListToStringList

from Monitor.ClassDebug import Debug


class ProtoCCTablePrinter(Debug):

    Spacing = 20
    TransFormat = ["StartState", "FinalState", "Access", "InMsg", "OutMsg", "Cond"]

    def __init__(self, debug_enable: bool = True):
        Debug.__init__(self, debug_enable)

    def ptransactions(self, transactions):
        if self.dbg:
            transitions = []
            for transaction in transactions:
                transitions += transaction.gettransitions()

            self.ptransitiontable(transitions)

    def ptransition(self, transition):
        self.ptable(self.TransFormat, [self.outtransition(transition)])

    def ptransitiontable(self, transitions):
        states = []
        for transition in transitions:
            states.append(str(transition.startState))
            states.append(str(transition.finalState))
        states = list(set(states))
        self.pheader("#States: " + str(len(states)) + "   #Transitions: " + str(len(transitions)))

        output = []
        for transition in transitions:
            output.append(self.outtransition(transition))
        self.ptable(self.TransFormat, output)

    @staticmethod
    def outtransition(transition):
        StartState = transition.getstartstate().getstatename()
        FinalState = transition.getfinalstate().getstatename()

        Access = transition.getaccess()
        InMsg = transition.getinmsg()
        if isinstance(InMsg, Message):
            pInMsg = InMsg.getmsgtype()
        else:
            pInMsg = InMsg

        pOutMsg = ""

        for OutMsg in transition.getoutmsg():
            if pOutMsg != "":
                pOutMsg += "; "
            pOutMsg += OutMsg.getmsgtype() + "@" + OutMsg.getvc() + ""

        pCond = ""
        for cond in transition.getcond():
            pCond += cond + "; "

        return [StartState, FinalState, Access, pInMsg, pOutMsg, pCond]

    @staticmethod
    def ptransaction(transactions):
        for transaction in transactions:
            ProtoCCTablePrinter().ptransitions(transaction.gettransitions())

    def ptransitions(self, transitions):
        for transition in transitions:
            ProtoCCTablePrinter().ptransition(transition)
            self.pdebug('$')
            ops = objListToStringList(transition.getoperation())
            for entry in ops:
                self.pdebug(entry)
            self.pdebug()

    def pstates(self, states):
        for state in states:
            self.pheader('$$$$' + state.getstatename())
            self.ptransitions(state.gettransitions())
