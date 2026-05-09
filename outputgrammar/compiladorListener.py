# Generated from c:\Users\alsan\Documents\compilador-interfaz\compilador-interfaz\grammar\compilador.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.
class compiladorListener(ParseTreeListener):

    # Enter a parse tree produced by compiladorParser#inicio.
    def enterInicio(self, ctx:compiladorParser.InicioContext):
        pass

    # Exit a parse tree produced by compiladorParser#inicio.
    def exitInicio(self, ctx:compiladorParser.InicioContext):
        pass


    # Enter a parse tree produced by compiladorParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#Declaracion.
    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladorParser#Declaracion.
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladorParser#Asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#Asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#CondicionalStmt.
    def enterCondicionalStmt(self, ctx:compiladorParser.CondicionalStmtContext):
        pass

    # Exit a parse tree produced by compiladorParser#CondicionalStmt.
    def exitCondicionalStmt(self, ctx:compiladorParser.CondicionalStmtContext):
        pass


    # Enter a parse tree produced by compiladorParser#CicloStmt.
    def enterCicloStmt(self, ctx:compiladorParser.CicloStmtContext):
        pass

    # Exit a parse tree produced by compiladorParser#CicloStmt.
    def exitCicloStmt(self, ctx:compiladorParser.CicloStmtContext):
        pass


    # Enter a parse tree produced by compiladorParser#SumRes.
    def enterSumRes(self, ctx:compiladorParser.SumResContext):
        pass

    # Exit a parse tree produced by compiladorParser#SumRes.
    def exitSumRes(self, ctx:compiladorParser.SumResContext):
        pass


    # Enter a parse tree produced by compiladorParser#Numero.
    def enterNumero(self, ctx:compiladorParser.NumeroContext):
        pass

    # Exit a parse tree produced by compiladorParser#Numero.
    def exitNumero(self, ctx:compiladorParser.NumeroContext):
        pass


    # Enter a parse tree produced by compiladorParser#Comparacion.
    def enterComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#Comparacion.
    def exitComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#Variable.
    def enterVariable(self, ctx:compiladorParser.VariableContext):
        pass

    # Exit a parse tree produced by compiladorParser#Variable.
    def exitVariable(self, ctx:compiladorParser.VariableContext):
        pass


    # Enter a parse tree produced by compiladorParser#MulDiv.
    def enterMulDiv(self, ctx:compiladorParser.MulDivContext):
        pass

    # Exit a parse tree produced by compiladorParser#MulDiv.
    def exitMulDiv(self, ctx:compiladorParser.MulDivContext):
        pass


    # Enter a parse tree produced by compiladorParser#Parentesis.
    def enterParentesis(self, ctx:compiladorParser.ParentesisContext):
        pass

    # Exit a parse tree produced by compiladorParser#Parentesis.
    def exitParentesis(self, ctx:compiladorParser.ParentesisContext):
        pass



del compiladorParser