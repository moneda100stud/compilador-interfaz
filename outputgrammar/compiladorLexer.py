# Generated from c:\Users\alsan\Documents\compilador-interfaz\compilador-interfaz\grammar\compilador.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u0089\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\7\25q\n\25\f\25\16\25t\13\25\3\26\6\26w\n\26")
        buf.write("\r\26\16\26x\3\26\3\26\6\26}\n\26\r\26\16\26~\5\26\u0081")
        buf.write("\n\26\3\27\6\27\u0084\n\27\r\27\16\27\u0085\3\27\3\27")
        buf.write("\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f")
        buf.write("\17\17\"\"\2\u008d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\3/\3\2\2\2\58\3\2\2\2\7:\3\2\2\2\t<\3")
        buf.write("\2\2\2\13>\3\2\2\2\r@\3\2\2\2\17B\3\2\2\2\21D\3\2\2\2")
        buf.write("\23G\3\2\2\2\25L\3\2\2\2\27U\3\2\2\2\31\\\3\2\2\2\33^")
        buf.write("\3\2\2\2\35`\3\2\2\2\37c\3\2\2\2!f\3\2\2\2#h\3\2\2\2%")
        buf.write("j\3\2\2\2\'l\3\2\2\2)n\3\2\2\2+v\3\2\2\2-\u0083\3\2\2")
        buf.write("\2/\60\7N\2\2\60\61\7g\2\2\61\62\7p\2\2\62\63\7i\2\2\63")
        buf.write("\64\7w\2\2\64\65\7c\2\2\65\66\7l\2\2\66\67\7g\2\2\67\4")
        buf.write("\3\2\2\289\7=\2\29\6\3\2\2\2:;\7?\2\2;\b\3\2\2\2<=\7,")
        buf.write("\2\2=\n\3\2\2\2>?\7\61\2\2?\f\3\2\2\2@A\7-\2\2A\16\3\2")
        buf.write("\2\2BC\7/\2\2C\20\3\2\2\2DE\7u\2\2EF\7k\2\2F\22\3\2\2")
        buf.write("\2GH\7u\2\2HI\7k\2\2IJ\7p\2\2JK\7q\2\2K\24\3\2\2\2LM\7")
        buf.write("o\2\2MN\7k\2\2NO\7g\2\2OP\7p\2\2PQ\7v\2\2QR\7t\2\2RS\7")
        buf.write("c\2\2ST\7u\2\2T\26\3\2\2\2UV\7g\2\2VW\7p\2\2WX\7v\2\2")
        buf.write("XY\7g\2\2YZ\7t\2\2Z[\7q\2\2[\30\3\2\2\2\\]\7@\2\2]\32")
        buf.write("\3\2\2\2^_\7>\2\2_\34\3\2\2\2`a\7?\2\2ab\7?\2\2b\36\3")
        buf.write("\2\2\2cd\7#\2\2de\7?\2\2e \3\2\2\2fg\7*\2\2g\"\3\2\2\2")
        buf.write("hi\7+\2\2i$\3\2\2\2jk\7}\2\2k&\3\2\2\2lm\7\177\2\2m(\3")
        buf.write("\2\2\2nr\t\2\2\2oq\t\3\2\2po\3\2\2\2qt\3\2\2\2rp\3\2\2")
        buf.write("\2rs\3\2\2\2s*\3\2\2\2tr\3\2\2\2uw\t\4\2\2vu\3\2\2\2w")
        buf.write("x\3\2\2\2xv\3\2\2\2xy\3\2\2\2y\u0080\3\2\2\2z|\7\60\2")
        buf.write("\2{}\t\4\2\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2")
        buf.write("\2\177\u0081\3\2\2\2\u0080z\3\2\2\2\u0080\u0081\3\2\2")
        buf.write("\2\u0081,\3\2\2\2\u0082\u0084\t\5\2\2\u0083\u0082\3\2")
        buf.write("\2\2\u0084\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\b\27\2\2\u0088")
        buf.write(".\3\2\2\2\b\2rx~\u0080\u0085\3\b\2\2")
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
    SI = 8
    SINO = 9
    MIENTRAS = 10
    ENTERO = 11
    GT = 12
    LT = 13
    EQ = 14
    NEQ = 15
    PAREN_A = 16
    PAREN_C = 17
    LLAVE_A = 18
    LLAVE_C = 19
    VAR = 20
    NUM = 21
    WS = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Lenguaje'", "';'", "'='", "'*'", "'/'", "'+'", "'-'", "'si'", 
            "'sino'", "'mientras'", "'entero'", "'>'", "'<'", "'=='", "'!='", 
            "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "SI", "SINO", "MIENTRAS", "ENTERO", "GT", "LT", "EQ", "NEQ", 
            "PAREN_A", "PAREN_C", "LLAVE_A", "LLAVE_C", "VAR", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "SI", "SINO", "MIENTRAS", "ENTERO", "GT", "LT", "EQ", 
                  "NEQ", "PAREN_A", "PAREN_C", "LLAVE_A", "LLAVE_C", "VAR", 
                  "NUM", "WS" ]

    grammarFileName = "compilador.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


