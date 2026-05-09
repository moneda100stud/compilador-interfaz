# Generated from c:\Users\alsan\Documents\compilador-interfaz\compilador-interfaz\grammar\compilador.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3\37\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\60\n\6\f\6\16\6\63")
        buf.write("\13\6\3\6\3\6\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\3\6\5\6")
        buf.write("?\n\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7G\n\7\f\7\16\7J\13\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bU\n\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b`\n\b\f\b\16\bc\13\b\3")
        buf.write("\b\2\3\16\t\2\4\6\b\n\f\16\2\5\3\2\6\7\3\2\b\t\3\2\16")
        buf.write("\21\2j\2\20\3\2\2\2\4\36\3\2\2\2\6 \3\2\2\2\b$\3\2\2\2")
        buf.write("\n)\3\2\2\2\f@\3\2\2\2\16T\3\2\2\2\20\21\7\3\2\2\21\25")
        buf.write("\7\24\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\27\3\2\2\2\25")
        buf.write("\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2")
        buf.write("\30\31\7\25\2\2\31\3\3\2\2\2\32\37\5\6\4\2\33\37\5\b\5")
        buf.write("\2\34\37\5\n\6\2\35\37\5\f\7\2\36\32\3\2\2\2\36\33\3\2")
        buf.write("\2\2\36\34\3\2\2\2\36\35\3\2\2\2\37\5\3\2\2\2 !\7\r\2")
        buf.write("\2!\"\7\26\2\2\"#\7\4\2\2#\7\3\2\2\2$%\7\26\2\2%&\7\5")
        buf.write("\2\2&\'\5\16\b\2\'(\7\4\2\2(\t\3\2\2\2)*\7\n\2\2*+\7\22")
        buf.write("\2\2+,\5\16\b\2,-\7\23\2\2-\61\7\24\2\2.\60\5\4\3\2/.")
        buf.write("\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\64")
        buf.write("\3\2\2\2\63\61\3\2\2\2\64>\7\25\2\2\65\66\7\13\2\2\66")
        buf.write(":\7\24\2\2\679\5\4\3\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2")
        buf.write(":;\3\2\2\2;=\3\2\2\2<:\3\2\2\2=?\7\25\2\2>\65\3\2\2\2")
        buf.write(">?\3\2\2\2?\13\3\2\2\2@A\7\f\2\2AB\7\22\2\2BC\5\16\b\2")
        buf.write("CD\7\23\2\2DH\7\24\2\2EG\5\4\3\2FE\3\2\2\2GJ\3\2\2\2H")
        buf.write("F\3\2\2\2HI\3\2\2\2IK\3\2\2\2JH\3\2\2\2KL\7\25\2\2L\r")
        buf.write("\3\2\2\2MN\b\b\1\2NO\7\22\2\2OP\5\16\b\2PQ\7\23\2\2QU")
        buf.write("\3\2\2\2RU\7\27\2\2SU\7\26\2\2TM\3\2\2\2TR\3\2\2\2TS\3")
        buf.write("\2\2\2Ua\3\2\2\2VW\f\b\2\2WX\t\2\2\2X`\5\16\b\tYZ\f\7")
        buf.write("\2\2Z[\t\3\2\2[`\5\16\b\b\\]\f\6\2\2]^\t\4\2\2^`\5\16")
        buf.write("\b\7_V\3\2\2\2_Y\3\2\2\2_\\\3\2\2\2`c\3\2\2\2a_\3\2\2")
        buf.write("\2ab\3\2\2\2b\17\3\2\2\2ca\3\2\2\2\13\25\36\61:>HT_a")
        return buf.getvalue()


