# $ANTLR 3.5.2 /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g 2020-02-28 17:10:15

import sys
from antlr3 import *

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__92=92
T__93=93
T__94=94
T__95=95
T__96=96
T__97=97
T__98=98
T__99=99
T__100=100
T__101=101
T__102=102
T__103=103
T__104=104
T__105=105
T__106=106
T__107=107
T__108=108
T__109=109
T__110=110
T__111=111
T__112=112
T__113=113
ACCESS=4
ARCH=5
ARCH_=6
ARRAY=7
ARRAY_=8
ASSIGN_=9
AWAIT=10
AWAIT_=11
BCAST_=12
BOOL=13
BOOLID=14
BOOL_=15
BREAK=16
BREAK_=17
CACHE=18
CACHE_=19
CBRACE=20
CCBRACE=21
CEBRACE=22
COMMA=23
COMMENT=24
COND_=25
CONSTANT=26
CONSTANT_=27
DATA=28
DATA_=29
DDOT=30
DIR=31
DIR_=32
DOT=33
ELEMENT_=34
ELSE=35
ENDIFELSE_=36
ENDIF_=37
ENDPROC_=38
ENDWHEN_=39
EQUALSIGN=40
EVICT=41
FIFO=42
FIFO_=43
GUARD_=44
ID=45
ID_=46
IF=47
IFELSE_=48
IF_=49
INITSTATE_=50
INITVAL_=51
INT=52
INTID=53
INT_=54
LINE_COMMENT=55
MACHN_=56
MCAST_=57
MEM=58
MEM_=59
MINUS=60
MODSTATEFUNC_=61
MSG=62
MSGCSTR_=63
MSG_=64
NCOND_=65
NEG=66
NETWORK=67
NETWORK_=68
NEXT=69
NEXT_=70
NID=71
OBJSET_=72
OBRACE=73
OCBRACE=74
OEBRACE=75
PLUS=76
PROC=77
PROC_=78
RANGE_=79
SEMICOLON=80
SEND_=81
SET=82
SETFUNC_=83
SET_=84
STABLE=85
STABLE_=86
STATE=87
TRANS_=88
WHEN=89
WHEN_=90
WS=91

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 92: "T__92", 93: "T__93", 94: "T__94", 95: "T__95", 96: "T__96", 
    97: "T__97", 98: "T__98", 99: "T__99", 100: "T__100", 101: "T__101", 
    102: "T__102", 103: "T__103", 104: "T__104", 105: "T__105", 106: "T__106", 
    107: "T__107", 108: "T__108", 109: "T__109", 110: "T__110", 111: "T__111", 
    112: "T__112", 113: "T__113", 4: "ACCESS", 5: "ARCH", 6: "ARCH_", 7: "ARRAY", 
    8: "ARRAY_", 9: "ASSIGN_", 10: "AWAIT", 11: "AWAIT_", 12: "BCAST_", 
    13: "BOOL", 14: "BOOLID", 15: "BOOL_", 16: "BREAK", 17: "BREAK_", 18: "CACHE", 
    19: "CACHE_", 20: "CBRACE", 21: "CCBRACE", 22: "CEBRACE", 23: "COMMA", 
    24: "COMMENT", 25: "COND_", 26: "CONSTANT", 27: "CONSTANT_", 28: "DATA", 
    29: "DATA_", 30: "DDOT", 31: "DIR", 32: "DIR_", 33: "DOT", 34: "ELEMENT_", 
    35: "ELSE", 36: "ENDIFELSE_", 37: "ENDIF_", 38: "ENDPROC_", 39: "ENDWHEN_", 
    40: "EQUALSIGN", 41: "EVICT", 42: "FIFO", 43: "FIFO_", 44: "GUARD_", 
    45: "ID", 46: "ID_", 47: "IF", 48: "IFELSE_", 49: "IF_", 50: "INITSTATE_", 
    51: "INITVAL_", 52: "INT", 53: "INTID", 54: "INT_", 55: "LINE_COMMENT", 
    56: "MACHN_", 57: "MCAST_", 58: "MEM", 59: "MEM_", 60: "MINUS", 61: "MODSTATEFUNC_", 
    62: "MSG", 63: "MSGCSTR_", 64: "MSG_", 65: "NCOND_", 66: "NEG", 67: "NETWORK", 
    68: "NETWORK_", 69: "NEXT", 70: "NEXT_", 71: "NID", 72: "OBJSET_", 73: "OBRACE", 
    74: "OCBRACE", 75: "OEBRACE", 76: "PLUS", 77: "PROC", 78: "PROC_", 79: "RANGE_", 
    80: "SEMICOLON", 81: "SEND_", 82: "SET", 83: "SETFUNC_", 84: "SET_", 
    85: "STABLE", 86: "STABLE_", 87: "STATE", 88: "TRANS_", 89: "WHEN", 
    90: "WHEN_", 91: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ACCESS", "ARCH", "ARCH_", "ARRAY", "ARRAY_", "ASSIGN_", "AWAIT", "AWAIT_", 
    "BCAST_", "BOOL", "BOOLID", "BOOL_", "BREAK", "BREAK_", "CACHE", "CACHE_", 
    "CBRACE", "CCBRACE", "CEBRACE", "COMMA", "COMMENT", "COND_", "CONSTANT", 
    "CONSTANT_", "DATA", "DATA_", "DDOT", "DIR", "DIR_", "DOT", "ELEMENT_", 
    "ELSE", "ENDIFELSE_", "ENDIF_", "ENDPROC_", "ENDWHEN_", "EQUALSIGN", 
    "EVICT", "FIFO", "FIFO_", "GUARD_", "ID", "ID_", "IF", "IFELSE_", "IF_", 
    "INITSTATE_", "INITVAL_", "INT", "INTID", "INT_", "LINE_COMMENT", "MACHN_", 
    "MCAST_", "MEM", "MEM_", "MINUS", "MODSTATEFUNC_", "MSG", "MSGCSTR_", 
    "MSG_", "NCOND_", "NEG", "NETWORK", "NETWORK_", "NEXT", "NEXT_", "NID", 
    "OBJSET_", "OBRACE", "OCBRACE", "OEBRACE", "PLUS", "PROC", "PROC_", 
    "RANGE_", "SEMICOLON", "SEND_", "SET", "SETFUNC_", "SET_", "STABLE", 
    "STABLE_", "STATE", "TRANS_", "WHEN", "WHEN_", "WS", "'!='", "'&'", 
    "'<'", "'<='", "'=='", "'>'", "'>='", "'Bcast'", "'Mcast'", "'ModifyStates'", 
    "'Ordered'", "'Send'", "'Unordered'", "'add'", "'bcast'", "'clear'", 
    "'contains'", "'count'", "'del'", "'mcast'", "'send'", "'|'"
]



