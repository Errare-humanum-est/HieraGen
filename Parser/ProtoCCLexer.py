# $ANTLR 3.5.2 /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g 2020-02-28 17:10:15

import sys
from antlr3 import *



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

class ProtoCCLexer(Lexer):

    grammarFileName = "/home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "ARCH"
    def mARCH(self, ):
        try:
            _type = ARCH
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:7:6: ( 'Architecture' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:7:8: 'Architecture'
            pass 
            self.match("Architecture")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARCH"



    # $ANTLR start "ARRAY"
    def mARRAY(self, ):
        try:
            _type = ARRAY
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:8:7: ( 'array' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:8:9: 'array'
            pass 
            self.match("array")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARRAY"



    # $ANTLR start "AWAIT"
    def mAWAIT(self, ):
        try:
            _type = AWAIT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:9:7: ( 'await' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:9:9: 'await'
            pass 
            self.match("await")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AWAIT"



    # $ANTLR start "BOOLID"
    def mBOOLID(self, ):
        try:
            _type = BOOLID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:10:8: ( 'bool' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:10:10: 'bool'
            pass 
            self.match("bool")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BOOLID"



    # $ANTLR start "BREAK"
    def mBREAK(self, ):
        try:
            _type = BREAK
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:11:7: ( 'break' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:11:9: 'break'
            pass 
            self.match("break")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BREAK"



    # $ANTLR start "CACHE"
    def mCACHE(self, ):
        try:
            _type = CACHE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:12:7: ( 'Cache' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:12:9: 'Cache'
            pass 
            self.match("Cache")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CACHE"



    # $ANTLR start "CBRACE"
    def mCBRACE(self, ):
        try:
            _type = CBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:13:8: ( ')' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:13:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CBRACE"



    # $ANTLR start "CCBRACE"
    def mCCBRACE(self, ):
        try:
            _type = CCBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:14:9: ( '}' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:14:11: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CCBRACE"



    # $ANTLR start "CEBRACE"
    def mCEBRACE(self, ):
        try:
            _type = CEBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:15:9: ( ']' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:15:11: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CEBRACE"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:16:7: ( ',' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:16:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "CONSTANT"
    def mCONSTANT(self, ):
        try:
            _type = CONSTANT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:17:10: ( '#' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:17:12: '#'
            pass 
            self.match(35)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONSTANT"



    # $ANTLR start "DATA"
    def mDATA(self, ):
        try:
            _type = DATA
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:18:6: ( 'Data' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:18:8: 'Data'
            pass 
            self.match("Data")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DATA"



    # $ANTLR start "DDOT"
    def mDDOT(self, ):
        try:
            _type = DDOT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:19:6: ( ':' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:19:8: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DDOT"



    # $ANTLR start "DIR"
    def mDIR(self, ):
        try:
            _type = DIR
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:20:5: ( 'Directory' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:20:7: 'Directory'
            pass 
            self.match("Directory")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIR"



    # $ANTLR start "DOT"
    def mDOT(self, ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:21:5: ( '.' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:21:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "ELSE"
    def mELSE(self, ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:22:6: ( 'else' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:22:8: 'else'
            pass 
            self.match("else")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "EQUALSIGN"
    def mEQUALSIGN(self, ):
        try:
            _type = EQUALSIGN
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:23:11: ( '=' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:23:13: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQUALSIGN"



    # $ANTLR start "FIFO"
    def mFIFO(self, ):
        try:
            _type = FIFO
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:24:6: ( 'FIFO' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:24:8: 'FIFO'
            pass 
            self.match("FIFO")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FIFO"



    # $ANTLR start "IF"
    def mIF(self, ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:25:4: ( 'if' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:25:6: 'if'
            pass 
            self.match("if")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IF"



    # $ANTLR start "INTID"
    def mINTID(self, ):
        try:
            _type = INTID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:26:7: ( 'int' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:26:9: 'int'
            pass 
            self.match("int")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INTID"



    # $ANTLR start "MEM"
    def mMEM(self, ):
        try:
            _type = MEM
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:27:5: ( 'Memory' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:27:7: 'Memory'
            pass 
            self.match("Memory")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MEM"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):
        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:28:7: ( '-' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:28:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MSG"
    def mMSG(self, ):
        try:
            _type = MSG
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:29:5: ( 'Message' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:29:7: 'Message'
            pass 
            self.match("Message")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MSG"



    # $ANTLR start "NEG"
    def mNEG(self, ):
        try:
            _type = NEG
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:30:5: ( '!' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:30:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEG"



    # $ANTLR start "NETWORK"
    def mNETWORK(self, ):
        try:
            _type = NETWORK
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:31:9: ( 'Network' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:31:11: 'Network'
            pass 
            self.match("Network")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NETWORK"



    # $ANTLR start "NEXT"
    def mNEXT(self, ):
        try:
            _type = NEXT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:32:6: ( 'next' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:32:8: 'next'
            pass 
            self.match("next")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEXT"



    # $ANTLR start "NID"
    def mNID(self, ):
        try:
            _type = NID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:33:5: ( 'ID' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:33:7: 'ID'
            pass 
            self.match("ID")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NID"



    # $ANTLR start "OBRACE"
    def mOBRACE(self, ):
        try:
            _type = OBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:34:8: ( '(' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:34:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OBRACE"



    # $ANTLR start "OCBRACE"
    def mOCBRACE(self, ):
        try:
            _type = OCBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:35:9: ( '{' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:35:11: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OCBRACE"



    # $ANTLR start "OEBRACE"
    def mOEBRACE(self, ):
        try:
            _type = OEBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:36:9: ( '[' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:36:11: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OEBRACE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:37:6: ( '+' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:37:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "PROC"
    def mPROC(self, ):
        try:
            _type = PROC
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:38:6: ( 'Process' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:38:8: 'Process'
            pass 
            self.match("Process")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROC"



    # $ANTLR start "SEMICOLON"
    def mSEMICOLON(self, ):
        try:
            _type = SEMICOLON
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:39:11: ( ';' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:39:13: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMICOLON"



    # $ANTLR start "SET"
    def mSET(self, ):
        try:
            _type = SET
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:40:5: ( 'set' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:40:7: 'set'
            pass 
            self.match("set")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SET"



    # $ANTLR start "STABLE"
    def mSTABLE(self, ):
        try:
            _type = STABLE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:41:8: ( 'Stable' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:41:10: 'Stable'
            pass 
            self.match("Stable")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STABLE"



    # $ANTLR start "STATE"
    def mSTATE(self, ):
        try:
            _type = STATE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:42:7: ( 'State' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:42:9: 'State'
            pass 
            self.match("State")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STATE"



    # $ANTLR start "WHEN"
    def mWHEN(self, ):
        try:
            _type = WHEN
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:43:6: ( 'when' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:43:8: 'when'
            pass 
            self.match("when")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHEN"



    # $ANTLR start "T__92"
    def mT__92(self, ):
        try:
            _type = T__92
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:44:7: ( '!=' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:44:9: '!='
            pass 
            self.match("!=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__92"



    # $ANTLR start "T__93"
    def mT__93(self, ):
        try:
            _type = T__93
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:45:7: ( '&' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:45:9: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__93"



    # $ANTLR start "T__94"
    def mT__94(self, ):
        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:46:7: ( '<' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:46:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):
        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:47:7: ( '<=' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:47:9: '<='
            pass 
            self.match("<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):
        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:48:7: ( '==' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:48:9: '=='
            pass 
            self.match("==")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):
        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:49:7: ( '>' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:49:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):
        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:50:7: ( '>=' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:50:9: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):
        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:51:7: ( 'Bcast' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:51:9: 'Bcast'
            pass 
            self.match("Bcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):
        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:52:8: ( 'Mcast' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:52:10: 'Mcast'
            pass 
            self.match("Mcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__100"



    # $ANTLR start "T__101"
    def mT__101(self, ):
        try:
            _type = T__101
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:53:8: ( 'ModifyStates' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:53:10: 'ModifyStates'
            pass 
            self.match("ModifyStates")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__101"



    # $ANTLR start "T__102"
    def mT__102(self, ):
        try:
            _type = T__102
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:54:8: ( 'Ordered' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:54:10: 'Ordered'
            pass 
            self.match("Ordered")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__102"



    # $ANTLR start "T__103"
    def mT__103(self, ):
        try:
            _type = T__103
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:55:8: ( 'Send' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:55:10: 'Send'
            pass 
            self.match("Send")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__103"



    # $ANTLR start "T__104"
    def mT__104(self, ):
        try:
            _type = T__104
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:56:8: ( 'Unordered' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:56:10: 'Unordered'
            pass 
            self.match("Unordered")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__104"



    # $ANTLR start "T__105"
    def mT__105(self, ):
        try:
            _type = T__105
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:57:8: ( 'add' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:57:10: 'add'
            pass 
            self.match("add")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__105"



    # $ANTLR start "T__106"
    def mT__106(self, ):
        try:
            _type = T__106
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:58:8: ( 'bcast' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:58:10: 'bcast'
            pass 
            self.match("bcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__106"



    # $ANTLR start "T__107"
    def mT__107(self, ):
        try:
            _type = T__107
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:59:8: ( 'clear' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:59:10: 'clear'
            pass 
            self.match("clear")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__107"



    # $ANTLR start "T__108"
    def mT__108(self, ):
        try:
            _type = T__108
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:60:8: ( 'contains' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:60:10: 'contains'
            pass 
            self.match("contains")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__108"



    # $ANTLR start "T__109"
    def mT__109(self, ):
        try:
            _type = T__109
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:61:8: ( 'count' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:61:10: 'count'
            pass 
            self.match("count")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__109"



    # $ANTLR start "T__110"
    def mT__110(self, ):
        try:
            _type = T__110
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:62:8: ( 'del' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:62:10: 'del'
            pass 
            self.match("del")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__110"



    # $ANTLR start "T__111"
    def mT__111(self, ):
        try:
            _type = T__111
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:63:8: ( 'mcast' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:63:10: 'mcast'
            pass 
            self.match("mcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__111"



    # $ANTLR start "T__112"
    def mT__112(self, ):
        try:
            _type = T__112
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:64:8: ( 'send' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:64:10: 'send'
            pass 
            self.match("send")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__112"



    # $ANTLR start "T__113"
    def mT__113(self, ):
        try:
            _type = T__113
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:65:8: ( '|' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:65:10: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__113"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:158:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:158:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if self.input.LA(1) in {9, 10, 13, 32}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:166:5: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:166:9: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")


            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:166:14: ( options {greedy=false; } : . )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 42) :
                    LA1_1 = self.input.LA(2)

                    if (LA1_1 == 47) :
                        alt1 = 2
                    elif ((0 <= LA1_1 <= 46) or (48 <= LA1_1 <= 65535) or LA1_1 in {}) :
                        alt1 = 1


                elif ((0 <= LA1_0 <= 41) or (43 <= LA1_0 <= 65535) or LA1_0 in {}) :
                    alt1 = 1


                if alt1 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:166:42: .
                    pass 
                    self.matchAny()


                else:
                    break #loop1


            self.match("*/")


            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):
        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:170:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:170:7: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")


            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:170:12: (~ ( '\\n' | '\\r' ) )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((0 <= LA2_0 <= 9) or (14 <= LA2_0 <= 65535) or LA2_0 in {11, 12}) :
                    alt2 = 1


                if alt2 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (14 <= self.input.LA(1) <= 65535) or self.input.LA(1) in {11, 12}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2


            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:170:26: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:170:26: '\\r'
                pass 
                self.match(13)




            self.match(10)

            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "BOOL"
    def mBOOL(self, ):
        try:
            _type = BOOL
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:175:5: ( 'true' | 'false' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 116) :
                alt4 = 1
            elif (LA4_0 == 102) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:175:9: 'true'
                pass 
                self.match("true")



            elif alt4 == 2:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:175:18: 'false'
                pass 
                self.match("false")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BOOL"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:176:5: ( ( '0' .. '9' )+ )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:176:7: ( '0' .. '9' )+
            pass 
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:176:7: ( '0' .. '9' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or LA5_0 in {}) :
                    alt5 = 1


                if alt5 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "ACCESS"
    def mACCESS(self, ):
        try:
            _type = ACCESS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:178:7: ( 'load' | 'store' )
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 108) :
                alt6 = 1
            elif (LA6_0 == 115) :
                alt6 = 2
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae


            if alt6 == 1:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:178:9: 'load'
                pass 
                self.match("load")



            elif alt6 == 2:
                # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:178:18: 'store'
                pass 
                self.match("store")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ACCESS"



    # $ANTLR start "EVICT"
    def mEVICT(self, ):
        try:
            _type = EVICT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:179:6: ( 'evict' )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:179:8: 'evict'
            pass 
            self.match("evict")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EVICT"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:181:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:181:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:181:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((48 <= LA7_0 <= 57) or (65 <= LA7_0 <= 90) or (97 <= LA7_0 <= 122) or LA7_0 in {95}) :
                    alt7 = 1


                if alt7 == 1:
                    # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop7




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    def mTokens(self):
        # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:8: ( ARCH | ARRAY | AWAIT | BOOLID | BREAK | CACHE | CBRACE | CCBRACE | CEBRACE | COMMA | CONSTANT | DATA | DDOT | DIR | DOT | ELSE | EQUALSIGN | FIFO | IF | INTID | MEM | MINUS | MSG | NEG | NETWORK | NEXT | NID | OBRACE | OCBRACE | OEBRACE | PLUS | PROC | SEMICOLON | SET | STABLE | STATE | WHEN | T__92 | T__93 | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | T__104 | T__105 | T__106 | T__107 | T__108 | T__109 | T__110 | T__111 | T__112 | T__113 | WS | COMMENT | LINE_COMMENT | BOOL | INT | ACCESS | EVICT | ID )
        alt8 = 67
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:10: ARCH
            pass 
            self.mARCH()



        elif alt8 == 2:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:15: ARRAY
            pass 
            self.mARRAY()



        elif alt8 == 3:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:21: AWAIT
            pass 
            self.mAWAIT()



        elif alt8 == 4:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:27: BOOLID
            pass 
            self.mBOOLID()



        elif alt8 == 5:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:34: BREAK
            pass 
            self.mBREAK()



        elif alt8 == 6:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:40: CACHE
            pass 
            self.mCACHE()



        elif alt8 == 7:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:46: CBRACE
            pass 
            self.mCBRACE()



        elif alt8 == 8:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:53: CCBRACE
            pass 
            self.mCCBRACE()



        elif alt8 == 9:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:61: CEBRACE
            pass 
            self.mCEBRACE()



        elif alt8 == 10:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:69: COMMA
            pass 
            self.mCOMMA()



        elif alt8 == 11:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:75: CONSTANT
            pass 
            self.mCONSTANT()



        elif alt8 == 12:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:84: DATA
            pass 
            self.mDATA()



        elif alt8 == 13:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:89: DDOT
            pass 
            self.mDDOT()



        elif alt8 == 14:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:94: DIR
            pass 
            self.mDIR()



        elif alt8 == 15:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:98: DOT
            pass 
            self.mDOT()



        elif alt8 == 16:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:102: ELSE
            pass 
            self.mELSE()



        elif alt8 == 17:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:107: EQUALSIGN
            pass 
            self.mEQUALSIGN()



        elif alt8 == 18:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:117: FIFO
            pass 
            self.mFIFO()



        elif alt8 == 19:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:122: IF
            pass 
            self.mIF()



        elif alt8 == 20:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:125: INTID
            pass 
            self.mINTID()



        elif alt8 == 21:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:131: MEM
            pass 
            self.mMEM()



        elif alt8 == 22:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:135: MINUS
            pass 
            self.mMINUS()



        elif alt8 == 23:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:141: MSG
            pass 
            self.mMSG()



        elif alt8 == 24:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:145: NEG
            pass 
            self.mNEG()



        elif alt8 == 25:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:149: NETWORK
            pass 
            self.mNETWORK()



        elif alt8 == 26:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:157: NEXT
            pass 
            self.mNEXT()



        elif alt8 == 27:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:162: NID
            pass 
            self.mNID()



        elif alt8 == 28:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:166: OBRACE
            pass 
            self.mOBRACE()



        elif alt8 == 29:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:173: OCBRACE
            pass 
            self.mOCBRACE()



        elif alt8 == 30:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:181: OEBRACE
            pass 
            self.mOEBRACE()



        elif alt8 == 31:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:189: PLUS
            pass 
            self.mPLUS()



        elif alt8 == 32:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:194: PROC
            pass 
            self.mPROC()



        elif alt8 == 33:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:199: SEMICOLON
            pass 
            self.mSEMICOLON()



        elif alt8 == 34:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:209: SET
            pass 
            self.mSET()



        elif alt8 == 35:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:213: STABLE
            pass 
            self.mSTABLE()



        elif alt8 == 36:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:220: STATE
            pass 
            self.mSTATE()



        elif alt8 == 37:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:226: WHEN
            pass 
            self.mWHEN()



        elif alt8 == 38:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:231: T__92
            pass 
            self.mT__92()



        elif alt8 == 39:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:237: T__93
            pass 
            self.mT__93()



        elif alt8 == 40:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:243: T__94
            pass 
            self.mT__94()



        elif alt8 == 41:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:249: T__95
            pass 
            self.mT__95()



        elif alt8 == 42:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:255: T__96
            pass 
            self.mT__96()



        elif alt8 == 43:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:261: T__97
            pass 
            self.mT__97()



        elif alt8 == 44:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:267: T__98
            pass 
            self.mT__98()



        elif alt8 == 45:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:273: T__99
            pass 
            self.mT__99()



        elif alt8 == 46:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:279: T__100
            pass 
            self.mT__100()



        elif alt8 == 47:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:286: T__101
            pass 
            self.mT__101()



        elif alt8 == 48:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:293: T__102
            pass 
            self.mT__102()



        elif alt8 == 49:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:300: T__103
            pass 
            self.mT__103()



        elif alt8 == 50:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:307: T__104
            pass 
            self.mT__104()



        elif alt8 == 51:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:314: T__105
            pass 
            self.mT__105()



        elif alt8 == 52:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:321: T__106
            pass 
            self.mT__106()



        elif alt8 == 53:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:328: T__107
            pass 
            self.mT__107()



        elif alt8 == 54:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:335: T__108
            pass 
            self.mT__108()



        elif alt8 == 55:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:342: T__109
            pass 
            self.mT__109()



        elif alt8 == 56:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:349: T__110
            pass 
            self.mT__110()



        elif alt8 == 57:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:356: T__111
            pass 
            self.mT__111()



        elif alt8 == 58:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:363: T__112
            pass 
            self.mT__112()



        elif alt8 == 59:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:370: T__113
            pass 
            self.mT__113()



        elif alt8 == 60:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:377: WS
            pass 
            self.mWS()



        elif alt8 == 61:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:380: COMMENT
            pass 
            self.mCOMMENT()



        elif alt8 == 62:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:388: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()



        elif alt8 == 63:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:401: BOOL
            pass 
            self.mBOOL()



        elif alt8 == 64:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:406: INT
            pass 
            self.mINT()



        elif alt8 == 65:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:410: ACCESS
            pass 
            self.mACCESS()



        elif alt8 == 66:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:417: EVICT
            pass 
            self.mEVICT()



        elif alt8 == 67:
            # /home/tux/PycharmProjects/ProtoCCv2/Parser/ProtoCC.g:1:423: ID
            pass 
            self.mID()








    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        "\1\uffff\4\60\5\uffff\1\60\2\uffff\1\60\1\76\3\60\1\uffff\1\106"
        "\3\60\4\uffff\1\60\1\uffff\3\60\1\uffff\1\121\1\123\6\60\3\uffff"
        "\2\60\1\uffff\1\60\1\uffff\14\60\2\uffff\1\60\1\155\4\60\2\uffff"
        "\2\60\1\165\6\60\4\uffff\7\60\2\uffff\6\60\1\u008b\11\60\1\uffff"
        "\1\u0095\6\60\1\uffff\1\60\1\u009d\13\60\1\u00aa\7\60\1\uffff\1"
        "\u00b2\3\60\1\u00b6\1\60\1\u00b8\1\60\1\u00ba\1\uffff\5\60\1\u00c0"
        "\1\60\1\uffff\1\u00c2\3\60\1\u00c6\1\u00c7\6\60\1\uffff\1\60\1\u00cf"
        "\1\60\1\u00d1\1\60\1\u00d3\1\u00d4\1\uffff\1\u00d5\1\u00d6\1\u00d7"
        "\1\uffff\1\60\1\uffff\1\u00d9\1\uffff\2\60\1\u00dc\2\60\1\uffff"
        "\1\60\1\uffff\1\u00d1\1\60\1\u00e1\2\uffff\1\u00e2\2\60\1\u00e5"
        "\1\60\1\u00e7\1\u00e8\1\uffff\1\u00cf\1\uffff\1\60\5\uffff\1\60"
        "\1\uffff\1\u00eb\1\60\1\uffff\3\60\1\u00f0\2\uffff\2\60\1\uffff"
        "\1\60\2\uffff\2\60\1\uffff\1\u00f6\1\60\1\u00f8\1\u00f9\1\uffff"
        "\1\u00fa\4\60\1\uffff\1\60\3\uffff\1\60\1\u0101\1\60\1\u0103\1\60"
        "\1\u0105\1\uffff\1\60\1\uffff\1\60\1\uffff\2\60\1\u010a\1\u010b"
        "\2\uffff"
        )

    DFA8_eof = DFA.unpack(
        "\u010c\uffff"
        )

    DFA8_min = DFA.unpack(
        "\1\11\1\162\1\144\1\143\1\141\5\uffff\1\141\2\uffff\1\154\1\75\1"
        "\111\1\146\1\143\1\uffff\1\75\2\145\1\104\4\uffff\1\162\1\uffff"
        "\2\145\1\150\1\uffff\2\75\1\143\1\162\1\156\1\154\1\145\1\143\2"
        "\uffff\1\52\1\162\1\141\1\uffff\1\157\1\uffff\1\143\1\162\1\141"
        "\1\144\1\157\1\145\1\141\1\143\1\164\1\162\1\163\1\151\2\uffff\1"
        "\106\1\60\1\164\1\155\1\141\1\144\2\uffff\1\164\1\170\1\60\1\157"
        "\1\156\1\157\1\141\1\156\1\145\4\uffff\1\141\1\144\1\157\1\145\1"
        "\156\1\154\1\141\2\uffff\1\165\1\154\1\141\1\150\1\141\1\151\1\60"
        "\1\154\1\141\1\163\1\150\1\141\2\145\1\143\1\117\1\uffff\1\60\1"
        "\157\2\163\1\151\1\167\1\164\1\uffff\1\143\1\60\1\144\1\162\1\142"
        "\1\144\1\156\1\163\1\145\1\162\1\141\1\164\1\156\1\60\1\163\1\145"
        "\1\163\1\144\1\151\1\171\1\164\1\uffff\1\60\1\153\1\164\1\145\1"
        "\60\1\143\1\60\1\164\1\60\1\uffff\1\162\1\141\1\164\1\146\1\157"
        "\1\60\1\145\1\uffff\1\60\1\145\1\154\1\145\2\60\1\164\1\162\1\144"
        "\1\162\1\141\1\164\1\uffff\1\164\1\60\1\145\1\60\1\164\2\60\1\uffff"
        "\3\60\1\uffff\1\164\1\uffff\1\60\1\uffff\1\171\1\147\1\60\1\171"
        "\1\162\1\uffff\1\163\1\uffff\1\60\1\145\1\60\2\uffff\1\60\2\145"
        "\1\60\1\151\2\60\1\uffff\1\60\1\uffff\1\145\5\uffff\1\157\1\uffff"
        "\1\60\1\145\1\uffff\1\123\1\153\1\163\1\60\2\uffff\1\144\1\162\1"
        "\uffff\1\156\2\uffff\1\143\1\162\1\uffff\1\60\1\164\2\60\1\uffff"
        "\1\60\1\145\1\163\1\164\1\171\1\uffff\1\141\3\uffff\1\144\1\60\1"
        "\165\1\60\1\164\1\60\1\uffff\1\162\1\uffff\1\145\1\uffff\1\145\1"
        "\163\2\60\2\uffff"
        )

    DFA8_max = DFA.unpack(
        "\1\175\1\162\1\167\1\162\1\141\5\uffff\1\151\2\uffff\1\166\1\75"
        "\1\111\1\156\1\157\1\uffff\1\75\2\145\1\104\4\uffff\1\162\1\uffff"
        "\2\164\1\150\1\uffff\2\75\1\143\1\162\1\156\1\157\1\145\1\143\2"
        "\uffff\1\57\1\162\1\141\1\uffff\1\157\1\uffff\1\143\1\162\1\141"
        "\1\144\1\157\1\145\1\141\1\143\1\164\1\162\1\163\1\151\2\uffff\1"
        "\106\1\172\1\164\1\163\1\141\1\144\2\uffff\1\164\1\170\1\172\1\157"
        "\1\164\1\157\1\141\1\156\1\145\4\uffff\1\141\1\144\1\157\1\145\1"
        "\165\1\154\1\141\2\uffff\1\165\1\154\1\141\1\150\1\141\1\151\1\172"
        "\1\154\1\141\1\163\1\150\1\141\2\145\1\143\1\117\1\uffff\1\172\1"
        "\157\2\163\1\151\1\167\1\164\1\uffff\1\143\1\172\1\144\1\162\1\164"
        "\1\144\1\156\1\163\1\145\1\162\1\141\1\164\1\156\1\172\1\163\1\145"
        "\1\163\1\144\1\151\1\171\1\164\1\uffff\1\172\1\153\1\164\1\145\1"
        "\172\1\143\1\172\1\164\1\172\1\uffff\1\162\1\141\1\164\1\146\1\157"
        "\1\172\1\145\1\uffff\1\172\1\145\1\154\1\145\2\172\1\164\1\162\1"
        "\144\1\162\1\141\1\164\1\uffff\1\164\1\172\1\145\1\172\1\164\2\172"
        "\1\uffff\3\172\1\uffff\1\164\1\uffff\1\172\1\uffff\1\171\1\147\1"
        "\172\1\171\1\162\1\uffff\1\163\1\uffff\1\172\1\145\1\172\2\uffff"
        "\1\172\2\145\1\172\1\151\2\172\1\uffff\1\172\1\uffff\1\145\5\uffff"
        "\1\157\1\uffff\1\172\1\145\1\uffff\1\123\1\153\1\163\1\172\2\uffff"
        "\1\144\1\162\1\uffff\1\156\2\uffff\1\143\1\162\1\uffff\1\172\1\164"
        "\2\172\1\uffff\1\172\1\145\1\163\1\164\1\171\1\uffff\1\141\3\uffff"
        "\1\144\1\172\1\165\1\172\1\164\1\172\1\uffff\1\162\1\uffff\1\145"
        "\1\uffff\1\145\1\163\2\172\2\uffff"
        )

    DFA8_accept = DFA.unpack(
        "\5\uffff\1\7\1\10\1\11\1\12\1\13\1\uffff\1\15\1\17\5\uffff\1\26"
        "\4\uffff\1\34\1\35\1\36\1\37\1\uffff\1\41\3\uffff\1\47\10\uffff"
        "\1\73\1\74\3\uffff\1\100\1\uffff\1\103\14\uffff\1\52\1\21\6\uffff"
        "\1\46\1\30\11\uffff\1\51\1\50\1\54\1\53\7\uffff\1\75\1\76\20\uffff"
        "\1\23\7\uffff\1\33\25\uffff\1\63\11\uffff\1\24\7\uffff\1\42\14\uffff"
        "\1\70\7\uffff\1\4\3\uffff\1\14\1\uffff\1\20\1\uffff\1\22\5\uffff"
        "\1\32\1\uffff\1\72\3\uffff\1\61\1\45\7\uffff\1\77\1\uffff\1\101"
        "\1\uffff\1\2\1\3\1\5\1\64\1\6\1\uffff\1\102\2\uffff\1\56\4\uffff"
        "\1\44\1\55\2\uffff\1\65\1\uffff\1\67\1\71\2\uffff\1\25\4\uffff\1"
        "\43\5\uffff\1\27\1\uffff\1\31\1\40\1\60\6\uffff\1\66\1\uffff\1\16"
        "\1\uffff\1\62\4\uffff\1\1\1\57"
        )

    DFA8_special = DFA.unpack(
        "\u010c\uffff"
        )


    DFA8_transition = [
        DFA.unpack("\2\52\2\uffff\1\52\22\uffff\1\52\1\23\1\uffff\1\11\2"
        "\uffff\1\40\1\uffff\1\27\1\5\1\uffff\1\32\1\10\1\22\1\14\1\53\12"
        "\56\1\13\1\34\1\41\1\16\1\42\2\uffff\1\1\1\43\1\4\1\12\1\60\1\17"
        "\2\60\1\26\3\60\1\21\1\24\1\44\1\33\2\60\1\36\1\60\1\45\5\60\1\31"
        "\1\uffff\1\7\1\uffff\1\60\1\uffff\1\2\1\3\1\46\1\47\1\15\1\55\2"
        "\60\1\20\2\60\1\57\1\50\1\25\4\60\1\35\1\54\2\60\1\37\3\60\1\30"
        "\1\51\1\6"),
        DFA.unpack("\1\61"),
        DFA.unpack("\1\64\15\uffff\1\62\4\uffff\1\63"),
        DFA.unpack("\1\67\13\uffff\1\65\2\uffff\1\66"),
        DFA.unpack("\1\70"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\71\7\uffff\1\72"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\73\11\uffff\1\74"),
        DFA.unpack("\1\75"),
        DFA.unpack("\1\77"),
        DFA.unpack("\1\100\7\uffff\1\101"),
        DFA.unpack("\1\103\1\uffff\1\102\11\uffff\1\104"),
        DFA.unpack(""),
        DFA.unpack("\1\105"),
        DFA.unpack("\1\107"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\112"),
        DFA.unpack(""),
        DFA.unpack("\1\113\16\uffff\1\114"),
        DFA.unpack("\1\116\16\uffff\1\115"),
        DFA.unpack("\1\117"),
        DFA.unpack(""),
        DFA.unpack("\1\120"),
        DFA.unpack("\1\122"),
        DFA.unpack("\1\124"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\127\2\uffff\1\130"),
        DFA.unpack("\1\131"),
        DFA.unpack("\1\132"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\133\4\uffff\1\134"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack(""),
        DFA.unpack("\1\137"),
        DFA.unpack(""),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack("\1\145"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\154"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\156"),
        DFA.unpack("\1\157\5\uffff\1\160"),
        DFA.unpack("\1\161"),
        DFA.unpack("\1\162"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\170\5\uffff\1\167"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081\6\uffff\1\u0082"),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\1\u0084"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\1\u008a"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u008c"),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u0090"),
        DFA.unpack("\1\u0091"),
        DFA.unpack("\1\u0092"),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\1\u0094"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\1\u0098"),
        DFA.unpack("\1\u0099"),
        DFA.unpack("\1\u009a"),
        DFA.unpack("\1\u009b"),
        DFA.unpack(""),
        DFA.unpack("\1\u009c"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u009e"),
        DFA.unpack("\1\u009f"),
        DFA.unpack("\1\u00a0\21\uffff\1\u00a1"),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\1\u00a3"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\1\u00a7"),
        DFA.unpack("\1\u00a8"),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\1\u00ad"),
        DFA.unpack("\1\u00ae"),
        DFA.unpack("\1\u00af"),
        DFA.unpack("\1\u00b0"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack("\1\u00b5"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00b7"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\1\u00bb"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00c1"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00c3"),
        DFA.unpack("\1\u00c4"),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\u00cb"),
        DFA.unpack("\1\u00cc"),
        DFA.unpack("\1\u00cd"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ce"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00d0"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d8"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack(""),
        DFA.unpack("\1\u00df"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00e3"),
        DFA.unpack("\1\u00e4"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e9"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00ea"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00ec"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ed"),
        DFA.unpack("\1\u00ee"),
        DFA.unpack("\1\u00ef"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f1"),
        DFA.unpack("\1\u00f2"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f3"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f4"),
        DFA.unpack("\1\u00f5"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00f7"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u00fb"),
        DFA.unpack("\1\u00fc"),
        DFA.unpack("\1\u00fd"),
        DFA.unpack("\1\u00fe"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ff"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0100"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u0102"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\1\u0104"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("\1\u0106"),
        DFA.unpack(""),
        DFA.unpack("\1\u0107"),
        DFA.unpack(""),
        DFA.unpack("\1\u0108"),
        DFA.unpack("\1\u0109"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack("\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(""),
        DFA.unpack("")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ProtoCCLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