class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Lenguaje'", "';'", "'='", "'*'", "'/'", 
                     "'+'", "'-'", "'si'", "'sino'", "'mientras'", "'entero'", 
                     "'>'", "'<'", "'=='", "'!='", "'('", "')'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SI", "SINO", "MIENTRAS", "ENTERO", "GT", "LT", "EQ", 
                      "NEQ", "PAREN_A", "PAREN_C", "LLAVE_A", "LLAVE_C", 
                      "VAR", "NUM", "WS" ]

    RULE_inicio = 0
    RULE_instrucciones = 1
    RULE_declaracionVariables = 2
    RULE_asignacionVariables = 3
    RULE_condicional = 4
    RULE_ciclo = 5
    RULE_expr = 6

    ruleNames =  [ "inicio", "instrucciones", "declaracionVariables", "asignacionVariables", 
                   "condicional", "ciclo", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    SI=8
    SINO=9
    MIENTRAS=10
    ENTERO=11
    GT=12
    LT=13
    EQ=14
    NEQ=15
    PAREN_A=16
    PAREN_C=17
    LLAVE_A=18
    LLAVE_C=19
    VAR=20
    NUM=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_A(self):
            return self.getToken(compiladorParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(compiladorParser.LLAVE_C, 0)

        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(compiladorParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return compiladorParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)




    def inicio(self):

        localctx = compiladorParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(compiladorParser.T__0)
            self.state = 15
            self.match(compiladorParser.LLAVE_A)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << compiladorParser.SI) | (1 << compiladorParser.MIENTRAS) | (1 << compiladorParser.ENTERO) | (1 << compiladorParser.VAR))) != 0):
                self.state = 16
                self.instrucciones()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(compiladorParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionVariables(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionVariablesContext,0)


        def asignacionVariables(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionVariablesContext,0)


        def condicional(self):
            return self.getTypedRuleContext(compiladorParser.CondicionalContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(compiladorParser.CicloContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)




    def instrucciones(self):

        localctx = compiladorParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladorParser.ENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.declaracionVariables()
                pass
            elif token in [compiladorParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.asignacionVariables()
                pass
            elif token in [compiladorParser.SI]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.condicional()
                pass
            elif token in [compiladorParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.ciclo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionVariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return compiladorParser.RULE_declaracionVariables

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionContext(DeclaracionVariablesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.DeclaracionVariablesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTERO(self):
            return self.getToken(compiladorParser.ENTERO, 0)
        def VAR(self):
            return self.getToken(compiladorParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)



    def declaracionVariables(self):

        localctx = compiladorParser.DeclaracionVariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracionVariables)
        try:
            localctx = compiladorParser.DeclaracionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(compiladorParser.ENTERO)
            self.state = 31
            self.match(compiladorParser.VAR)
            self.state = 32
            self.match(compiladorParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionVariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return compiladorParser.RULE_asignacionVariables

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(AsignacionVariablesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.AsignacionVariablesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(compiladorParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)



    def asignacionVariables(self):

        localctx = compiladorParser.AsignacionVariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacionVariables)
        try:
            localctx = compiladorParser.AsignacionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(compiladorParser.VAR)
            self.state = 35
            self.match(compiladorParser.T__2)
            self.state = 36
            self.expr(0)
            self.state = 37
            self.match(compiladorParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return compiladorParser.RULE_condicional

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionalStmtContext(CondicionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.CondicionalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SI(self):
            return self.getToken(compiladorParser.SI, 0)
        def PAREN_A(self):
            return self.getToken(compiladorParser.PAREN_A, 0)
        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)

        def PAREN_C(self):
            return self.getToken(compiladorParser.PAREN_C, 0)
        def LLAVE_A(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.LLAVE_A)
            else:
                return self.getToken(compiladorParser.LLAVE_A, i)
        def LLAVE_C(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.LLAVE_C)
            else:
                return self.getToken(compiladorParser.LLAVE_C, i)
        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(compiladorParser.InstruccionesContext,i)

        def SINO(self):
            return self.getToken(compiladorParser.SINO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionalStmt" ):
                listener.enterCondicionalStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionalStmt" ):
                listener.exitCondicionalStmt(self)



    def condicional(self):

        localctx = compiladorParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            localctx = compiladorParser.CondicionalStmtContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(compiladorParser.SI)
            self.state = 40
            self.match(compiladorParser.PAREN_A)
            self.state = 41
            self.expr(0)
            self.state = 42
            self.match(compiladorParser.PAREN_C)
            self.state = 43
            self.match(compiladorParser.LLAVE_A)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << compiladorParser.SI) | (1 << compiladorParser.MIENTRAS) | (1 << compiladorParser.ENTERO) | (1 << compiladorParser.VAR))) != 0):
                self.state = 44
                self.instrucciones()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(compiladorParser.LLAVE_C)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==compiladorParser.SINO:
                self.state = 51
                self.match(compiladorParser.SINO)
                self.state = 52
                self.match(compiladorParser.LLAVE_A)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << compiladorParser.SI) | (1 << compiladorParser.MIENTRAS) | (1 << compiladorParser.ENTERO) | (1 << compiladorParser.VAR))) != 0):
                    self.state = 53
                    self.instrucciones()
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
                self.match(compiladorParser.LLAVE_C)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return compiladorParser.RULE_ciclo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CicloStmtContext(CicloContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.CicloContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MIENTRAS(self):
            return self.getToken(compiladorParser.MIENTRAS, 0)
        def PAREN_A(self):
            return self.getToken(compiladorParser.PAREN_A, 0)
        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)

        def PAREN_C(self):
            return self.getToken(compiladorParser.PAREN_C, 0)
        def LLAVE_A(self):
            return self.getToken(compiladorParser.LLAVE_A, 0)
        def LLAVE_C(self):
            return self.getToken(compiladorParser.LLAVE_C, 0)
        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(compiladorParser.InstruccionesContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicloStmt" ):
                listener.enterCicloStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicloStmt" ):
                listener.exitCicloStmt(self)



    def ciclo(self):

        localctx = compiladorParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ciclo)
        self._la = 0 # Token type
        try:
            localctx = compiladorParser.CicloStmtContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(compiladorParser.MIENTRAS)
            self.state = 63
            self.match(compiladorParser.PAREN_A)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.match(compiladorParser.PAREN_C)
            self.state = 66
            self.match(compiladorParser.LLAVE_A)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << compiladorParser.SI) | (1 << compiladorParser.MIENTRAS) | (1 << compiladorParser.ENTERO) | (1 << compiladorParser.VAR))) != 0):
                self.state = 67
                self.instrucciones()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(compiladorParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return compiladorParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumResContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.ExprContext)
            else:
                return self.getTypedRuleContext(compiladorParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumRes" ):
                listener.enterSumRes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumRes" ):
                listener.exitSumRes(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(compiladorParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class ComparacionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.ExprContext)
            else:
                return self.getTypedRuleContext(compiladorParser.ExprContext,i)

        def GT(self):
            return self.getToken(compiladorParser.GT, 0)
        def LT(self):
            return self.getToken(compiladorParser.LT, 0)
        def EQ(self):
            return self.getToken(compiladorParser.EQ, 0)
        def NEQ(self):
            return self.getToken(compiladorParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(compiladorParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.ExprContext)
            else:
                return self.getTypedRuleContext(compiladorParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a compiladorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAREN_A(self):
            return self.getToken(compiladorParser.PAREN_A, 0)
        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)

        def PAREN_C(self):
            return self.getToken(compiladorParser.PAREN_C, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = compiladorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladorParser.PAREN_A]:
                localctx = compiladorParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 76
                self.match(compiladorParser.PAREN_A)
                self.state = 77
                self.expr(0)
                self.state = 78
                self.match(compiladorParser.PAREN_C)
                pass
            elif token in [compiladorParser.NUM]:
                localctx = compiladorParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(compiladorParser.NUM)
                pass
            elif token in [compiladorParser.VAR]:
                localctx = compiladorParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(compiladorParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = compiladorParser.MulDivContext(self, compiladorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 85
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==compiladorParser.T__3 or _la==compiladorParser.T__4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = compiladorParser.SumResContext(self, compiladorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 88
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==compiladorParser.T__5 or _la==compiladorParser.T__6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = compiladorParser.ComparacionContext(self, compiladorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 91
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << compiladorParser.GT) | (1 << compiladorParser.LT) | (1 << compiladorParser.EQ) | (1 << compiladorParser.NEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        self.expr(5)
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




