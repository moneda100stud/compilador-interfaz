# Generated from C:\Users\alsan\Documents\compilador-interfaz\compilador-interfaz\grammar\compilador.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\7\16H\n\16\f\16\16\16K\13\16\3\17")
        buf.write("\6\17N\n\17\r\17\16\17O\3\17\3\17\6\17T\n\17\r\17\16\17")
        buf.write("U\5\17X\n\17\3\20\6\20[\n\20\r\20\16\20\\\3\20\3\20\2")
        buf.write("\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21\3\2\6\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\5\2\13\f\17\17\"\"\2d\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\3!\3\2\2\2\5*\3\2\2\2\7,\3\2\2\2\t.\3\2\2\2\13")
        buf.write("\60\3\2\2\2\r\62\3\2\2\2\17\64\3\2\2\2\21\66\3\2\2\2\23")
        buf.write("8\3\2\2\2\25:\3\2\2\2\27<\3\2\2\2\31>\3\2\2\2\33E\3\2")
        buf.write("\2\2\35M\3\2\2\2\37Z\3\2\2\2!\"\7N\2\2\"#\7g\2\2#$\7p")
        buf.write("\2\2$%\7i\2\2%&\7w\2\2&\'\7c\2\2\'(\7l\2\2()\7g\2\2)\4")
        buf.write("\3\2\2\2*+\7}\2\2+\6\3\2\2\2,-\7\177\2\2-\b\3\2\2\2./")
        buf.write("\7=\2\2/\n\3\2\2\2\60\61\7?\2\2\61\f\3\2\2\2\62\63\7,")
        buf.write("\2\2\63\16\3\2\2\2\64\65\7\61\2\2\65\20\3\2\2\2\66\67")
        buf.write("\7-\2\2\67\22\3\2\2\289\7/\2\29\24\3\2\2\2:;\7*\2\2;\26")
        buf.write("\3\2\2\2<=\7+\2\2=\30\3\2\2\2>?\7g\2\2?@\7p\2\2@A\7v\2")
        buf.write("\2AB\7g\2\2BC\7t\2\2CD\7q\2\2D\32\3\2\2\2EI\t\2\2\2FH")
        buf.write("\t\3\2\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\34\3")
        buf.write("\2\2\2KI\3\2\2\2LN\t\4\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2")
        buf.write("\2OP\3\2\2\2PW\3\2\2\2QS\7\60\2\2RT\t\4\2\2SR\3\2\2\2")
        buf.write("TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WQ\3\2\2\2WX\3")
        buf.write("\2\2\2X\36\3\2\2\2Y[\t\5\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3")
        buf.write("\2\2\2\\]\3\2\2\2]^\3\2\2\2^_\b\20\2\2_ \3\2\2\2\b\2I")
        buf.write("OUW\\\3\b\2\2")
        return buf.getvalue()


class compiladorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    ENTERO = 12
    VAR = 13
    NUM = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Lenguaje'", "'{'", "'}'", "';'", "'='", "'*'", "'/'", "'+'", 
            "'-'", "'('", "')'", "'entero'" ]

    symbolicNames = [ "<INVALID>",
            "ENTERO", "VAR", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "ENTERO", "VAR", "NUM", 
                  "WS" ]

    grammarFileName = "compilador.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