class ProtoCCParser(Parser):
    grammarFileName = "/home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)




        self.delegates = []

        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class send_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "send_function"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:117:1: send_function : ( 'send' | 'Send' );
    def send_function(self, ):
        retval = self.send_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set1 = None

        set1_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:118:2: ( 'send' | 'Send' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set1 = self.input.LT(1)

                if self.input.LA(1) in {103, 112}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set1))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "send_function"


    class mcast_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "mcast_function"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:122:1: mcast_function : ( 'mcast' | 'Mcast' );
    def mcast_function(self, ):
        retval = self.mcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set2 = None

        set2_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:123:2: ( 'mcast' | 'Mcast' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set2 = self.input.LT(1)

                if self.input.LA(1) in {100, 111}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set2))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mcast_function"


    class bcast_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "bcast_function"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:127:1: bcast_function : ( 'bcast' | 'Bcast' );
    def bcast_function(self, ):
        retval = self.bcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set3 = None

        set3_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:128:2: ( 'bcast' | 'Bcast' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set3 = self.input.LT(1)

                if self.input.LA(1) in {99, 106}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set3))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "bcast_function"


    class modify_state_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "modify_state_function"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:132:1: modify_state_function : 'ModifyStates' ;
    def modify_state_function(self, ):
        retval = self.modify_state_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal4 = None

        string_literal4_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:133:2: ( 'ModifyStates' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:133:4: 'ModifyStates'
                pass 
                root_0 = self._adaptor.nil()


                string_literal4 = self.match(self.input, 101, self.FOLLOW_101_in_modify_state_function653)
                string_literal4_tree = self._adaptor.createWithPayload(string_literal4)
                self._adaptor.addChild(root_0, string_literal4_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "modify_state_function"


    class set_function_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_function_types"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:136:1: set_function_types : ( 'add' | 'count' | 'contains' | 'del' | 'clear' );
    def set_function_types(self, ):
        retval = self.set_function_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set5 = None

        set5_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:137:2: ( 'add' | 'count' | 'contains' | 'del' | 'clear' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set5 = self.input.LT(1)

                if self.input.LA(1) in {105, 107, 108, 109, 110}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set5))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_function_types"


    class relational_operator_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "relational_operator"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:144:1: relational_operator : ( '==' | '!=' | '<=' | '>=' | '<' | '>' );
    def relational_operator(self, ):
        retval = self.relational_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set6 = None

        set6_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:145:2: ( '==' | '!=' | '<=' | '>=' | '<' | '>' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set6 = self.input.LT(1)

                if (94 <= self.input.LA(1) <= 98) or self.input.LA(1) in {92}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set6))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "relational_operator"


    class combinatorial_operator_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "combinatorial_operator"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:153:1: combinatorial_operator : ( '&' | '|' );
    def combinatorial_operator(self, ):
        retval = self.combinatorial_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set7 = None

        set7_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:154:5: ( '&' | '|' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set7 = self.input.LT(1)

                if self.input.LA(1) in {93, 113}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set7))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "combinatorial_operator"


    class document_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "document"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:184:1: document : ( const_decl | init_hw | arch_block | expressions )* ;
    def document(self, ):
        retval = self.document_return()
        retval.start = self.input.LT(1)


        root_0 = None

        const_decl8 = None
        init_hw9 = None
        arch_block10 = None
        expressions11 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:185:2: ( ( const_decl | init_hw | arch_block | expressions )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:185:4: ( const_decl | init_hw | arch_block | expressions )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:185:4: ( const_decl | init_hw | arch_block | expressions )*
                while True: #loop1
                    alt1 = 5
                    LA1 = self.input.LA(1)
                    if LA1 in {CONSTANT}:
                        alt1 = 1
                    elif LA1 in {CACHE, DIR, MEM, MSG, NETWORK}:
                        alt1 = 2
                    elif LA1 in {ARCH}:
                        alt1 = 3
                    elif LA1 in {ID, IF, STATE, 101}:
                        alt1 = 4

                    if alt1 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:185:5: const_decl
                        pass 
                        self._state.following.append(self.FOLLOW_const_decl_in_document976)
                        const_decl8 = self.const_decl()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, const_decl8.tree)



                    elif alt1 == 2:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:185:18: init_hw
                        pass 
                        self._state.following.append(self.FOLLOW_init_hw_in_document980)
                        init_hw9 = self.init_hw()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, init_hw9.tree)



                    elif alt1 == 3:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:185:28: arch_block
                        pass 
                        self._state.following.append(self.FOLLOW_arch_block_in_document984)
                        arch_block10 = self.arch_block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arch_block10.tree)



                    elif alt1 == 4:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:185:41: expressions
                        pass 
                        self._state.following.append(self.FOLLOW_expressions_in_document988)
                        expressions11 = self.expressions()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expressions11.tree)



                    else:
                        break #loop1




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "document"


    class declarations_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "declarations"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:189:1: declarations : ( int_decl | bool_decl | state_decl | data_decl | id_decl );
    def declarations(self, ):
        retval = self.declarations_return()
        retval.start = self.input.LT(1)


        root_0 = None

        int_decl12 = None
        bool_decl13 = None
        state_decl14 = None
        data_decl15 = None
        id_decl16 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:189:14: ( int_decl | bool_decl | state_decl | data_decl | id_decl )
                alt2 = 5
                LA2 = self.input.LA(1)
                if LA2 in {INTID}:
                    alt2 = 1
                elif LA2 in {BOOLID}:
                    alt2 = 2
                elif LA2 in {STATE}:
                    alt2 = 3
                elif LA2 in {DATA}:
                    alt2 = 4
                elif LA2 in {NID, SET}:
                    alt2 = 5
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:189:16: int_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_int_decl_in_declarations1001)
                    int_decl12 = self.int_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, int_decl12.tree)



                elif alt2 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:189:27: bool_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_bool_decl_in_declarations1005)
                    bool_decl13 = self.bool_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bool_decl13.tree)



                elif alt2 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:189:39: state_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_state_decl_in_declarations1009)
                    state_decl14 = self.state_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, state_decl14.tree)



                elif alt2 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:189:52: data_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_data_decl_in_declarations1013)
                    data_decl15 = self.data_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, data_decl15.tree)



                elif alt2 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:189:64: id_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_id_decl_in_declarations1017)
                    id_decl16 = self.id_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, id_decl16.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "declarations"


    class const_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "const_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:191:5: const_decl : CONSTANT ID INT -> ^( CONSTANT_ ID INT ) ;
    def const_decl(self, ):
        retval = self.const_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTANT17 = None
        ID18 = None
        INT19 = None

        CONSTANT17_tree = None
        ID18_tree = None
        INT19_tree = None
        stream_CONSTANT = RewriteRuleTokenStream(self._adaptor, "token CONSTANT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:191:16: ( CONSTANT ID INT -> ^( CONSTANT_ ID INT ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:191:18: CONSTANT ID INT
                pass 
                CONSTANT17 = self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_const_decl1029) 
                stream_CONSTANT.add(CONSTANT17)


                ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_const_decl1031) 
                stream_ID.add(ID18)


                INT19 = self.match(self.input, INT, self.FOLLOW_INT_in_const_decl1033) 
                stream_INT.add(INT19)


                # AST Rewrite
                # elements: ID, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 191:34: -> ^( CONSTANT_ ID INT )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:191:37: ^( CONSTANT_ ID INT )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CONSTANT_, "CONSTANT_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_INT.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "const_decl"


    class int_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "int_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:193:5: int_decl : INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ range ID ( INITVAL_ INT )* ) ;
    def int_decl(self, ):
        retval = self.int_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INTID20 = None
        ID22 = None
        EQUALSIGN23 = None
        INT24 = None
        SEMICOLON25 = None
        range21 = None

        INTID20_tree = None
        ID22_tree = None
        EQUALSIGN23_tree = None
        INT24_tree = None
        SEMICOLON25_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_INTID = RewriteRuleTokenStream(self._adaptor, "token INTID")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_range = RewriteRuleSubtreeStream(self._adaptor, "rule range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:193:14: ( INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ range ID ( INITVAL_ INT )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:193:16: INTID range ID ( EQUALSIGN INT )* SEMICOLON
                pass 
                INTID20 = self.match(self.input, INTID, self.FOLLOW_INTID_in_int_decl1055) 
                stream_INTID.add(INTID20)


                self._state.following.append(self.FOLLOW_range_in_int_decl1057)
                range21 = self.range()

                self._state.following.pop()
                stream_range.add(range21.tree)


                ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_int_decl1059) 
                stream_ID.add(ID22)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:193:31: ( EQUALSIGN INT )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == EQUALSIGN) :
                        alt3 = 1


                    if alt3 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:193:32: EQUALSIGN INT
                        pass 
                        EQUALSIGN23 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_int_decl1062) 
                        stream_EQUALSIGN.add(EQUALSIGN23)


                        INT24 = self.match(self.input, INT, self.FOLLOW_INT_in_int_decl1064) 
                        stream_INT.add(INT24)



                    else:
                        break #loop3


                SEMICOLON25 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_int_decl1068) 
                stream_SEMICOLON.add(SEMICOLON25)


                # AST Rewrite
                # elements: range, ID, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 193:58: -> ^( INT_ range ID ( INITVAL_ INT )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:193:61: ^( INT_ range ID ( INITVAL_ INT )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INT_, "INT_")
                , root_1)

                self._adaptor.addChild(root_1, stream_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:193:77: ( INITVAL_ INT )*
                while stream_INT.hasNext():
                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    )

                    self._adaptor.addChild(root_1, 
                    stream_INT.nextNode()
                    )


                stream_INT.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "int_decl"


    class bool_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "bool_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:194:5: bool_decl : BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( INITVAL_ BOOL )* ) ;
    def bool_decl(self, ):
        retval = self.bool_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BOOLID26 = None
        ID27 = None
        EQUALSIGN28 = None
        BOOL29 = None
        SEMICOLON30 = None

        BOOLID26_tree = None
        ID27_tree = None
        EQUALSIGN28_tree = None
        BOOL29_tree = None
        SEMICOLON30_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_BOOL = RewriteRuleTokenStream(self._adaptor, "token BOOL")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BOOLID = RewriteRuleTokenStream(self._adaptor, "token BOOLID")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:194:15: ( BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( INITVAL_ BOOL )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:194:17: BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON
                pass 
                BOOLID26 = self.match(self.input, BOOLID, self.FOLLOW_BOOLID_in_bool_decl1096) 
                stream_BOOLID.add(BOOLID26)


                ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_bool_decl1098) 
                stream_ID.add(ID27)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:194:27: ( EQUALSIGN BOOL )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQUALSIGN) :
                        alt4 = 1


                    if alt4 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:194:28: EQUALSIGN BOOL
                        pass 
                        EQUALSIGN28 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_bool_decl1101) 
                        stream_EQUALSIGN.add(EQUALSIGN28)


                        BOOL29 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_bool_decl1103) 
                        stream_BOOL.add(BOOL29)



                    else:
                        break #loop4


                SEMICOLON30 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_bool_decl1107) 
                stream_SEMICOLON.add(SEMICOLON30)


                # AST Rewrite
                # elements: ID, BOOL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 194:55: -> ^( BOOL_ ID ( INITVAL_ BOOL )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:194:58: ^( BOOL_ ID ( INITVAL_ BOOL )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BOOL_, "BOOL_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:194:69: ( INITVAL_ BOOL )*
                while stream_BOOL.hasNext():
                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    )

                    self._adaptor.addChild(root_1, 
                    stream_BOOL.nextNode()
                    )


                stream_BOOL.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "bool_decl"


    class state_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "state_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:196:5: state_decl : STATE ID SEMICOLON -> ^( INITSTATE_ ID ) ;
    def state_decl(self, ):
        retval = self.state_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATE31 = None
        ID32 = None
        SEMICOLON33 = None

        STATE31_tree = None
        ID32_tree = None
        SEMICOLON33_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_STATE = RewriteRuleTokenStream(self._adaptor, "token STATE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:196:16: ( STATE ID SEMICOLON -> ^( INITSTATE_ ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:196:18: STATE ID SEMICOLON
                pass 
                STATE31 = self.match(self.input, STATE, self.FOLLOW_STATE_in_state_decl1134) 
                stream_STATE.add(STATE31)


                ID32 = self.match(self.input, ID, self.FOLLOW_ID_in_state_decl1136) 
                stream_ID.add(ID32)


                SEMICOLON33 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_state_decl1138) 
                stream_SEMICOLON.add(SEMICOLON33)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 196:37: -> ^( INITSTATE_ ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:196:40: ^( INITSTATE_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INITSTATE_, "INITSTATE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "state_decl"


    class data_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "data_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:197:5: data_decl : DATA ID SEMICOLON -> ^( DATA_ ID ) ;
    def data_decl(self, ):
        retval = self.data_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DATA34 = None
        ID35 = None
        SEMICOLON36 = None

        DATA34_tree = None
        ID35_tree = None
        SEMICOLON36_tree = None
        stream_DATA = RewriteRuleTokenStream(self._adaptor, "token DATA")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:197:15: ( DATA ID SEMICOLON -> ^( DATA_ ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:197:17: DATA ID SEMICOLON
                pass 
                DATA34 = self.match(self.input, DATA, self.FOLLOW_DATA_in_data_decl1157) 
                stream_DATA.add(DATA34)


                ID35 = self.match(self.input, ID, self.FOLLOW_ID_in_data_decl1159) 
                stream_ID.add(ID35)


                SEMICOLON36 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_data_decl1161) 
                stream_SEMICOLON.add(SEMICOLON36)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 197:35: -> ^( DATA_ ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:197:38: ^( DATA_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DATA_, "DATA_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "data_decl"


    class id_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "id_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:198:5: id_decl : ( set_decl )* NID ID SEMICOLON -> ^( ID_ ( set_decl )* ID ) ;
    def id_decl(self, ):
        retval = self.id_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NID38 = None
        ID39 = None
        SEMICOLON40 = None
        set_decl37 = None

        NID38_tree = None
        ID39_tree = None
        SEMICOLON40_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_NID = RewriteRuleTokenStream(self._adaptor, "token NID")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_set_decl = RewriteRuleSubtreeStream(self._adaptor, "rule set_decl")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:198:13: ( ( set_decl )* NID ID SEMICOLON -> ^( ID_ ( set_decl )* ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:198:15: ( set_decl )* NID ID SEMICOLON
                pass 
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:198:15: ( set_decl )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == SET) :
                        alt5 = 1


                    if alt5 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:198:15: set_decl
                        pass 
                        self._state.following.append(self.FOLLOW_set_decl_in_id_decl1180)
                        set_decl37 = self.set_decl()

                        self._state.following.pop()
                        stream_set_decl.add(set_decl37.tree)



                    else:
                        break #loop5


                NID38 = self.match(self.input, NID, self.FOLLOW_NID_in_id_decl1183) 
                stream_NID.add(NID38)


                ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_id_decl1185) 
                stream_ID.add(ID39)


                SEMICOLON40 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_id_decl1187) 
                stream_SEMICOLON.add(SEMICOLON40)


                # AST Rewrite
                # elements: set_decl, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 198:42: -> ^( ID_ ( set_decl )* ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:198:45: ^( ID_ ( set_decl )* ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ID_, "ID_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:198:51: ( set_decl )*
                while stream_set_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_set_decl.nextTree())


                stream_set_decl.reset();

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "id_decl"


    class set_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:199:5: set_decl : SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) ;
    def set_decl(self, ):
        retval = self.set_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET41 = None
        OEBRACE42 = None
        CEBRACE44 = None
        val_range43 = None

        SET41_tree = None
        OEBRACE42_tree = None
        CEBRACE44_tree = None
        stream_SET = RewriteRuleTokenStream(self._adaptor, "token SET")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:199:14: ( SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:199:16: SET OEBRACE val_range CEBRACE
                pass 
                SET41 = self.match(self.input, SET, self.FOLLOW_SET_in_set_decl1209) 
                stream_SET.add(SET41)


                OEBRACE42 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_set_decl1211) 
                stream_OEBRACE.add(OEBRACE42)


                self._state.following.append(self.FOLLOW_val_range_in_set_decl1213)
                val_range43 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range43.tree)


                CEBRACE44 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_set_decl1215) 
                stream_CEBRACE.add(CEBRACE44)


                # AST Rewrite
                # elements: val_range
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 199:46: -> ^( SET_ val_range )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:199:49: ^( SET_ val_range )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SET_, "SET_")
                , root_1)

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_decl"


    class objset_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "objset_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:200:5: objset_decl : SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) ;
    def objset_decl(self, ):
        retval = self.objset_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET45 = None
        OEBRACE46 = None
        CEBRACE48 = None
        val_range47 = None

        SET45_tree = None
        OEBRACE46_tree = None
        CEBRACE48_tree = None
        stream_SET = RewriteRuleTokenStream(self._adaptor, "token SET")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:200:17: ( SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:200:19: SET OEBRACE val_range CEBRACE
                pass 
                SET45 = self.match(self.input, SET, self.FOLLOW_SET_in_objset_decl1234) 
                stream_SET.add(SET45)


                OEBRACE46 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_objset_decl1236) 
                stream_OEBRACE.add(OEBRACE46)


                self._state.following.append(self.FOLLOW_val_range_in_objset_decl1238)
                val_range47 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range47.tree)


                CEBRACE48 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_objset_decl1240) 
                stream_CEBRACE.add(CEBRACE48)


                # AST Rewrite
                # elements: val_range
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 200:49: -> ^( OBJSET_ val_range )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:200:52: ^( OBJSET_ val_range )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(OBJSET_, "OBJSET_")
                , root_1)

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "objset_decl"


    class range_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "range"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:202:9: range : OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) ;
    def range(self, ):
        retval = self.range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OEBRACE49 = None
        DOT51 = None
        DOT52 = None
        CEBRACE54 = None
        val_range50 = None
        val_range53 = None

        OEBRACE49_tree = None
        DOT51_tree = None
        DOT52_tree = None
        CEBRACE54_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:202:15: ( OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:202:17: OEBRACE val_range DOT DOT val_range CEBRACE
                pass 
                OEBRACE49 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_range1264) 
                stream_OEBRACE.add(OEBRACE49)


                self._state.following.append(self.FOLLOW_val_range_in_range1266)
                val_range50 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range50.tree)


                DOT51 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1268) 
                stream_DOT.add(DOT51)


                DOT52 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1270) 
                stream_DOT.add(DOT52)


                self._state.following.append(self.FOLLOW_val_range_in_range1272)
                val_range53 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range53.tree)


                CEBRACE54 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_range1274) 
                stream_CEBRACE.add(CEBRACE54)


                # AST Rewrite
                # elements: OEBRACE, val_range, DOT, DOT, val_range, CEBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 202:61: -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:202:64: ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(RANGE_, "RANGE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_OEBRACE.nextNode()
                )

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_CEBRACE.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "range"


    class val_range_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "val_range"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:203:9: val_range : ( INT | ID );
    def val_range(self, ):
        retval = self.val_range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set55 = None

        set55_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:203:19: ( INT | ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set55 = self.input.LT(1)

                if self.input.LA(1) in {ID, INT}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set55))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "val_range"


    class array_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "array_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:205:5: array_decl : ARRAY range ;
    def array_decl(self, ):
        retval = self.array_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARRAY56 = None
        range57 = None

        ARRAY56_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:205:16: ( ARRAY range )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:205:18: ARRAY range
                pass 
                root_0 = self._adaptor.nil()


                ARRAY56 = self.match(self.input, ARRAY, self.FOLLOW_ARRAY_in_array_decl1323)
                ARRAY56_tree = self._adaptor.createWithPayload(ARRAY56)
                self._adaptor.addChild(root_0, ARRAY56_tree)



                self._state.following.append(self.FOLLOW_range_in_array_decl1325)
                range57 = self.range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, range57.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "array_decl"


    class fifo_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "fifo_decl"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:206:5: fifo_decl : FIFO range ;
    def fifo_decl(self, ):
        retval = self.fifo_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FIFO58 = None
        range59 = None

        FIFO58_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:206:14: ( FIFO range )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:206:16: FIFO range
                pass 
                root_0 = self._adaptor.nil()


                FIFO58 = self.match(self.input, FIFO, self.FOLLOW_FIFO_in_fifo_decl1335)
                FIFO58_tree = self._adaptor.createWithPayload(FIFO58)
                self._adaptor.addChild(root_0, FIFO58_tree)



                self._state.following.append(self.FOLLOW_range_in_fifo_decl1337)
                range59 = self.range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, range59.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "fifo_decl"


    class init_hw_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "init_hw"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:209:1: init_hw : ( network_block | machines | message_block );
    def init_hw(self, ):
        retval = self.init_hw_return()
        retval.start = self.input.LT(1)


        root_0 = None

        network_block60 = None
        machines61 = None
        message_block62 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:209:9: ( network_block | machines | message_block )
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 in {NETWORK}:
                    alt6 = 1
                elif LA6 in {CACHE, DIR, MEM}:
                    alt6 = 2
                elif LA6 in {MSG}:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:209:11: network_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_block_in_init_hw1347)
                    network_block60 = self.network_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_block60.tree)



                elif alt6 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:209:27: machines
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_machines_in_init_hw1351)
                    machines61 = self.machines()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, machines61.tree)



                elif alt6 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:209:38: message_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_block_in_init_hw1355)
                    message_block62 = self.message_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_block62.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "init_hw"


    class object_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:210:5: object_block : object_expr SEMICOLON -> object_expr ;
    def object_block(self, ):
        retval = self.object_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON64 = None
        object_expr63 = None

        SEMICOLON64_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_object_expr = RewriteRuleSubtreeStream(self._adaptor, "rule object_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:210:18: ( object_expr SEMICOLON -> object_expr )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:210:20: object_expr SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_object_expr_in_object_block1366)
                object_expr63 = self.object_expr()

                self._state.following.pop()
                stream_object_expr.add(object_expr63.tree)


                SEMICOLON64 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_object_block1368) 
                stream_SEMICOLON.add(SEMICOLON64)


                # AST Rewrite
                # elements: object_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 210:42: -> object_expr
                self._adaptor.addChild(root_0, stream_object_expr.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_block"


    class object_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_expr"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:211:5: object_expr : ( object_id | object_func );
    def object_expr(self, ):
        retval = self.object_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        object_id65 = None
        object_func66 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:211:17: ( object_id | object_func )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == ID) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == DOT) :
                        alt7 = 2
                    elif ((92 <= LA7_1 <= 98) or LA7_1 in {BOOL, CBRACE, COMMA, ID, INT, NID, OCBRACE, SEMICOLON, 113}) :
                        alt7 = 1
                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:211:19: object_id
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_id_in_object_expr1383)
                    object_id65 = self.object_id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_id65.tree)



                elif alt7 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:211:31: object_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_func_in_object_expr1387)
                    object_func66 = self.object_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_func66.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_expr"


    class object_id_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_id"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:212:5: object_id : ID -> ^( ID ) ;
    def object_id(self, ):
        retval = self.object_id_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID67 = None

        ID67_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:212:14: ( ID -> ^( ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:212:17: ID
                pass 
                ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_object_id1398) 
                stream_ID.add(ID67)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 212:20: -> ^( ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:212:23: ^( ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_id"


    class object_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_func"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:5: object_func : ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) ;
    def object_func(self, ):
        retval = self.object_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID68 = None
        DOT69 = None
        OBRACE71 = None
        COMMA73 = None
        CBRACE75 = None
        object_idres70 = None
        object_expr72 = None
        object_expr74 = None

        ID68_tree = None
        DOT69_tree = None
        OBRACE71_tree = None
        COMMA73_tree = None
        CBRACE75_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_object_idres = RewriteRuleSubtreeStream(self._adaptor, "rule object_idres")
        stream_object_expr = RewriteRuleSubtreeStream(self._adaptor, "rule object_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:17: ( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:19: ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                pass 
                ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_object_func1415) 
                stream_ID.add(ID68)


                DOT69 = self.match(self.input, DOT, self.FOLLOW_DOT_in_object_func1417) 
                stream_DOT.add(DOT69)


                self._state.following.append(self.FOLLOW_object_idres_in_object_func1419)
                object_idres70 = self.object_idres()

                self._state.following.pop()
                stream_object_idres.add(object_idres70.tree)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:39: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == OBRACE) :
                        alt10 = 1


                    if alt10 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:40: OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE
                        pass 
                        OBRACE71 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_object_func1422) 
                        stream_OBRACE.add(OBRACE71)


                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:47: ( object_expr )*
                        while True: #loop8
                            alt8 = 2
                            LA8_0 = self.input.LA(1)

                            if (LA8_0 == ID) :
                                alt8 = 1


                            if alt8 == 1:
                                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:47: object_expr
                                pass 
                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1424)
                                object_expr72 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr72.tree)



                            else:
                                break #loop8


                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:60: ( COMMA object_expr )*
                        while True: #loop9
                            alt9 = 2
                            LA9_0 = self.input.LA(1)

                            if (LA9_0 == COMMA) :
                                alt9 = 1


                            if alt9 == 1:
                                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:213:61: COMMA object_expr
                                pass 
                                COMMA73 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_object_func1428) 
                                stream_COMMA.add(COMMA73)


                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1430)
                                object_expr74 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr74.tree)



                            else:
                                break #loop9


                        CBRACE75 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_object_func1434) 
                        stream_CBRACE.add(CBRACE75)



                    else:
                        break #loop10


                # AST Rewrite
                # elements: ID, DOT, object_idres, OBRACE, object_expr, COMMA, object_expr, CBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 213:90: -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:214:9: ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_object_idres.nextTree())

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:214:31: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while stream_OBRACE.hasNext() or stream_CBRACE.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_OBRACE.nextNode()
                    )

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:214:39: ( object_expr )*
                    while stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_object_expr.reset();

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:214:52: ( COMMA object_expr )*
                    while stream_COMMA.hasNext() or stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_COMMA.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_COMMA.reset();
                    stream_object_expr.reset();

                    self._adaptor.addChild(root_1, 
                    stream_CBRACE.nextNode()
                    )


                stream_OBRACE.reset();
                stream_CBRACE.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_func"


    class object_idres_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_idres"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:215:5: object_idres : ( ID | NID );
    def object_idres(self, ):
        retval = self.object_idres_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set76 = None

        set76_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:215:17: ( ID | NID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set76 = self.input.LT(1)

                if self.input.LA(1) in {ID, NID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set76))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_idres"


    class machines_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "machines"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:218:5: machines : ( cache_block | dir_block | mem_block );
    def machines(self, ):
        retval = self.machines_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cache_block77 = None
        dir_block78 = None
        mem_block79 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:218:14: ( cache_block | dir_block | mem_block )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 in {CACHE}:
                    alt11 = 1
                elif LA11 in {DIR}:
                    alt11 = 2
                elif LA11 in {MEM}:
                    alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:218:16: cache_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cache_block_in_machines1503)
                    cache_block77 = self.cache_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, cache_block77.tree)



                elif alt11 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:218:30: dir_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_dir_block_in_machines1507)
                    dir_block78 = self.dir_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, dir_block78.tree)



                elif alt11 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:218:42: mem_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_mem_block_in_machines1511)
                    mem_block79 = self.mem_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, mem_block79.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "machines"


    class cache_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cache_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:219:9: cache_block : CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) ;
    def cache_block(self, ):
        retval = self.cache_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CACHE80 = None
        OCBRACE81 = None
        CCBRACE83 = None
        ID85 = None
        SEMICOLON86 = None
        declarations82 = None
        objset_decl84 = None

        CACHE80_tree = None
        OCBRACE81_tree = None
        CCBRACE83_tree = None
        ID85_tree = None
        SEMICOLON86_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CACHE = RewriteRuleTokenStream(self._adaptor, "token CACHE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:219:21: ( CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:219:23: CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                CACHE80 = self.match(self.input, CACHE, self.FOLLOW_CACHE_in_cache_block1526) 
                stream_CACHE.add(CACHE80)


                OCBRACE81 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_cache_block1528) 
                stream_OCBRACE.add(OCBRACE81)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:219:37: ( declarations )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt12 = 1


                    if alt12 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:219:37: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_cache_block1530)
                        declarations82 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations82.tree)



                    else:
                        break #loop12


                CCBRACE83 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_cache_block1533) 
                stream_CCBRACE.add(CCBRACE83)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:219:59: ( objset_decl )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == SET) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:219:59: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_cache_block1535)
                        objset_decl84 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl84.tree)



                    else:
                        break #loop13


                ID85 = self.match(self.input, ID, self.FOLLOW_ID_in_cache_block1538) 
                stream_ID.add(ID85)


                SEMICOLON86 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_cache_block1540) 
                stream_SEMICOLON.add(SEMICOLON86)


                # AST Rewrite
                # elements: ID, objset_decl, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 219:85: -> ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:220:13: ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CACHE_, "CACHE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:220:25: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:220:38: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cache_block"


    class dir_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "dir_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:221:9: dir_block : DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) ;
    def dir_block(self, ):
        retval = self.dir_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DIR87 = None
        OCBRACE88 = None
        CCBRACE90 = None
        ID92 = None
        SEMICOLON93 = None
        declarations89 = None
        objset_decl91 = None

        DIR87_tree = None
        OCBRACE88_tree = None
        CCBRACE90_tree = None
        ID92_tree = None
        SEMICOLON93_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_DIR = RewriteRuleTokenStream(self._adaptor, "token DIR")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:221:19: ( DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:221:21: DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                DIR87 = self.match(self.input, DIR, self.FOLLOW_DIR_in_dir_block1581) 
                stream_DIR.add(DIR87)


                OCBRACE88 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_dir_block1583) 
                stream_OCBRACE.add(OCBRACE88)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:221:33: ( declarations )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt14 = 1


                    if alt14 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:221:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_dir_block1585)
                        declarations89 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations89.tree)



                    else:
                        break #loop14


                CCBRACE90 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_dir_block1588) 
                stream_CCBRACE.add(CCBRACE90)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:221:55: ( objset_decl )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SET) :
                        alt15 = 1


                    if alt15 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:221:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_dir_block1590)
                        objset_decl91 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl91.tree)



                    else:
                        break #loop15


                ID92 = self.match(self.input, ID, self.FOLLOW_ID_in_dir_block1593) 
                stream_ID.add(ID92)


                SEMICOLON93 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_dir_block1595) 
                stream_SEMICOLON.add(SEMICOLON93)


                # AST Rewrite
                # elements: ID, objset_decl, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 221:81: -> ^( DIR_ ID ( objset_decl )* ( declarations )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:222:13: ^( DIR_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DIR_, "DIR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:222:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:222:36: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "dir_block"


    class mem_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "mem_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:223:9: mem_block : MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( MEM_ ID ( objset_decl )* ( declarations )* ) ;
    def mem_block(self, ):
        retval = self.mem_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MEM94 = None
        OCBRACE95 = None
        CCBRACE97 = None
        ID99 = None
        SEMICOLON100 = None
        declarations96 = None
        objset_decl98 = None

        MEM94_tree = None
        OCBRACE95_tree = None
        CCBRACE97_tree = None
        ID99_tree = None
        SEMICOLON100_tree = None
        stream_MEM = RewriteRuleTokenStream(self._adaptor, "token MEM")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:223:19: ( MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( MEM_ ID ( objset_decl )* ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:223:21: MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                MEM94 = self.match(self.input, MEM, self.FOLLOW_MEM_in_mem_block1636) 
                stream_MEM.add(MEM94)


                OCBRACE95 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_mem_block1638) 
                stream_OCBRACE.add(OCBRACE95)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:223:33: ( declarations )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt16 = 1


                    if alt16 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:223:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_mem_block1640)
                        declarations96 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations96.tree)



                    else:
                        break #loop16


                CCBRACE97 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_mem_block1643) 
                stream_CCBRACE.add(CCBRACE97)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:223:55: ( objset_decl )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == SET) :
                        alt17 = 1


                    if alt17 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:223:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_mem_block1645)
                        objset_decl98 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl98.tree)



                    else:
                        break #loop17


                ID99 = self.match(self.input, ID, self.FOLLOW_ID_in_mem_block1648) 
                stream_ID.add(ID99)


                SEMICOLON100 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_mem_block1650) 
                stream_SEMICOLON.add(SEMICOLON100)


                # AST Rewrite
                # elements: ID, objset_decl, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 223:81: -> ^( MEM_ ID ( objset_decl )* ( declarations )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:224:13: ^( MEM_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MEM_, "MEM_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:224:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:224:36: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mem_block"


    class network_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:227:5: network_block : NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) ;
    def network_block(self, ):
        retval = self.network_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NETWORK101 = None
        OCBRACE102 = None
        CCBRACE104 = None
        SEMICOLON105 = None
        network_element103 = None

        NETWORK101_tree = None
        OCBRACE102_tree = None
        CCBRACE104_tree = None
        SEMICOLON105_tree = None
        stream_NETWORK = RewriteRuleTokenStream(self._adaptor, "token NETWORK")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_network_element = RewriteRuleSubtreeStream(self._adaptor, "rule network_element")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:227:19: ( NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:227:21: NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON
                pass 
                NETWORK101 = self.match(self.input, NETWORK, self.FOLLOW_NETWORK_in_network_block1694) 
                stream_NETWORK.add(NETWORK101)


                OCBRACE102 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_network_block1696) 
                stream_OCBRACE.add(OCBRACE102)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:227:37: ( network_element )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 in {102, 104}) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:227:37: network_element
                        pass 
                        self._state.following.append(self.FOLLOW_network_element_in_network_block1698)
                        network_element103 = self.network_element()

                        self._state.following.pop()
                        stream_network_element.add(network_element103.tree)



                    else:
                        break #loop18


                CCBRACE104 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_network_block1701) 
                stream_CCBRACE.add(CCBRACE104)


                SEMICOLON105 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_block1703) 
                stream_SEMICOLON.add(SEMICOLON105)


                # AST Rewrite
                # elements: network_element
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 227:72: -> ^( NETWORK_ ( network_element )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:227:75: ^( NETWORK_ ( network_element )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NETWORK_, "NETWORK_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:227:86: ( network_element )*
                while stream_network_element.hasNext():
                    self._adaptor.addChild(root_1, stream_network_element.nextTree())


                stream_network_element.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_block"


    class element_type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "element_type"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:228:9: element_type : ( 'Ordered' | 'Unordered' );
    def element_type(self, ):
        retval = self.element_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set106 = None

        set106_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:228:22: ( 'Ordered' | 'Unordered' )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set106 = self.input.LT(1)

                if self.input.LA(1) in {102, 104}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set106))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "element_type"


    class network_element_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_element"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:229:9: network_element : element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) ;
    def network_element(self, ):
        retval = self.network_element_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID108 = None
        SEMICOLON109 = None
        element_type107 = None

        ID108_tree = None
        SEMICOLON109_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_element_type = RewriteRuleSubtreeStream(self._adaptor, "rule element_type")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:229:25: ( element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:229:27: element_type ID SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_element_type_in_network_element1746)
                element_type107 = self.element_type()

                self._state.following.pop()
                stream_element_type.add(element_type107.tree)


                ID108 = self.match(self.input, ID, self.FOLLOW_ID_in_network_element1748) 
                stream_ID.add(ID108)


                SEMICOLON109 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_element1750) 
                stream_SEMICOLON.add(SEMICOLON109)


                # AST Rewrite
                # elements: element_type, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 229:53: -> ^( ELEMENT_ element_type ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:229:56: ^( ELEMENT_ element_type ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ELEMENT_, "ELEMENT_")
                , root_1)

                self._adaptor.addChild(root_1, stream_element_type.nextTree())

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_element"


    class network_send_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_send"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:230:5: network_send : ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) ;
    def network_send(self, ):
        retval = self.network_send_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID110 = None
        DOT111 = None
        OBRACE113 = None
        ID114 = None
        CBRACE115 = None
        SEMICOLON116 = None
        send_function112 = None

        ID110_tree = None
        DOT111_tree = None
        OBRACE113_tree = None
        ID114_tree = None
        CBRACE115_tree = None
        SEMICOLON116_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_send_function = RewriteRuleSubtreeStream(self._adaptor, "rule send_function")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:230:18: ( ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:230:20: ID DOT send_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID110 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1771) 
                stream_ID.add(ID110)


                DOT111 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_send1773) 
                stream_DOT.add(DOT111)


                self._state.following.append(self.FOLLOW_send_function_in_network_send1775)
                send_function112 = self.send_function()

                self._state.following.pop()
                stream_send_function.add(send_function112.tree)


                OBRACE113 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_send1777) 
                stream_OBRACE.add(OBRACE113)


                ID114 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1779) 
                stream_ID.add(ID114)


                CBRACE115 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_send1781) 
                stream_CBRACE.add(CBRACE115)


                SEMICOLON116 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_send1783) 
                stream_SEMICOLON.add(SEMICOLON116)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 230:68: -> ^( SEND_ ID ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:230:71: ^( SEND_ ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SEND_, "SEND_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_send"


    class network_bcast_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_bcast"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:231:5: network_bcast : ID DOT bcast_function OBRACE ID CBRACE SEMICOLON -> ^( BCAST_ ID ID ) ;
    def network_bcast(self, ):
        retval = self.network_bcast_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID117 = None
        DOT118 = None
        OBRACE120 = None
        ID121 = None
        CBRACE122 = None
        SEMICOLON123 = None
        bcast_function119 = None

        ID117_tree = None
        DOT118_tree = None
        OBRACE120_tree = None
        ID121_tree = None
        CBRACE122_tree = None
        SEMICOLON123_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_bcast_function = RewriteRuleSubtreeStream(self._adaptor, "rule bcast_function")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:231:18: ( ID DOT bcast_function OBRACE ID CBRACE SEMICOLON -> ^( BCAST_ ID ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:231:20: ID DOT bcast_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID117 = self.match(self.input, ID, self.FOLLOW_ID_in_network_bcast1803) 
                stream_ID.add(ID117)


                DOT118 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_bcast1805) 
                stream_DOT.add(DOT118)


                self._state.following.append(self.FOLLOW_bcast_function_in_network_bcast1807)
                bcast_function119 = self.bcast_function()

                self._state.following.pop()
                stream_bcast_function.add(bcast_function119.tree)


                OBRACE120 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_bcast1809) 
                stream_OBRACE.add(OBRACE120)


                ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_network_bcast1811) 
                stream_ID.add(ID121)


                CBRACE122 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_bcast1813) 
                stream_CBRACE.add(CBRACE122)


                SEMICOLON123 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_bcast1815) 
                stream_SEMICOLON.add(SEMICOLON123)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 231:69: -> ^( BCAST_ ID ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:231:72: ^( BCAST_ ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BCAST_, "BCAST_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_bcast"


    class network_mcast_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_mcast"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:232:5: network_mcast : ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) ;
    def network_mcast(self, ):
        retval = self.network_mcast_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID124 = None
        DOT125 = None
        OBRACE127 = None
        ID128 = None
        COMMA129 = None
        ID130 = None
        CBRACE131 = None
        SEMICOLON132 = None
        mcast_function126 = None

        ID124_tree = None
        DOT125_tree = None
        OBRACE127_tree = None
        ID128_tree = None
        COMMA129_tree = None
        ID130_tree = None
        CBRACE131_tree = None
        SEMICOLON132_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_mcast_function = RewriteRuleSubtreeStream(self._adaptor, "rule mcast_function")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:232:18: ( ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:232:20: ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON
                pass 
                ID124 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1835) 
                stream_ID.add(ID124)


                DOT125 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_mcast1837) 
                stream_DOT.add(DOT125)


                self._state.following.append(self.FOLLOW_mcast_function_in_network_mcast1839)
                mcast_function126 = self.mcast_function()

                self._state.following.pop()
                stream_mcast_function.add(mcast_function126.tree)


                OBRACE127 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_mcast1841) 
                stream_OBRACE.add(OBRACE127)


                ID128 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1843) 
                stream_ID.add(ID128)


                COMMA129 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_network_mcast1845) 
                stream_COMMA.add(COMMA129)


                ID130 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1847) 
                stream_ID.add(ID130)


                CBRACE131 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_mcast1849) 
                stream_CBRACE.add(CBRACE131)


                SEMICOLON132 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_mcast1851) 
                stream_SEMICOLON.add(SEMICOLON132)


                # AST Rewrite
                # elements: ID, ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 232:78: -> ^( MCAST_ ID ID ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:232:81: ^( MCAST_ ID ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MCAST_, "MCAST_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_mcast"


    class message_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:235:5: message_block : MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) ;
    def message_block(self, ):
        retval = self.message_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MSG133 = None
        ID134 = None
        OCBRACE135 = None
        CCBRACE137 = None
        SEMICOLON138 = None
        declarations136 = None

        MSG133_tree = None
        ID134_tree = None
        OCBRACE135_tree = None
        CCBRACE137_tree = None
        SEMICOLON138_tree = None
        stream_MSG = RewriteRuleTokenStream(self._adaptor, "token MSG")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:235:19: ( MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:235:21: MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON
                pass 
                MSG133 = self.match(self.input, MSG, self.FOLLOW_MSG_in_message_block1881) 
                stream_MSG.add(MSG133)


                ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_message_block1883) 
                stream_ID.add(ID134)


                OCBRACE135 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_message_block1885) 
                stream_OCBRACE.add(OCBRACE135)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:235:36: ( declarations )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt19 = 1


                    if alt19 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:235:36: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_message_block1887)
                        declarations136 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations136.tree)



                    else:
                        break #loop19


                CCBRACE137 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_message_block1890) 
                stream_CCBRACE.add(CCBRACE137)


                SEMICOLON138 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_message_block1892) 
                stream_SEMICOLON.add(SEMICOLON138)


                # AST Rewrite
                # elements: ID, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 235:68: -> ^( MSG_ ID ( declarations )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:235:71: ^( MSG_ ID ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSG_, "MSG_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:235:81: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_block"


    class message_constr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_constr"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:5: message_constr : ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) ;
    def message_constr(self, ):
        retval = self.message_constr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID139 = None
        OBRACE140 = None
        COMMA142 = None
        CBRACE144 = None
        message_expr141 = None
        message_expr143 = None

        ID139_tree = None
        OBRACE140_tree = None
        COMMA142_tree = None
        CBRACE144_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_message_expr = RewriteRuleSubtreeStream(self._adaptor, "rule message_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:20: ( ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:22: ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE
                pass 
                ID139 = self.match(self.input, ID, self.FOLLOW_ID_in_message_constr1914) 
                stream_ID.add(ID139)


                OBRACE140 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_message_constr1916) 
                stream_OBRACE.add(OBRACE140)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:32: ( message_expr )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 in {BOOL, ID, INT, NID}) :
                        alt20 = 1


                    if alt20 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:32: message_expr
                        pass 
                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr1918)
                        message_expr141 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr141.tree)



                    else:
                        break #loop20


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:46: ( COMMA message_expr )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == COMMA) :
                        alt21 = 1


                    if alt21 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:47: COMMA message_expr
                        pass 
                        COMMA142 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_message_constr1922) 
                        stream_COMMA.add(COMMA142)


                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr1924)
                        message_expr143 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr143.tree)



                    else:
                        break #loop21


                CBRACE144 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_message_constr1928) 
                stream_CBRACE.add(CBRACE144)


                # AST Rewrite
                # elements: ID, message_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 236:75: -> ^( MSGCSTR_ ID ( message_expr )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:78: ^( MSGCSTR_ ID ( message_expr )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSGCSTR_, "MSGCSTR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:236:92: ( message_expr )*
                while stream_message_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_message_expr.nextTree())


                stream_message_expr.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_constr"


    class message_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_expr"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:237:5: message_expr : ( object_expr | set_func | INT | BOOL | NID );
    def message_expr(self, ):
        retval = self.message_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT147 = None
        BOOL148 = None
        NID149 = None
        object_expr145 = None
        set_func146 = None

        INT147_tree = None
        BOOL148_tree = None
        NID149_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:237:18: ( object_expr | set_func | INT | BOOL | NID )
                alt22 = 5
                LA22 = self.input.LA(1)
                if LA22 in {ID}:
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == DOT) :
                        LA22_5 = self.input.LA(3)

                        if (LA22_5 in {ID, NID}) :
                            alt22 = 1
                        elif (LA22_5 in {105, 107, 108, 109, 110}) :
                            alt22 = 2
                        else:
                            nvae = NoViableAltException("", 22, 5, self.input)

                            raise nvae


                    elif (LA22_1 in {BOOL, CBRACE, COMMA, ID, INT, NID}) :
                        alt22 = 1
                    else:
                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae


                elif LA22 in {INT}:
                    alt22 = 3
                elif LA22 in {BOOL}:
                    alt22 = 4
                elif LA22 in {NID}:
                    alt22 = 5
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:237:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_message_expr1950)
                    object_expr145 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr145.tree)



                elif alt22 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:237:34: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_message_expr1954)
                    set_func146 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func146.tree)



                elif alt22 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:237:45: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT147 = self.match(self.input, INT, self.FOLLOW_INT_in_message_expr1958)
                    INT147_tree = self._adaptor.createWithPayload(INT147)
                    self._adaptor.addChild(root_0, INT147_tree)




                elif alt22 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:237:51: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL148 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_message_expr1962)
                    BOOL148_tree = self._adaptor.createWithPayload(BOOL148)
                    self._adaptor.addChild(root_0, BOOL148_tree)




                elif alt22 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:237:58: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID149 = self.match(self.input, NID, self.FOLLOW_NID_in_message_expr1966)
                    NID149_tree = self._adaptor.createWithPayload(NID149)
                    self._adaptor.addChild(root_0, NID149_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_expr"


    class set_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:240:5: set_block : set_func SEMICOLON -> set_func ;
    def set_block(self, ):
        retval = self.set_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON151 = None
        set_func150 = None

        SEMICOLON151_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_set_func = RewriteRuleSubtreeStream(self._adaptor, "rule set_func")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:240:15: ( set_func SEMICOLON -> set_func )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:240:17: set_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_set_func_in_set_block1984)
                set_func150 = self.set_func()

                self._state.following.pop()
                stream_set_func.add(set_func150.tree)


                SEMICOLON151 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_set_block1986) 
                stream_SEMICOLON.add(SEMICOLON151)


                # AST Rewrite
                # elements: set_func
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 240:36: -> set_func
                self._adaptor.addChild(root_0, stream_set_func.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_block"


    class set_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_func"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:241:5: set_func : ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) ;
    def set_func(self, ):
        retval = self.set_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID152 = None
        DOT153 = None
        OBRACE155 = None
        CBRACE157 = None
        set_function_types154 = None
        set_nest156 = None

        ID152_tree = None
        DOT153_tree = None
        OBRACE155_tree = None
        CBRACE157_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_set_function_types = RewriteRuleSubtreeStream(self._adaptor, "rule set_function_types")
        stream_set_nest = RewriteRuleSubtreeStream(self._adaptor, "rule set_nest")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:241:14: ( ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:241:16: ID DOT set_function_types OBRACE ( set_nest )* CBRACE
                pass 
                ID152 = self.match(self.input, ID, self.FOLLOW_ID_in_set_func2001) 
                stream_ID.add(ID152)


                DOT153 = self.match(self.input, DOT, self.FOLLOW_DOT_in_set_func2003) 
                stream_DOT.add(DOT153)


                self._state.following.append(self.FOLLOW_set_function_types_in_set_func2005)
                set_function_types154 = self.set_function_types()

                self._state.following.pop()
                stream_set_function_types.add(set_function_types154.tree)


                OBRACE155 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_set_func2007) 
                stream_OBRACE.add(OBRACE155)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:241:49: ( set_nest )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == ID) :
                        alt23 = 1


                    if alt23 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:241:49: set_nest
                        pass 
                        self._state.following.append(self.FOLLOW_set_nest_in_set_func2009)
                        set_nest156 = self.set_nest()

                        self._state.following.pop()
                        stream_set_nest.add(set_nest156.tree)



                    else:
                        break #loop23


                CBRACE157 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_set_func2012) 
                stream_CBRACE.add(CBRACE157)


                # AST Rewrite
                # elements: ID, DOT, set_function_types, OBRACE, set_nest, CBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 241:66: -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:242:9: ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SETFUNC_, "SETFUNC_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_set_function_types.nextTree())

                self._adaptor.addChild(root_1, 
                stream_OBRACE.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:242:53: ( set_nest )*
                while stream_set_nest.hasNext():
                    self._adaptor.addChild(root_1, stream_set_nest.nextTree())


                stream_set_nest.reset();

                self._adaptor.addChild(root_1, 
                stream_CBRACE.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_func"


    class set_nest_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_nest"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:243:5: set_nest : ( set_func | object_expr );
    def set_nest(self, ):
        retval = self.set_nest_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set_func158 = None
        object_expr159 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:243:14: ( set_func | object_expr )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == ID) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == DOT) :
                        LA24_2 = self.input.LA(3)

                        if (LA24_2 in {105, 107, 108, 109, 110}) :
                            alt24 = 1
                        elif (LA24_2 in {ID, NID}) :
                            alt24 = 2
                        else:
                            nvae = NoViableAltException("", 24, 2, self.input)

                            raise nvae


                    elif (LA24_1 in {CBRACE, ID}) :
                        alt24 = 2
                    else:
                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:243:16: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_set_nest2050)
                    set_func158 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func158.tree)



                elif alt24 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:243:27: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_set_nest2054)
                    object_expr159 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr159.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_nest"


    class mod_state_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "mod_state_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:246:5: mod_state_block : mod_state_func SEMICOLON -> mod_state_func ;
    def mod_state_block(self, ):
        retval = self.mod_state_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON161 = None
        mod_state_func160 = None

        SEMICOLON161_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_mod_state_func = RewriteRuleSubtreeStream(self._adaptor, "rule mod_state_func")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:246:21: ( mod_state_func SEMICOLON -> mod_state_func )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:246:23: mod_state_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_mod_state_func_in_mod_state_block2072)
                mod_state_func160 = self.mod_state_func()

                self._state.following.pop()
                stream_mod_state_func.add(mod_state_func160.tree)


                SEMICOLON161 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_mod_state_block2074) 
                stream_SEMICOLON.add(SEMICOLON161)


                # AST Rewrite
                # elements: mod_state_func
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 246:48: -> mod_state_func
                self._adaptor.addChild(root_0, stream_mod_state_func.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mod_state_block"


    class mod_state_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "mod_state_func"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:247:5: mod_state_func : modify_state_function OBRACE ID COMMA ID CBRACE -> ^( MODSTATEFUNC_ ID ID ) ;
    def mod_state_func(self, ):
        retval = self.mod_state_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE163 = None
        ID164 = None
        COMMA165 = None
        ID166 = None
        CBRACE167 = None
        modify_state_function162 = None

        OBRACE163_tree = None
        ID164_tree = None
        COMMA165_tree = None
        ID166_tree = None
        CBRACE167_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_modify_state_function = RewriteRuleSubtreeStream(self._adaptor, "rule modify_state_function")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:247:19: ( modify_state_function OBRACE ID COMMA ID CBRACE -> ^( MODSTATEFUNC_ ID ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:247:21: modify_state_function OBRACE ID COMMA ID CBRACE
                pass 
                self._state.following.append(self.FOLLOW_modify_state_function_in_mod_state_func2088)
                modify_state_function162 = self.modify_state_function()

                self._state.following.pop()
                stream_modify_state_function.add(modify_state_function162.tree)


                OBRACE163 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_mod_state_func2090) 
                stream_OBRACE.add(OBRACE163)


                ID164 = self.match(self.input, ID, self.FOLLOW_ID_in_mod_state_func2092) 
                stream_ID.add(ID164)


                COMMA165 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_mod_state_func2094) 
                stream_COMMA.add(COMMA165)


                ID166 = self.match(self.input, ID, self.FOLLOW_ID_in_mod_state_func2096) 
                stream_ID.add(ID166)


                CBRACE167 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_mod_state_func2098) 
                stream_CBRACE.add(CBRACE167)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 247:69: -> ^( MODSTATEFUNC_ ID ID )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:247:72: ^( MODSTATEFUNC_ ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MODSTATEFUNC_, "MODSTATEFUNC_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mod_state_func"


    class arch_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "arch_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:250:1: arch_block : ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) ;
    def arch_block(self, ):
        retval = self.arch_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARCH168 = None
        ID169 = None
        OCBRACE170 = None
        CCBRACE172 = None
        arch_body171 = None

        ARCH168_tree = None
        ID169_tree = None
        OCBRACE170_tree = None
        CCBRACE172_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ARCH = RewriteRuleTokenStream(self._adaptor, "token ARCH")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_arch_body = RewriteRuleSubtreeStream(self._adaptor, "rule arch_body")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:250:12: ( ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:250:14: ARCH ID OCBRACE arch_body CCBRACE
                pass 
                ARCH168 = self.match(self.input, ARCH, self.FOLLOW_ARCH_in_arch_block2118) 
                stream_ARCH.add(ARCH168)


                ID169 = self.match(self.input, ID, self.FOLLOW_ID_in_arch_block2120) 
                stream_ID.add(ID169)


                OCBRACE170 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_arch_block2122) 
                stream_OCBRACE.add(OCBRACE170)


                self._state.following.append(self.FOLLOW_arch_body_in_arch_block2124)
                arch_body171 = self.arch_body()

                self._state.following.pop()
                stream_arch_body.add(arch_body171.tree)


                CCBRACE172 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_arch_block2126) 
                stream_CCBRACE.add(CCBRACE172)


                # AST Rewrite
                # elements: ID, arch_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 250:48: -> ^( ARCH_ ^( MACHN_ ID ) arch_body )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:250:51: ^( ARCH_ ^( MACHN_ ID ) arch_body )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARCH_, "ARCH_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:250:59: ^( MACHN_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MACHN_, "MACHN_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_1, stream_arch_body.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arch_block"


    class arch_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "arch_body"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:252:1: arch_body : ( stable_def | process_block )* ;
    def arch_body(self, ):
        retval = self.arch_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        stable_def173 = None
        process_block174 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:252:10: ( ( stable_def | process_block )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:252:12: ( stable_def | process_block )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:252:12: ( stable_def | process_block )*
                while True: #loop25
                    alt25 = 3
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == STABLE) :
                        alt25 = 1
                    elif (LA25_0 == PROC) :
                        alt25 = 2


                    if alt25 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:252:13: stable_def
                        pass 
                        self._state.following.append(self.FOLLOW_stable_def_in_arch_body2148)
                        stable_def173 = self.stable_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stable_def173.tree)



                    elif alt25 == 2:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:252:26: process_block
                        pass 
                        self._state.following.append(self.FOLLOW_process_block_in_arch_body2152)
                        process_block174 = self.process_block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, process_block174.tree)



                    else:
                        break #loop25




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arch_body"


    class stable_def_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "stable_def"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:254:1: stable_def : STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) ;
    def stable_def(self, ):
        retval = self.stable_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STABLE175 = None
        OCBRACE176 = None
        ID177 = None
        COMMA178 = None
        ID179 = None
        CCBRACE180 = None

        STABLE175_tree = None
        OCBRACE176_tree = None
        ID177_tree = None
        COMMA178_tree = None
        ID179_tree = None
        CCBRACE180_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_STABLE = RewriteRuleTokenStream(self._adaptor, "token STABLE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:254:12: ( STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:254:14: STABLE OCBRACE ID ( COMMA ID )* CCBRACE
                pass 
                STABLE175 = self.match(self.input, STABLE, self.FOLLOW_STABLE_in_stable_def2162) 
                stream_STABLE.add(STABLE175)


                OCBRACE176 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_stable_def2164) 
                stream_OCBRACE.add(OCBRACE176)


                ID177 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def2166) 
                stream_ID.add(ID177)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:254:32: ( COMMA ID )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == COMMA) :
                        alt26 = 1


                    if alt26 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:254:33: COMMA ID
                        pass 
                        COMMA178 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_stable_def2169) 
                        stream_COMMA.add(COMMA178)


                        ID179 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def2171) 
                        stream_ID.add(ID179)



                    else:
                        break #loop26


                CCBRACE180 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_stable_def2175) 
                stream_CCBRACE.add(CCBRACE180)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 254:52: -> ^( STABLE_ ID ( ID )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:254:55: ^( STABLE_ ID ( ID )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(STABLE_, "STABLE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:254:68: ( ID )*
                while stream_ID.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )


                stream_ID.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "stable_def"


    class process_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_block"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:1: process_block : PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) ;
    def process_block(self, ):
        retval = self.process_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC181 = None
        OCBRACE183 = None
        CCBRACE185 = None
        process_trans182 = None
        process_expr184 = None

        PROC181_tree = None
        OCBRACE183_tree = None
        CCBRACE185_tree = None
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_process_trans = RewriteRuleSubtreeStream(self._adaptor, "rule process_trans")
        stream_process_expr = RewriteRuleSubtreeStream(self._adaptor, "rule process_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:15: ( PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:17: PROC process_trans OCBRACE ( process_expr )* CCBRACE
                pass 
                PROC181 = self.match(self.input, PROC, self.FOLLOW_PROC_in_process_block2194) 
                stream_PROC.add(PROC181)


                self._state.following.append(self.FOLLOW_process_trans_in_process_block2196)
                process_trans182 = self.process_trans()

                self._state.following.pop()
                stream_process_trans.add(process_trans182.tree)


                OCBRACE183 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_process_block2198) 
                stream_OCBRACE.add(OCBRACE183)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:44: ( process_expr )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 in {AWAIT, ID, IF, STATE, 101}) :
                        alt27 = 1


                    if alt27 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:44: process_expr
                        pass 
                        self._state.following.append(self.FOLLOW_process_expr_in_process_block2200)
                        process_expr184 = self.process_expr()

                        self._state.following.pop()
                        stream_process_expr.add(process_expr184.tree)



                    else:
                        break #loop27


                CCBRACE185 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_process_block2203) 
                stream_CCBRACE.add(CCBRACE185)


                # AST Rewrite
                # elements: process_trans, process_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 256:66: -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:69: ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROC_, "PROC_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_trans.nextTree())

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:91: ( process_expr )*
                while stream_process_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_process_expr.nextTree())


                stream_process_expr.reset();

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:256:105: ^( ENDPROC_ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ENDPROC_, "ENDPROC_")
                , root_2)

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_block"


    class process_trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_trans"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:257:5: process_trans : OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) ;
    def process_trans(self, ):
        retval = self.process_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE186 = None
        ID187 = None
        COMMA188 = None
        CBRACE191 = None
        process_events189 = None
        process_finalstate190 = None

        OBRACE186_tree = None
        ID187_tree = None
        COMMA188_tree = None
        CBRACE191_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_process_events = RewriteRuleSubtreeStream(self._adaptor, "rule process_events")
        stream_process_finalstate = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalstate")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:257:19: ( OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:257:21: OBRACE ID COMMA process_events ( process_finalstate )* CBRACE
                pass 
                OBRACE186 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_process_trans2229) 
                stream_OBRACE.add(OBRACE186)


                ID187 = self.match(self.input, ID, self.FOLLOW_ID_in_process_trans2231) 
                stream_ID.add(ID187)


                COMMA188 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_trans2233) 
                stream_COMMA.add(COMMA188)


                self._state.following.append(self.FOLLOW_process_events_in_process_trans2235)
                process_events189 = self.process_events()

                self._state.following.pop()
                stream_process_events.add(process_events189.tree)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:257:52: ( process_finalstate )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == COMMA) :
                        alt28 = 1


                    if alt28 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:257:52: process_finalstate
                        pass 
                        self._state.following.append(self.FOLLOW_process_finalstate_in_process_trans2237)
                        process_finalstate190 = self.process_finalstate()

                        self._state.following.pop()
                        stream_process_finalstate.add(process_finalstate190.tree)



                    else:
                        break #loop28


                CBRACE191 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_process_trans2240) 
                stream_CBRACE.add(CBRACE191)


                # AST Rewrite
                # elements: ID, process_events, process_finalstate
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 257:79: -> ^( TRANS_ ID process_events ( process_finalstate )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:257:82: ^( TRANS_ ID process_events ( process_finalstate )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TRANS_, "TRANS_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_process_events.nextTree())

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:257:109: ( process_finalstate )*
                while stream_process_finalstate.hasNext():
                    self._adaptor.addChild(root_1, stream_process_finalstate.nextTree())


                stream_process_finalstate.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_trans"


    class process_finalstate_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_finalstate"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:258:5: process_finalstate : COMMA process_finalident -> ^( process_finalident ) ;
    def process_finalstate(self, ):
        retval = self.process_finalstate_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA192 = None
        process_finalident193 = None

        COMMA192_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:258:23: ( COMMA process_finalident -> ^( process_finalident ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:258:25: COMMA process_finalident
                pass 
                COMMA192 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_finalstate2263) 
                stream_COMMA.add(COMMA192)


                self._state.following.append(self.FOLLOW_process_finalident_in_process_finalstate2265)
                process_finalident193 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident193.tree)


                # AST Rewrite
                # elements: process_finalident
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 258:50: -> ^( process_finalident )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:258:53: ^( process_finalident )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_process_finalident.nextNode(), root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_finalstate"


    class process_finalident_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_finalident"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:259:5: process_finalident : ( ID | STATE ) ;
    def process_finalident(self, ):
        retval = self.process_finalident_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set194 = None

        set194_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:259:23: ( ( ID | STATE ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set194 = self.input.LT(1)

                if self.input.LA(1) in {ID, STATE}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set194))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_finalident"


    class process_events_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_events"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:260:5: process_events : ( ACCESS | EVICT | ID ) ;
    def process_events(self, ):
        retval = self.process_events_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set195 = None

        set195_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:260:20: ( ( ACCESS | EVICT | ID ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set195 = self.input.LT(1)

                if self.input.LA(1) in {ACCESS, EVICT, ID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set195))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_events"


    class process_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_expr"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:261:5: process_expr : ( expressions | network_send | network_mcast | network_bcast | transaction );
    def process_expr(self, ):
        retval = self.process_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions196 = None
        network_send197 = None
        network_mcast198 = None
        network_bcast199 = None
        transaction200 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:261:17: ( expressions | network_send | network_mcast | network_bcast | transaction )
                alt29 = 5
                LA29 = self.input.LA(1)
                if LA29 in {ID}:
                    LA29_1 = self.input.LA(2)

                    if (LA29_1 == DOT) :
                        LA29 = self.input.LA(3)
                        if LA29 in {ID, NID, 105, 107, 108, 109, 110}:
                            alt29 = 1
                        elif LA29 in {103, 112}:
                            alt29 = 2
                        elif LA29 in {100, 111}:
                            alt29 = 3
                        elif LA29 in {99, 106}:
                            alt29 = 4
                        else:
                            nvae = NoViableAltException("", 29, 6, self.input)

                            raise nvae


                    elif (LA29_1 in {EQUALSIGN, SEMICOLON}) :
                        alt29 = 1
                    else:
                        nvae = NoViableAltException("", 29, 1, self.input)

                        raise nvae


                elif LA29 in {IF, STATE, 101}:
                    alt29 = 1
                elif LA29 in {AWAIT}:
                    alt29 = 5
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:261:19: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_process_expr2318)
                    expressions196 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions196.tree)



                elif alt29 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:261:33: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_process_expr2322)
                    network_send197 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send197.tree)



                elif alt29 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:261:48: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_process_expr2326)
                    network_mcast198 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast198.tree)



                elif alt29 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:261:64: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_process_expr2330)
                    network_bcast199 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast199.tree)



                elif alt29 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:261:79: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_process_expr2333)
                    transaction200 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction200.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_expr"


    class transaction_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "transaction"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:264:1: transaction : AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) ;
    def transaction(self, ):
        retval = self.transaction_return()
        retval.start = self.input.LT(1)


        root_0 = None

        AWAIT201 = None
        OCBRACE202 = None
        CCBRACE204 = None
        trans203 = None

        AWAIT201_tree = None
        OCBRACE202_tree = None
        CCBRACE204_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_AWAIT = RewriteRuleTokenStream(self._adaptor, "token AWAIT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:264:13: ( AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:264:15: AWAIT OCBRACE ( trans )* CCBRACE
                pass 
                AWAIT201 = self.match(self.input, AWAIT, self.FOLLOW_AWAIT_in_transaction2343) 
                stream_AWAIT.add(AWAIT201)


                OCBRACE202 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_transaction2345) 
                stream_OCBRACE.add(OCBRACE202)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:264:29: ( trans )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == WHEN) :
                        alt30 = 1


                    if alt30 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:264:29: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_transaction2347)
                        trans203 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans203.tree)



                    else:
                        break #loop30


                CCBRACE204 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_transaction2350) 
                stream_CCBRACE.add(CCBRACE204)


                # AST Rewrite
                # elements: trans
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 264:44: -> ^( AWAIT_ ( trans )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:264:47: ^( AWAIT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(AWAIT_, "AWAIT_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:264:56: ( trans )*
                while stream_trans.hasNext():
                    self._adaptor.addChild(root_1, stream_trans.nextTree())


                stream_trans.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "transaction"


    class trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "trans"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:5: trans : WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) ;
    def trans(self, ):
        retval = self.trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHEN205 = None
        ID206 = None
        DDOT207 = None
        trans_body208 = None

        WHEN205_tree = None
        ID206_tree = None
        DDOT207_tree = None
        stream_WHEN = RewriteRuleTokenStream(self._adaptor, "token WHEN")
        stream_DDOT = RewriteRuleTokenStream(self._adaptor, "token DDOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_trans_body = RewriteRuleSubtreeStream(self._adaptor, "rule trans_body")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:11: ( WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:13: WHEN ID DDOT ( trans_body )*
                pass 
                WHEN205 = self.match(self.input, WHEN, self.FOLLOW_WHEN_in_trans2370) 
                stream_WHEN.add(WHEN205)


                ID206 = self.match(self.input, ID, self.FOLLOW_ID_in_trans2372) 
                stream_ID.add(ID206)


                DDOT207 = self.match(self.input, DDOT, self.FOLLOW_DDOT_in_trans2374) 
                stream_DDOT.add(DDOT207)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:26: ( trans_body )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 in {AWAIT, BREAK, ID, IF, NEXT, STATE, 101}) :
                        alt31 = 1


                    if alt31 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:26: trans_body
                        pass 
                        self._state.following.append(self.FOLLOW_trans_body_in_trans2376)
                        trans_body208 = self.trans_body()

                        self._state.following.pop()
                        stream_trans_body.add(trans_body208.tree)



                    else:
                        break #loop31


                # AST Rewrite
                # elements: ID, trans_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 265:38: -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:41: ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(WHEN_, "WHEN_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:49: ^( GUARD_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(GUARD_, "GUARD_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:265:62: ( trans_body )*
                while stream_trans_body.hasNext():
                    self._adaptor.addChild(root_1, stream_trans_body.nextTree())


                stream_trans_body.reset();

                self._adaptor.addChild(root_1, 
                self._adaptor.createFromType(ENDWHEN_, "ENDWHEN_")
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "trans"


    class trans_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "trans_body"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:9: trans_body : ( expressions | next_trans | next_break | transaction | network_send | network_mcast | network_bcast );
    def trans_body(self, ):
        retval = self.trans_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions209 = None
        next_trans210 = None
        next_break211 = None
        transaction212 = None
        network_send213 = None
        network_mcast214 = None
        network_bcast215 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:20: ( expressions | next_trans | next_break | transaction | network_send | network_mcast | network_bcast )
                alt32 = 7
                LA32 = self.input.LA(1)
                if LA32 in {ID}:
                    LA32_1 = self.input.LA(2)

                    if (LA32_1 == DOT) :
                        LA32 = self.input.LA(3)
                        if LA32 in {ID, NID, 105, 107, 108, 109, 110}:
                            alt32 = 1
                        elif LA32 in {103, 112}:
                            alt32 = 5
                        elif LA32 in {100, 111}:
                            alt32 = 6
                        elif LA32 in {99, 106}:
                            alt32 = 7
                        else:
                            nvae = NoViableAltException("", 32, 8, self.input)

                            raise nvae


                    elif (LA32_1 in {EQUALSIGN, SEMICOLON}) :
                        alt32 = 1
                    else:
                        nvae = NoViableAltException("", 32, 1, self.input)

                        raise nvae


                elif LA32 in {IF, STATE, 101}:
                    alt32 = 1
                elif LA32 in {NEXT}:
                    alt32 = 2
                elif LA32 in {BREAK}:
                    alt32 = 3
                elif LA32 in {AWAIT}:
                    alt32 = 4
                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:22: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_trans_body2409)
                    expressions209 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions209.tree)



                elif alt32 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:36: next_trans
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_trans_in_trans_body2413)
                    next_trans210 = self.next_trans()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_trans210.tree)



                elif alt32 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:49: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_trans_body2417)
                    next_break211 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break211.tree)



                elif alt32 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:62: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_trans_body2421)
                    transaction212 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction212.tree)



                elif alt32 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:76: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_trans_body2425)
                    network_send213 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send213.tree)



                elif alt32 == 6:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:91: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_trans_body2429)
                    network_mcast214 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast214.tree)



                elif alt32 == 7:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:266:107: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_trans_body2433)
                    network_bcast215 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast215.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "trans_body"


    class next_trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "next_trans"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:267:13: next_trans : NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) ;
    def next_trans(self, ):
        retval = self.next_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEXT216 = None
        OCBRACE217 = None
        CCBRACE219 = None
        trans218 = None

        NEXT216_tree = None
        OCBRACE217_tree = None
        CCBRACE219_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_NEXT = RewriteRuleTokenStream(self._adaptor, "token NEXT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:267:23: ( NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:267:25: NEXT OCBRACE ( trans )* CCBRACE
                pass 
                NEXT216 = self.match(self.input, NEXT, self.FOLLOW_NEXT_in_next_trans2451) 
                stream_NEXT.add(NEXT216)


                OCBRACE217 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_next_trans2453) 
                stream_OCBRACE.add(OCBRACE217)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:267:38: ( trans )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == WHEN) :
                        alt33 = 1


                    if alt33 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:267:38: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_next_trans2455)
                        trans218 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans218.tree)



                    else:
                        break #loop33


                CCBRACE219 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_next_trans2458) 
                stream_CCBRACE.add(CCBRACE219)


                # AST Rewrite
                # elements: trans
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 267:53: -> ^( NEXT_ ( trans )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:267:56: ^( NEXT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NEXT_, "NEXT_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:267:64: ( trans )*
                while stream_trans.hasNext():
                    self._adaptor.addChild(root_1, stream_trans.nextTree())


                stream_trans.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "next_trans"


    class next_break_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "next_break"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:269:1: next_break : BREAK SEMICOLON -> ^( BREAK_ ) ;
    def next_break(self, ):
        retval = self.next_break_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BREAK220 = None
        SEMICOLON221 = None

        BREAK220_tree = None
        SEMICOLON221_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BREAK = RewriteRuleTokenStream(self._adaptor, "token BREAK")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:269:12: ( BREAK SEMICOLON -> ^( BREAK_ ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:269:14: BREAK SEMICOLON
                pass 
                BREAK220 = self.match(self.input, BREAK, self.FOLLOW_BREAK_in_next_break2475) 
                stream_BREAK.add(BREAK220)


                SEMICOLON221 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_next_break2477) 
                stream_SEMICOLON.add(SEMICOLON221)


                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 269:30: -> ^( BREAK_ )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:269:33: ^( BREAK_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BREAK_, "BREAK_")
                , root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "next_break"


    class expressions_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "expressions"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:272:1: expressions : ( assignment | conditional | object_block | set_block | mod_state_block );
    def expressions(self, ):
        retval = self.expressions_return()
        retval.start = self.input.LT(1)


        root_0 = None

        assignment222 = None
        conditional223 = None
        object_block224 = None
        set_block225 = None
        mod_state_block226 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:272:13: ( assignment | conditional | object_block | set_block | mod_state_block )
                alt34 = 5
                LA34 = self.input.LA(1)
                if LA34 in {ID}:
                    LA34 = self.input.LA(2)
                    if LA34 in {DOT}:
                        LA34_5 = self.input.LA(3)

                        if (LA34_5 in {ID, NID}) :
                            alt34 = 3
                        elif (LA34_5 in {105, 107, 108, 109, 110}) :
                            alt34 = 4
                        else:
                            nvae = NoViableAltException("", 34, 5, self.input)

                            raise nvae


                    elif LA34 in {EQUALSIGN}:
                        alt34 = 1
                    elif LA34 in {SEMICOLON}:
                        alt34 = 3
                    else:
                        nvae = NoViableAltException("", 34, 1, self.input)

                        raise nvae


                elif LA34 in {IF}:
                    alt34 = 2
                elif LA34 in {STATE}:
                    alt34 = 1
                elif LA34 in {101}:
                    alt34 = 5
                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae


                if alt34 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:272:15: assignment
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_assignment_in_expressions2493)
                    assignment222 = self.assignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, assignment222.tree)



                elif alt34 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:272:28: conditional
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_conditional_in_expressions2497)
                    conditional223 = self.conditional()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, conditional223.tree)



                elif alt34 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:272:42: object_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_block_in_expressions2501)
                    object_block224 = self.object_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_block224.tree)



                elif alt34 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:272:57: set_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_block_in_expressions2505)
                    set_block225 = self.set_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_block225.tree)



                elif alt34 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:272:69: mod_state_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_mod_state_block_in_expressions2509)
                    mod_state_block226 = self.mod_state_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, mod_state_block226.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "expressions"


    class assignment_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "assignment"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:273:1: assignment : process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) ;
    def assignment(self, ):
        retval = self.assignment_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EQUALSIGN228 = None
        SEMICOLON230 = None
        process_finalident227 = None
        assign_types229 = None

        EQUALSIGN228_tree = None
        SEMICOLON230_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_assign_types = RewriteRuleSubtreeStream(self._adaptor, "rule assign_types")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:273:12: ( process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:273:14: process_finalident EQUALSIGN assign_types SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_process_finalident_in_assignment2516)
                process_finalident227 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident227.tree)


                EQUALSIGN228 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_assignment2518) 
                stream_EQUALSIGN.add(EQUALSIGN228)


                self._state.following.append(self.FOLLOW_assign_types_in_assignment2520)
                assign_types229 = self.assign_types()

                self._state.following.pop()
                stream_assign_types.add(assign_types229.tree)


                SEMICOLON230 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_assignment2522) 
                stream_SEMICOLON.add(SEMICOLON230)


                # AST Rewrite
                # elements: process_finalident, EQUALSIGN, assign_types
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 273:65: -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:273:68: ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ASSIGN_, "ASSIGN_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_finalident.nextTree())

                self._adaptor.addChild(root_1, 
                stream_EQUALSIGN.nextNode()
                )

                self._adaptor.addChild(root_1, stream_assign_types.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "assignment"


    class assign_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "assign_types"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:5: assign_types : ( object_expr | message_constr | math_op | set_func | INT | BOOL );
    def assign_types(self, ):
        retval = self.assign_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT235 = None
        BOOL236 = None
        object_expr231 = None
        message_constr232 = None
        math_op233 = None
        set_func234 = None

        INT235_tree = None
        BOOL236_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:18: ( object_expr | message_constr | math_op | set_func | INT | BOOL )
                alt35 = 6
                LA35 = self.input.LA(1)
                if LA35 in {ID}:
                    LA35 = self.input.LA(2)
                    if LA35 in {DOT}:
                        LA35_4 = self.input.LA(3)

                        if (LA35_4 in {ID, NID}) :
                            alt35 = 1
                        elif (LA35_4 in {105, 107, 108, 109, 110}) :
                            alt35 = 4
                        else:
                            nvae = NoViableAltException("", 35, 4, self.input)

                            raise nvae


                    elif LA35 in {OBRACE}:
                        alt35 = 2
                    elif LA35 in {SEMICOLON}:
                        alt35 = 1
                    elif LA35 in {MINUS, PLUS}:
                        alt35 = 3
                    else:
                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae


                elif LA35 in {INT}:
                    LA35_2 = self.input.LA(2)

                    if (LA35_2 in {MINUS, PLUS}) :
                        alt35 = 3
                    elif (LA35_2 == SEMICOLON) :
                        alt35 = 5
                    else:
                        nvae = NoViableAltException("", 35, 2, self.input)

                        raise nvae


                elif LA35 in {BOOL}:
                    alt35 = 6
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae


                if alt35 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_assign_types2544)
                    object_expr231 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr231.tree)



                elif alt35 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:34: message_constr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_constr_in_assign_types2548)
                    message_constr232 = self.message_constr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_constr232.tree)



                elif alt35 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:51: math_op
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_math_op_in_assign_types2552)
                    math_op233 = self.math_op()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, math_op233.tree)



                elif alt35 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:61: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_assign_types2556)
                    set_func234 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func234.tree)



                elif alt35 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:72: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT235 = self.match(self.input, INT, self.FOLLOW_INT_in_assign_types2560)
                    INT235_tree = self._adaptor.createWithPayload(INT235)
                    self._adaptor.addChild(root_0, INT235_tree)




                elif alt35 == 6:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:274:78: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL236 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_assign_types2564)
                    BOOL236_tree = self._adaptor.createWithPayload(BOOL236)
                    self._adaptor.addChild(root_0, BOOL236_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "assign_types"


    class math_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "math_op"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:275:5: math_op : val_range ( PLUS | MINUS ) val_range ;
    def math_op(self, ):
        retval = self.math_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set238 = None
        val_range237 = None
        val_range239 = None

        set238_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:275:13: ( val_range ( PLUS | MINUS ) val_range )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:275:15: val_range ( PLUS | MINUS ) val_range
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_val_range_in_math_op2575)
                val_range237 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range237.tree)


                set238 = self.input.LT(1)

                if self.input.LA(1) in {MINUS, PLUS}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set238))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self._state.following.append(self.FOLLOW_val_range_in_math_op2585)
                val_range239 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range239.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "math_op"


    class conditional_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "conditional"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:278:1: conditional : ( if_stmt | ifnot_stmt );
    def conditional(self, ):
        retval = self.conditional_return()
        retval.start = self.input.LT(1)


        root_0 = None

        if_stmt240 = None
        ifnot_stmt241 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:278:12: ( if_stmt | ifnot_stmt )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == IF) :
                    LA36_1 = self.input.LA(2)

                    if (LA36_1 == NEG) :
                        alt36 = 2
                    elif (LA36_1 in {BOOL, ID, INT, NID, OBRACE}) :
                        alt36 = 1
                    else:
                        nvae = NoViableAltException("", 36, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:278:14: if_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_if_stmt_in_conditional2594)
                    if_stmt240 = self.if_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, if_stmt240.tree)



                elif alt36 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:278:24: ifnot_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_ifnot_stmt_in_conditional2598)
                    ifnot_stmt241 = self.ifnot_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, ifnot_stmt241.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "conditional"


    class if_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "if_stmt"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:279:5: if_stmt : IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) ;
    def if_stmt(self, ):
        retval = self.if_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF242 = None
        OCBRACE244 = None
        CCBRACE246 = None
        ELSE247 = None
        OCBRACE248 = None
        CCBRACE250 = None
        cond_comb243 = None
        if_expression245 = None
        else_expression249 = None

        IF242_tree = None
        OCBRACE244_tree = None
        CCBRACE246_tree = None
        ELSE247_tree = None
        OCBRACE248_tree = None
        CCBRACE250_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_else_expression = RewriteRuleSubtreeStream(self._adaptor, "rule else_expression")
        stream_if_expression = RewriteRuleSubtreeStream(self._adaptor, "rule if_expression")
        stream_cond_comb = RewriteRuleSubtreeStream(self._adaptor, "rule cond_comb")
        t_else = 0
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:280:5: ( IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:280:7: IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF242 = self.match(self.input, IF, self.FOLLOW_IF_in_if_stmt2617) 
                stream_IF.add(IF242)


                self._state.following.append(self.FOLLOW_cond_comb_in_if_stmt2619)
                cond_comb243 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb243.tree)


                OCBRACE244 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2621) 
                stream_OCBRACE.add(OCBRACE244)


                self._state.following.append(self.FOLLOW_if_expression_in_if_stmt2623)
                if_expression245 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression245.tree)


                CCBRACE246 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2625) 
                stream_CCBRACE.add(CCBRACE246)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:281:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == ELSE) :
                        alt37 = 1


                    if alt37 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:281:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE247 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_if_stmt2632) 
                        stream_ELSE.add(ELSE247)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE248 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2636) 
                        stream_OCBRACE.add(OCBRACE248)


                        self._state.following.append(self.FOLLOW_else_expression_in_if_stmt2638)
                        else_expression249 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression249.tree)


                        CCBRACE250 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2640) 
                        stream_CCBRACE.add(CCBRACE250)



                    else:
                        break #loop37


                # AST Rewrite
                # elements: cond_comb, if_expression, cond_comb, else_expression, cond_comb, if_expression, cond_comb
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                if t_else:
                    # 282:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:282:18: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:282:28: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:282:34: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:282:53: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:282:76: ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:282:82: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:282:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 283:5: -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:283:8: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:283:18: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:283:24: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:283:43: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:283:66: ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:283:72: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "if_stmt"


    class ifnot_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "ifnot_stmt"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:286:5: ifnot_stmt : IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) ;
    def ifnot_stmt(self, ):
        retval = self.ifnot_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF251 = None
        NEG252 = None
        OCBRACE254 = None
        CCBRACE256 = None
        ELSE257 = None
        OCBRACE258 = None
        CCBRACE260 = None
        cond_comb253 = None
        if_expression255 = None
        else_expression259 = None

        IF251_tree = None
        NEG252_tree = None
        OCBRACE254_tree = None
        CCBRACE256_tree = None
        ELSE257_tree = None
        OCBRACE258_tree = None
        CCBRACE260_tree = None
        stream_NEG = RewriteRuleTokenStream(self._adaptor, "token NEG")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_else_expression = RewriteRuleSubtreeStream(self._adaptor, "rule else_expression")
        stream_if_expression = RewriteRuleSubtreeStream(self._adaptor, "rule if_expression")
        stream_cond_comb = RewriteRuleSubtreeStream(self._adaptor, "rule cond_comb")
        t_else = 0
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:287:5: ( IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:287:7: IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF251 = self.match(self.input, IF, self.FOLLOW_IF_in_ifnot_stmt2746) 
                stream_IF.add(IF251)


                NEG252 = self.match(self.input, NEG, self.FOLLOW_NEG_in_ifnot_stmt2748) 
                stream_NEG.add(NEG252)


                self._state.following.append(self.FOLLOW_cond_comb_in_ifnot_stmt2750)
                cond_comb253 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb253.tree)


                OCBRACE254 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt2752) 
                stream_OCBRACE.add(OCBRACE254)


                self._state.following.append(self.FOLLOW_if_expression_in_ifnot_stmt2754)
                if_expression255 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression255.tree)


                CCBRACE256 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt2756) 
                stream_CCBRACE.add(CCBRACE256)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:288:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == ELSE) :
                        alt38 = 1


                    if alt38 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:288:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE257 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_ifnot_stmt2763) 
                        stream_ELSE.add(ELSE257)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE258 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt2767) 
                        stream_OCBRACE.add(OCBRACE258)


                        self._state.following.append(self.FOLLOW_else_expression_in_ifnot_stmt2769)
                        else_expression259 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression259.tree)


                        CCBRACE260 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt2771) 
                        stream_CCBRACE.add(CCBRACE260)



                    else:
                        break #loop38


                # AST Rewrite
                # elements: cond_comb, if_expression, cond_comb, else_expression, cond_comb, if_expression, cond_comb
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                if t_else:
                    # 289:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:289:18: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:289:28: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:289:34: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:289:54: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:289:77: ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:289:83: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:289:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 290:5: -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:290:8: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:290:18: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:290:24: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:290:44: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:290:67: ^( IF_ ^( COND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:290:73: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "ifnot_stmt"


    class if_expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "if_expression"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:293:9: if_expression : ( exprwbreak )* ;
    def if_expression(self, ):
        retval = self.if_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak261 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:293:22: ( ( exprwbreak )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:293:24: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:293:24: ( exprwbreak )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 in {AWAIT, BREAK, ID, IF, STATE, 101}) :
                        alt39 = 1


                    if alt39 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:293:24: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_if_expression2872)
                        exprwbreak261 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak261.tree)



                    else:
                        break #loop39




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "if_expression"


    class else_expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "else_expression"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:294:9: else_expression : ( exprwbreak )* ;
    def else_expression(self, ):
        retval = self.else_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak262 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:294:24: ( ( exprwbreak )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:294:26: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:294:26: ( exprwbreak )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 in {AWAIT, BREAK, ID, IF, STATE, 101}) :
                        alt40 = 1


                    if alt40 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:294:26: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_else_expression2887)
                        exprwbreak262 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak262.tree)



                    else:
                        break #loop40




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "else_expression"


    class exprwbreak_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "exprwbreak"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:9: exprwbreak : ( expressions | network_send | network_mcast | network_bcast | transaction | next_break );
    def exprwbreak(self, ):
        retval = self.exprwbreak_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions263 = None
        network_send264 = None
        network_mcast265 = None
        network_bcast266 = None
        transaction267 = None
        next_break268 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:19: ( expressions | network_send | network_mcast | network_bcast | transaction | next_break )
                alt41 = 6
                LA41 = self.input.LA(1)
                if LA41 in {ID}:
                    LA41_1 = self.input.LA(2)

                    if (LA41_1 == DOT) :
                        LA41 = self.input.LA(3)
                        if LA41 in {ID, NID, 105, 107, 108, 109, 110}:
                            alt41 = 1
                        elif LA41 in {103, 112}:
                            alt41 = 2
                        elif LA41 in {100, 111}:
                            alt41 = 3
                        elif LA41 in {99, 106}:
                            alt41 = 4
                        else:
                            nvae = NoViableAltException("", 41, 7, self.input)

                            raise nvae


                    elif (LA41_1 in {EQUALSIGN, SEMICOLON}) :
                        alt41 = 1
                    else:
                        nvae = NoViableAltException("", 41, 1, self.input)

                        raise nvae


                elif LA41 in {IF, STATE, 101}:
                    alt41 = 1
                elif LA41 in {AWAIT}:
                    alt41 = 5
                elif LA41 in {BREAK}:
                    alt41 = 6
                else:
                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae


                if alt41 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:21: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_exprwbreak2902)
                    expressions263 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions263.tree)



                elif alt41 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:35: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_exprwbreak2906)
                    network_send264 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send264.tree)



                elif alt41 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:50: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_exprwbreak2910)
                    network_mcast265 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast265.tree)



                elif alt41 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:66: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_exprwbreak2914)
                    network_bcast266 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast266.tree)



                elif alt41 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:82: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_exprwbreak2918)
                    transaction267 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction267.tree)



                elif alt41 == 6:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:295:96: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_exprwbreak2922)
                    next_break268 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break268.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "exprwbreak"


    class cond_comb_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_comb"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:296:9: cond_comb : cond_rel ( combinatorial_operator cond_rel )* ;
    def cond_comb(self, ):
        retval = self.cond_comb_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_rel269 = None
        combinatorial_operator270 = None
        cond_rel271 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:296:18: ( cond_rel ( combinatorial_operator cond_rel )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:296:20: cond_rel ( combinatorial_operator cond_rel )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb2936)
                cond_rel269 = self.cond_rel()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_rel269.tree)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:296:29: ( combinatorial_operator cond_rel )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 in {93, 113}) :
                        alt42 = 1


                    if alt42 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:296:30: combinatorial_operator cond_rel
                        pass 
                        self._state.following.append(self.FOLLOW_combinatorial_operator_in_cond_comb2939)
                        combinatorial_operator270 = self.combinatorial_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, combinatorial_operator270.tree)


                        self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb2941)
                        cond_rel271 = self.cond_rel()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_rel271.tree)



                    else:
                        break #loop42




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_comb"


    class cond_rel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_rel"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:297:9: cond_rel : ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel ;
    def cond_rel(self, ):
        retval = self.cond_rel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE272 = None
        CBRACE274 = None
        cond_sel273 = None

        OBRACE272_tree = None
        CBRACE274_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_cond_sel = RewriteRuleSubtreeStream(self._adaptor, "rule cond_sel")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:297:18: ( ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:297:20: ( OBRACE )* cond_sel ( CBRACE )*
                pass 
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:297:20: ( OBRACE )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == OBRACE) :
                        alt43 = 1


                    if alt43 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:297:20: OBRACE
                        pass 
                        OBRACE272 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_cond_rel2958) 
                        stream_OBRACE.add(OBRACE272)



                    else:
                        break #loop43


                self._state.following.append(self.FOLLOW_cond_sel_in_cond_rel2961)
                cond_sel273 = self.cond_sel()

                self._state.following.pop()
                stream_cond_sel.add(cond_sel273.tree)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:297:37: ( CBRACE )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == CBRACE) :
                        alt44 = 1


                    if alt44 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:297:37: CBRACE
                        pass 
                        CBRACE274 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_cond_rel2963) 
                        stream_CBRACE.add(CBRACE274)



                    else:
                        break #loop44


                # AST Rewrite
                # elements: cond_sel
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 297:45: -> cond_sel
                self._adaptor.addChild(root_0, stream_cond_sel.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_rel"


    class cond_sel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_sel"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:298:13: cond_sel : cond_types ( relational_operator cond_types )* ;
    def cond_sel(self, ):
        retval = self.cond_sel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_types275 = None
        relational_operator276 = None
        cond_types277 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:298:22: ( cond_types ( relational_operator cond_types )* )
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:298:24: cond_types ( relational_operator cond_types )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_types_in_cond_sel2987)
                cond_types275 = self.cond_types()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_types275.tree)


                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:298:35: ( relational_operator cond_types )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if ((94 <= LA45_0 <= 98) or LA45_0 in {92}) :
                        alt45 = 1


                    if alt45 == 1:
                        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:298:36: relational_operator cond_types
                        pass 
                        self._state.following.append(self.FOLLOW_relational_operator_in_cond_sel2990)
                        relational_operator276 = self.relational_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, relational_operator276.tree)


                        self._state.following.append(self.FOLLOW_cond_types_in_cond_sel2992)
                        cond_types277 = self.cond_types()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_types277.tree)



                    else:
                        break #loop45




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_sel"


    class cond_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_types"
    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:299:13: cond_types : ( object_expr | set_func | INT | BOOL | NID );
    def cond_types(self, ):
        retval = self.cond_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT280 = None
        BOOL281 = None
        NID282 = None
        object_expr278 = None
        set_func279 = None

        INT280_tree = None
        BOOL281_tree = None
        NID282_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:299:24: ( object_expr | set_func | INT | BOOL | NID )
                alt46 = 5
                LA46 = self.input.LA(1)
                if LA46 in {ID}:
                    LA46_1 = self.input.LA(2)

                    if (LA46_1 == DOT) :
                        LA46_5 = self.input.LA(3)

                        if (LA46_5 in {ID, NID}) :
                            alt46 = 1
                        elif (LA46_5 in {105, 107, 108, 109, 110}) :
                            alt46 = 2
                        else:
                            nvae = NoViableAltException("", 46, 5, self.input)

                            raise nvae


                    elif ((92 <= LA46_1 <= 98) or LA46_1 in {CBRACE, OCBRACE, 113}) :
                        alt46 = 1
                    else:
                        nvae = NoViableAltException("", 46, 1, self.input)

                        raise nvae


                elif LA46 in {INT}:
                    alt46 = 3
                elif LA46 in {BOOL}:
                    alt46 = 4
                elif LA46 in {NID}:
                    alt46 = 5
                else:
                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae


                if alt46 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:299:26: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_cond_types3013)
                    object_expr278 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr278.tree)



                elif alt46 == 2:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:299:40: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_cond_types3017)
                    set_func279 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func279.tree)



                elif alt46 == 3:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:299:51: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT280 = self.match(self.input, INT, self.FOLLOW_INT_in_cond_types3021)
                    INT280_tree = self._adaptor.createWithPayload(INT280)
                    self._adaptor.addChild(root_0, INT280_tree)




                elif alt46 == 4:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:299:57: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL281 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_cond_types3025)
                    BOOL281_tree = self._adaptor.createWithPayload(BOOL281)
                    self._adaptor.addChild(root_0, BOOL281_tree)




                elif alt46 == 5:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:299:64: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID282 = self.match(self.input, NID, self.FOLLOW_NID_in_cond_types3029)
                    NID282_tree = self._adaptor.createWithPayload(NID282)
                    self._adaptor.addChild(root_0, NID282_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_types"



 

    FOLLOW_101_in_modify_state_function653 = frozenset([1])
    FOLLOW_const_decl_in_document976 = frozenset([1, 5, 18, 26, 31, 45, 47, 58, 62, 67, 87, 101])
    FOLLOW_init_hw_in_document980 = frozenset([1, 5, 18, 26, 31, 45, 47, 58, 62, 67, 87, 101])
    FOLLOW_arch_block_in_document984 = frozenset([1, 5, 18, 26, 31, 45, 47, 58, 62, 67, 87, 101])
    FOLLOW_expressions_in_document988 = frozenset([1, 5, 18, 26, 31, 45, 47, 58, 62, 67, 87, 101])
    FOLLOW_int_decl_in_declarations1001 = frozenset([1])
    FOLLOW_bool_decl_in_declarations1005 = frozenset([1])
    FOLLOW_state_decl_in_declarations1009 = frozenset([1])
    FOLLOW_data_decl_in_declarations1013 = frozenset([1])
    FOLLOW_id_decl_in_declarations1017 = frozenset([1])
    FOLLOW_CONSTANT_in_const_decl1029 = frozenset([45])
    FOLLOW_ID_in_const_decl1031 = frozenset([52])
    FOLLOW_INT_in_const_decl1033 = frozenset([1])
    FOLLOW_INTID_in_int_decl1055 = frozenset([75])
    FOLLOW_range_in_int_decl1057 = frozenset([45])
    FOLLOW_ID_in_int_decl1059 = frozenset([40, 80])
    FOLLOW_EQUALSIGN_in_int_decl1062 = frozenset([52])
    FOLLOW_INT_in_int_decl1064 = frozenset([40, 80])
    FOLLOW_SEMICOLON_in_int_decl1068 = frozenset([1])
    FOLLOW_BOOLID_in_bool_decl1096 = frozenset([45])
    FOLLOW_ID_in_bool_decl1098 = frozenset([40, 80])
    FOLLOW_EQUALSIGN_in_bool_decl1101 = frozenset([13])
    FOLLOW_BOOL_in_bool_decl1103 = frozenset([40, 80])
    FOLLOW_SEMICOLON_in_bool_decl1107 = frozenset([1])
    FOLLOW_STATE_in_state_decl1134 = frozenset([45])
    FOLLOW_ID_in_state_decl1136 = frozenset([80])
    FOLLOW_SEMICOLON_in_state_decl1138 = frozenset([1])
    FOLLOW_DATA_in_data_decl1157 = frozenset([45])
    FOLLOW_ID_in_data_decl1159 = frozenset([80])
    FOLLOW_SEMICOLON_in_data_decl1161 = frozenset([1])
    FOLLOW_set_decl_in_id_decl1180 = frozenset([71, 82])
    FOLLOW_NID_in_id_decl1183 = frozenset([45])
    FOLLOW_ID_in_id_decl1185 = frozenset([80])
    FOLLOW_SEMICOLON_in_id_decl1187 = frozenset([1])
    FOLLOW_SET_in_set_decl1209 = frozenset([75])
    FOLLOW_OEBRACE_in_set_decl1211 = frozenset([45, 52])
    FOLLOW_val_range_in_set_decl1213 = frozenset([22])
    FOLLOW_CEBRACE_in_set_decl1215 = frozenset([1])
    FOLLOW_SET_in_objset_decl1234 = frozenset([75])
    FOLLOW_OEBRACE_in_objset_decl1236 = frozenset([45, 52])
    FOLLOW_val_range_in_objset_decl1238 = frozenset([22])
    FOLLOW_CEBRACE_in_objset_decl1240 = frozenset([1])
    FOLLOW_OEBRACE_in_range1264 = frozenset([45, 52])
    FOLLOW_val_range_in_range1266 = frozenset([33])
    FOLLOW_DOT_in_range1268 = frozenset([33])
    FOLLOW_DOT_in_range1270 = frozenset([45, 52])
    FOLLOW_val_range_in_range1272 = frozenset([22])
    FOLLOW_CEBRACE_in_range1274 = frozenset([1])
    FOLLOW_ARRAY_in_array_decl1323 = frozenset([75])
    FOLLOW_range_in_array_decl1325 = frozenset([1])
    FOLLOW_FIFO_in_fifo_decl1335 = frozenset([75])
    FOLLOW_range_in_fifo_decl1337 = frozenset([1])
    FOLLOW_network_block_in_init_hw1347 = frozenset([1])
    FOLLOW_machines_in_init_hw1351 = frozenset([1])
    FOLLOW_message_block_in_init_hw1355 = frozenset([1])
    FOLLOW_object_expr_in_object_block1366 = frozenset([80])
    FOLLOW_SEMICOLON_in_object_block1368 = frozenset([1])
    FOLLOW_object_id_in_object_expr1383 = frozenset([1])
    FOLLOW_object_func_in_object_expr1387 = frozenset([1])
    FOLLOW_ID_in_object_id1398 = frozenset([1])
    FOLLOW_ID_in_object_func1415 = frozenset([33])
    FOLLOW_DOT_in_object_func1417 = frozenset([45, 71])
    FOLLOW_object_idres_in_object_func1419 = frozenset([1, 73])
    FOLLOW_OBRACE_in_object_func1422 = frozenset([20, 23, 45])
    FOLLOW_object_expr_in_object_func1424 = frozenset([20, 23, 45])
    FOLLOW_COMMA_in_object_func1428 = frozenset([45])
    FOLLOW_object_expr_in_object_func1430 = frozenset([20, 23])
    FOLLOW_CBRACE_in_object_func1434 = frozenset([1, 73])
    FOLLOW_cache_block_in_machines1503 = frozenset([1])
    FOLLOW_dir_block_in_machines1507 = frozenset([1])
    FOLLOW_mem_block_in_machines1511 = frozenset([1])
    FOLLOW_CACHE_in_cache_block1526 = frozenset([74])
    FOLLOW_OCBRACE_in_cache_block1528 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_declarations_in_cache_block1530 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_CCBRACE_in_cache_block1533 = frozenset([45, 82])
    FOLLOW_objset_decl_in_cache_block1535 = frozenset([45, 82])
    FOLLOW_ID_in_cache_block1538 = frozenset([80])
    FOLLOW_SEMICOLON_in_cache_block1540 = frozenset([1])
    FOLLOW_DIR_in_dir_block1581 = frozenset([74])
    FOLLOW_OCBRACE_in_dir_block1583 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_declarations_in_dir_block1585 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_CCBRACE_in_dir_block1588 = frozenset([45, 82])
    FOLLOW_objset_decl_in_dir_block1590 = frozenset([45, 82])
    FOLLOW_ID_in_dir_block1593 = frozenset([80])
    FOLLOW_SEMICOLON_in_dir_block1595 = frozenset([1])
    FOLLOW_MEM_in_mem_block1636 = frozenset([74])
    FOLLOW_OCBRACE_in_mem_block1638 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_declarations_in_mem_block1640 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_CCBRACE_in_mem_block1643 = frozenset([45, 82])
    FOLLOW_objset_decl_in_mem_block1645 = frozenset([45, 82])
    FOLLOW_ID_in_mem_block1648 = frozenset([80])
    FOLLOW_SEMICOLON_in_mem_block1650 = frozenset([1])
    FOLLOW_NETWORK_in_network_block1694 = frozenset([74])
    FOLLOW_OCBRACE_in_network_block1696 = frozenset([21, 102, 104])
    FOLLOW_network_element_in_network_block1698 = frozenset([21, 102, 104])
    FOLLOW_CCBRACE_in_network_block1701 = frozenset([80])
    FOLLOW_SEMICOLON_in_network_block1703 = frozenset([1])
    FOLLOW_element_type_in_network_element1746 = frozenset([45])
    FOLLOW_ID_in_network_element1748 = frozenset([80])
    FOLLOW_SEMICOLON_in_network_element1750 = frozenset([1])
    FOLLOW_ID_in_network_send1771 = frozenset([33])
    FOLLOW_DOT_in_network_send1773 = frozenset([103, 112])
    FOLLOW_send_function_in_network_send1775 = frozenset([73])
    FOLLOW_OBRACE_in_network_send1777 = frozenset([45])
    FOLLOW_ID_in_network_send1779 = frozenset([20])
    FOLLOW_CBRACE_in_network_send1781 = frozenset([80])
    FOLLOW_SEMICOLON_in_network_send1783 = frozenset([1])
    FOLLOW_ID_in_network_bcast1803 = frozenset([33])
    FOLLOW_DOT_in_network_bcast1805 = frozenset([99, 106])
    FOLLOW_bcast_function_in_network_bcast1807 = frozenset([73])
    FOLLOW_OBRACE_in_network_bcast1809 = frozenset([45])
    FOLLOW_ID_in_network_bcast1811 = frozenset([20])
    FOLLOW_CBRACE_in_network_bcast1813 = frozenset([80])
    FOLLOW_SEMICOLON_in_network_bcast1815 = frozenset([1])
    FOLLOW_ID_in_network_mcast1835 = frozenset([33])
    FOLLOW_DOT_in_network_mcast1837 = frozenset([100, 111])
    FOLLOW_mcast_function_in_network_mcast1839 = frozenset([73])
    FOLLOW_OBRACE_in_network_mcast1841 = frozenset([45])
    FOLLOW_ID_in_network_mcast1843 = frozenset([23])
    FOLLOW_COMMA_in_network_mcast1845 = frozenset([45])
    FOLLOW_ID_in_network_mcast1847 = frozenset([20])
    FOLLOW_CBRACE_in_network_mcast1849 = frozenset([80])
    FOLLOW_SEMICOLON_in_network_mcast1851 = frozenset([1])
    FOLLOW_MSG_in_message_block1881 = frozenset([45])
    FOLLOW_ID_in_message_block1883 = frozenset([74])
    FOLLOW_OCBRACE_in_message_block1885 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_declarations_in_message_block1887 = frozenset([14, 21, 28, 53, 71, 82, 87])
    FOLLOW_CCBRACE_in_message_block1890 = frozenset([80])
    FOLLOW_SEMICOLON_in_message_block1892 = frozenset([1])
    FOLLOW_ID_in_message_constr1914 = frozenset([73])
    FOLLOW_OBRACE_in_message_constr1916 = frozenset([13, 20, 23, 45, 52, 71])
    FOLLOW_message_expr_in_message_constr1918 = frozenset([13, 20, 23, 45, 52, 71])
    FOLLOW_COMMA_in_message_constr1922 = frozenset([13, 45, 52, 71])
    FOLLOW_message_expr_in_message_constr1924 = frozenset([20, 23])
    FOLLOW_CBRACE_in_message_constr1928 = frozenset([1])
    FOLLOW_object_expr_in_message_expr1950 = frozenset([1])
    FOLLOW_set_func_in_message_expr1954 = frozenset([1])
    FOLLOW_INT_in_message_expr1958 = frozenset([1])
    FOLLOW_BOOL_in_message_expr1962 = frozenset([1])
    FOLLOW_NID_in_message_expr1966 = frozenset([1])
    FOLLOW_set_func_in_set_block1984 = frozenset([80])
    FOLLOW_SEMICOLON_in_set_block1986 = frozenset([1])
    FOLLOW_ID_in_set_func2001 = frozenset([33])
    FOLLOW_DOT_in_set_func2003 = frozenset([105, 107, 108, 109, 110])
    FOLLOW_set_function_types_in_set_func2005 = frozenset([73])
    FOLLOW_OBRACE_in_set_func2007 = frozenset([20, 45])
    FOLLOW_set_nest_in_set_func2009 = frozenset([20, 45])
    FOLLOW_CBRACE_in_set_func2012 = frozenset([1])
    FOLLOW_set_func_in_set_nest2050 = frozenset([1])
    FOLLOW_object_expr_in_set_nest2054 = frozenset([1])
    FOLLOW_mod_state_func_in_mod_state_block2072 = frozenset([80])
    FOLLOW_SEMICOLON_in_mod_state_block2074 = frozenset([1])
    FOLLOW_modify_state_function_in_mod_state_func2088 = frozenset([73])
    FOLLOW_OBRACE_in_mod_state_func2090 = frozenset([45])
    FOLLOW_ID_in_mod_state_func2092 = frozenset([23])
    FOLLOW_COMMA_in_mod_state_func2094 = frozenset([45])
    FOLLOW_ID_in_mod_state_func2096 = frozenset([20])
    FOLLOW_CBRACE_in_mod_state_func2098 = frozenset([1])
    FOLLOW_ARCH_in_arch_block2118 = frozenset([45])
    FOLLOW_ID_in_arch_block2120 = frozenset([74])
    FOLLOW_OCBRACE_in_arch_block2122 = frozenset([21, 77, 85])
    FOLLOW_arch_body_in_arch_block2124 = frozenset([21])
    FOLLOW_CCBRACE_in_arch_block2126 = frozenset([1])
    FOLLOW_stable_def_in_arch_body2148 = frozenset([1, 77, 85])
    FOLLOW_process_block_in_arch_body2152 = frozenset([1, 77, 85])
    FOLLOW_STABLE_in_stable_def2162 = frozenset([74])
    FOLLOW_OCBRACE_in_stable_def2164 = frozenset([45])
    FOLLOW_ID_in_stable_def2166 = frozenset([21, 23])
    FOLLOW_COMMA_in_stable_def2169 = frozenset([45])
    FOLLOW_ID_in_stable_def2171 = frozenset([21, 23])
    FOLLOW_CCBRACE_in_stable_def2175 = frozenset([1])
    FOLLOW_PROC_in_process_block2194 = frozenset([73])
    FOLLOW_process_trans_in_process_block2196 = frozenset([74])
    FOLLOW_OCBRACE_in_process_block2198 = frozenset([10, 21, 45, 47, 87, 101])
    FOLLOW_process_expr_in_process_block2200 = frozenset([10, 21, 45, 47, 87, 101])
    FOLLOW_CCBRACE_in_process_block2203 = frozenset([1])
    FOLLOW_OBRACE_in_process_trans2229 = frozenset([45])
    FOLLOW_ID_in_process_trans2231 = frozenset([23])
    FOLLOW_COMMA_in_process_trans2233 = frozenset([4, 41, 45])
    FOLLOW_process_events_in_process_trans2235 = frozenset([20, 23])
    FOLLOW_process_finalstate_in_process_trans2237 = frozenset([20, 23])
    FOLLOW_CBRACE_in_process_trans2240 = frozenset([1])
    FOLLOW_COMMA_in_process_finalstate2263 = frozenset([45, 87])
    FOLLOW_process_finalident_in_process_finalstate2265 = frozenset([1])
    FOLLOW_expressions_in_process_expr2318 = frozenset([1])
    FOLLOW_network_send_in_process_expr2322 = frozenset([1])
    FOLLOW_network_mcast_in_process_expr2326 = frozenset([1])
    FOLLOW_network_bcast_in_process_expr2330 = frozenset([1])
    FOLLOW_transaction_in_process_expr2333 = frozenset([1])
    FOLLOW_AWAIT_in_transaction2343 = frozenset([74])
    FOLLOW_OCBRACE_in_transaction2345 = frozenset([21, 89])
    FOLLOW_trans_in_transaction2347 = frozenset([21, 89])
    FOLLOW_CCBRACE_in_transaction2350 = frozenset([1])
    FOLLOW_WHEN_in_trans2370 = frozenset([45])
    FOLLOW_ID_in_trans2372 = frozenset([30])
    FOLLOW_DDOT_in_trans2374 = frozenset([1, 10, 16, 45, 47, 69, 87, 101])
    FOLLOW_trans_body_in_trans2376 = frozenset([1, 10, 16, 45, 47, 69, 87, 101])
    FOLLOW_expressions_in_trans_body2409 = frozenset([1])
    FOLLOW_next_trans_in_trans_body2413 = frozenset([1])
    FOLLOW_next_break_in_trans_body2417 = frozenset([1])
    FOLLOW_transaction_in_trans_body2421 = frozenset([1])
    FOLLOW_network_send_in_trans_body2425 = frozenset([1])
    FOLLOW_network_mcast_in_trans_body2429 = frozenset([1])
    FOLLOW_network_bcast_in_trans_body2433 = frozenset([1])
    FOLLOW_NEXT_in_next_trans2451 = frozenset([74])
    FOLLOW_OCBRACE_in_next_trans2453 = frozenset([21, 89])
    FOLLOW_trans_in_next_trans2455 = frozenset([21, 89])
    FOLLOW_CCBRACE_in_next_trans2458 = frozenset([1])
    FOLLOW_BREAK_in_next_break2475 = frozenset([80])
    FOLLOW_SEMICOLON_in_next_break2477 = frozenset([1])
    FOLLOW_assignment_in_expressions2493 = frozenset([1])
    FOLLOW_conditional_in_expressions2497 = frozenset([1])
    FOLLOW_object_block_in_expressions2501 = frozenset([1])
    FOLLOW_set_block_in_expressions2505 = frozenset([1])
    FOLLOW_mod_state_block_in_expressions2509 = frozenset([1])
    FOLLOW_process_finalident_in_assignment2516 = frozenset([40])
    FOLLOW_EQUALSIGN_in_assignment2518 = frozenset([13, 45, 52])
    FOLLOW_assign_types_in_assignment2520 = frozenset([80])
    FOLLOW_SEMICOLON_in_assignment2522 = frozenset([1])
    FOLLOW_object_expr_in_assign_types2544 = frozenset([1])
    FOLLOW_message_constr_in_assign_types2548 = frozenset([1])
    FOLLOW_math_op_in_assign_types2552 = frozenset([1])
    FOLLOW_set_func_in_assign_types2556 = frozenset([1])
    FOLLOW_INT_in_assign_types2560 = frozenset([1])
    FOLLOW_BOOL_in_assign_types2564 = frozenset([1])
    FOLLOW_val_range_in_math_op2575 = frozenset([60, 76])
    FOLLOW_set_in_math_op2577 = frozenset([45, 52])
    FOLLOW_val_range_in_math_op2585 = frozenset([1])
    FOLLOW_if_stmt_in_conditional2594 = frozenset([1])
    FOLLOW_ifnot_stmt_in_conditional2598 = frozenset([1])
    FOLLOW_IF_in_if_stmt2617 = frozenset([13, 45, 52, 71, 73])
    FOLLOW_cond_comb_in_if_stmt2619 = frozenset([74])
    FOLLOW_OCBRACE_in_if_stmt2621 = frozenset([10, 16, 21, 45, 47, 87, 101])
    FOLLOW_if_expression_in_if_stmt2623 = frozenset([21])
    FOLLOW_CCBRACE_in_if_stmt2625 = frozenset([1, 35])
    FOLLOW_ELSE_in_if_stmt2632 = frozenset([74])
    FOLLOW_OCBRACE_in_if_stmt2636 = frozenset([10, 16, 21, 45, 47, 87, 101])
    FOLLOW_else_expression_in_if_stmt2638 = frozenset([21])
    FOLLOW_CCBRACE_in_if_stmt2640 = frozenset([1, 35])
    FOLLOW_IF_in_ifnot_stmt2746 = frozenset([66])
    FOLLOW_NEG_in_ifnot_stmt2748 = frozenset([13, 45, 52, 71, 73])
    FOLLOW_cond_comb_in_ifnot_stmt2750 = frozenset([74])
    FOLLOW_OCBRACE_in_ifnot_stmt2752 = frozenset([10, 16, 21, 45, 47, 87, 101])
    FOLLOW_if_expression_in_ifnot_stmt2754 = frozenset([21])
    FOLLOW_CCBRACE_in_ifnot_stmt2756 = frozenset([1, 35])
    FOLLOW_ELSE_in_ifnot_stmt2763 = frozenset([74])
    FOLLOW_OCBRACE_in_ifnot_stmt2767 = frozenset([10, 16, 21, 45, 47, 87, 101])
    FOLLOW_else_expression_in_ifnot_stmt2769 = frozenset([21])
    FOLLOW_CCBRACE_in_ifnot_stmt2771 = frozenset([1, 35])
    FOLLOW_exprwbreak_in_if_expression2872 = frozenset([1, 10, 16, 45, 47, 87, 101])
    FOLLOW_exprwbreak_in_else_expression2887 = frozenset([1, 10, 16, 45, 47, 87, 101])
    FOLLOW_expressions_in_exprwbreak2902 = frozenset([1])
    FOLLOW_network_send_in_exprwbreak2906 = frozenset([1])
    FOLLOW_network_mcast_in_exprwbreak2910 = frozenset([1])
    FOLLOW_network_bcast_in_exprwbreak2914 = frozenset([1])
    FOLLOW_transaction_in_exprwbreak2918 = frozenset([1])
    FOLLOW_next_break_in_exprwbreak2922 = frozenset([1])
    FOLLOW_cond_rel_in_cond_comb2936 = frozenset([1, 93, 113])
    FOLLOW_combinatorial_operator_in_cond_comb2939 = frozenset([13, 45, 52, 71, 73])
    FOLLOW_cond_rel_in_cond_comb2941 = frozenset([1, 93, 113])
    FOLLOW_OBRACE_in_cond_rel2958 = frozenset([13, 45, 52, 71, 73])
    FOLLOW_cond_sel_in_cond_rel2961 = frozenset([1, 20])
    FOLLOW_CBRACE_in_cond_rel2963 = frozenset([1, 20])
    FOLLOW_cond_types_in_cond_sel2987 = frozenset([1, 92, 94, 95, 96, 97, 98])
    FOLLOW_relational_operator_in_cond_sel2990 = frozenset([13, 45, 52, 71])
    FOLLOW_cond_types_in_cond_sel2992 = frozenset([1, 92, 94, 95, 96, 97, 98])
    FOLLOW_object_expr_in_cond_types3013 = frozenset([1])
    FOLLOW_set_func_in_cond_types3017 = frozenset([1])
    FOLLOW_INT_in_cond_types3021 = frozenset([1])
    FOLLOW_BOOL_in_cond_types3025 = frozenset([1])
    FOLLOW_NID_in_cond_types3029 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ProtoCCLexer", ProtoCCParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
