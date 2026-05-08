# Generated from C:\Users\alsan\Documents\compilador-interfaz\compilador-interfaz\grammar\compilador.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\3\3\3\5\3\31\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6+\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\63\n")
        buf.write("\6\f\6\16\6\66\13\6\3\6\2\3\n\7\2\4\6\b\n\2\4\3\2\b\t")
        buf.write("\3\2\n\13\28\2\f\3\2\2\2\4\30\3\2\2\2\6\32\3\2\2\2\b\36")
        buf.write("\3\2\2\2\n*\3\2\2\2\f\r\7\3\2\2\r\21\7\4\2\2\16\20\5\4")
        buf.write("\3\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3")
        buf.write("\2\2\2\22\24\3\2\2\2\23\21\3\2\2\2\24\25\7\5\2\2\25\3")
        buf.write("\3\2\2\2\26\31\5\6\4\2\27\31\5\b\5\2\30\26\3\2\2\2\30")
        buf.write("\27\3\2\2\2\31\5\3\2\2\2\32\33\7\16\2\2\33\34\7\17\2\2")
        buf.write("\34\35\7\6\2\2\35\7\3\2\2\2\36\37\7\17\2\2\37 \7\7\2\2")
        buf.write(" !\5\n\6\2!\"\7\6\2\2\"\t\3\2\2\2#$\b\6\1\2$%\7\f\2\2")
        buf.write("%&\5\n\6\2&\'\7\r\2\2\'+\3\2\2\2(+\7\20\2\2)+\7\17\2\2")
        buf.write("*#\3\2\2\2*(\3\2\2\2*)\3\2\2\2+\64\3\2\2\2,-\f\7\2\2-")
        buf.write(".\t\2\2\2.\63\5\n\6\b/\60\f\6\2\2\60\61\t\3\2\2\61\63")
        buf.write("\5\n\6\7\62,\3\2\2\2\62/\3\2\2\2\63\66\3\2\2\2\64\62\3")
        buf.write("\2\2\2\64\65\3\2\2\2\65\13\3\2\2\2\66\64\3\2\2\2\7\21")
        buf.write("\30*\62\64")
        return buf.getvalue()


class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Lenguaje'", "'{'", "'}'", "';'", "'='", 
                     "'*'", "'/'", "'+'", "'-'", "'('", "')'", "'entero'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENTERO", "VAR", "NUM", "WS" ]

    RULE_inicio = 0
    RULE_instrucciones = 1
    RULE_declaracionVariables = 2
    RULE_asignacionVariables = 3
    RULE_expr = 4

    ruleNames =  [ "inicio", "instrucciones", "declaracionVariables", "asignacionVariables", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    ENTERO=12
    VAR=13
    NUM=14
    WS=15

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
            self.state = 10
            self.match(compiladorParser.T__0)
            self.state = 11
            self.match(compiladorParser.T__1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==compiladorParser.ENTERO or _la==compiladorParser.VAR:
                self.state = 12
                self.instrucciones()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(compiladorParser.T__2)
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
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladorParser.ENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.declaracionVariables()
                pass
            elif token in [compiladorParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.asignacionVariables()
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
            self.state = 24
            self.match(compiladorParser.ENTERO)
            self.state = 25
            self.match(compiladorParser.VAR)
            self.state = 26
            self.match(compiladorParser.T__3)
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
            self.state = 28
            self.match(compiladorParser.VAR)
            self.state = 29
            self.match(compiladorParser.T__4)
            self.state = 30
            self.expr(0)
            self.state = 31
            self.match(compiladorParser.T__3)
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

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladorParser.T__9]:
                localctx = compiladorParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 34
                self.match(compiladorParser.T__9)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(compiladorParser.T__10)
                pass
            elif token in [compiladorParser.NUM]:
                localctx = compiladorParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(compiladorParser.NUM)
                pass
            elif token in [compiladorParser.VAR]:
                localctx = compiladorParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(compiladorParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = compiladorParser.MulDivContext(self, compiladorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 43
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==compiladorParser.T__5 or _la==compiladorParser.T__6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = compiladorParser.SumResContext(self, compiladorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 46
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==compiladorParser.T__7 or _la==compiladorParser.T__8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(5)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




