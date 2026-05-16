import os
import sys
from dataclasses import dataclass, field
from typing import List, Optional
from antlr4 import InputStream, CommonTokenStream, TerminalNode
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Token import Token

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from outputgrammar.compiladorLexer import compiladorLexer
    from outputgrammar.compiladorParser import compiladorParser
except ImportError as exc:
    raise ImportError(
        "No se encontraron los archivos generados de ANTLR en la carpeta 'outputgrammar'. "
        "Ejecuta: python generate_antlr.py"
    ) from exc

@dataclass
class CompilerReport:
    success: bool
    output: str
    tree_text: Optional[str] = None
    tree: Optional[object] = None
    errors: List[str] = field(default_factory=list)
    tokens: List[str] = field(default_factory=list)
    symbols: List[str] = field(default_factory=list)
    values: dict = field(default_factory=dict)

class ParserErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors: List[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message = f"Línea {line}:{column} - {msg}"
        self.errors.append(message)


def parse_source(source: str) -> CompilerReport:
    if not source.strip():
        return CompilerReport(success=False, output="El código de entrada está vacío.", errors=["Editor vacío"])

    input_stream = InputStream(source)
    lexer = compiladorLexer(input_stream)
    lexer.removeErrorListeners()

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    # Capturar tokens
    tokens = []
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = compiladorLexer.symbolicNames[token.type] if token.type < len(compiladorLexer.symbolicNames) else f"T{token.type}"
            tokens.append(f"{token_name}: '{token.text}' (línea {token.line}:{token.column})")

    parser = compiladorParser(token_stream)
    parser.removeErrorListeners()

    error_listener = ParserErrorListener()
    parser.addErrorListener(error_listener)

    tree = parser.inicio()

    symbols = []
    values = {}
    declared = set()

    def parse_number(text: str):
        return int(text) if '.' not in text else float(text)

    def declare_variable(name: str):
        if name not in declared:
            declared.add(name)
            symbols.append(f"Variable: {name} (tipo: entero)")
            values[name] = None

    def assign_variable(name: str, value):
        if name not in declared:
            declared.add(name)
            symbols.append(f"Variable: {name} (tipo: entero)")
        values[name] = value

    def eval_expr(expr):
        if expr is None:
            raise ValueError("Expresión vacía")

        class_name = expr.__class__.__name__
        if class_name == 'NumeroContext':
            return parse_number(expr.NUM().getText())
        if class_name == 'VariableContext':
            name = expr.VAR().getText()
            if name not in values:
                raise NameError(f"Variable no declarada: {name}")
            return values[name]
        if class_name == 'ParentesisContext':
            return eval_expr(expr.expr())
        if class_name == 'SumResContext':
            left = eval_expr(expr.expr(0))
            right = eval_expr(expr.expr(1))
            if expr.op.text == '+':
                return left + right
            return left - right
        if class_name == 'MulDivContext':
            left = eval_expr(expr.expr(0))
            right = eval_expr(expr.expr(1))
            if expr.op.text == '*':
                return left * right
            return left / right
        if class_name == 'ComparacionContext':
            left = eval_expr(expr.expr(0))
            right = eval_expr(expr.expr(1))
            op = expr.op.text
            if op == '>':
                return left > right
            if op == '<':
                return left < right
            if op == '==':
                return left == right
            return left != right

        raise ValueError(f"Tipo de expresión no soportado: {class_name}")

    def collect_instruction_blocks(context):
        blocks = [[]]
        current_block = blocks[0]
        depth = 0

        for child in context.children:
            if isinstance(child, TerminalNode):
                symbol = child.getSymbol() if hasattr(child, 'getSymbol') else child.symbol
                if symbol is None:
                    continue
                token_type = symbol.type
                if token_type == compiladorParser.SINO and depth == 0:
                    blocks.append([])
                    current_block = blocks[-1]
                    continue
                if token_type == compiladorParser.LLAVE_A:
                    depth += 1
                    continue
                if token_type == compiladorParser.LLAVE_C:
                    depth -= 1
                    continue
            elif isinstance(child, compiladorParser.InstruccionesContext):
                current_block.append(child)

        return blocks

    def execute_instruction(instruction):
        if instruction.declaracionVariables() is not None:
            decl = instruction.declaracionVariables()
            declare_variable(decl.VAR().getText())
            return

        if instruction.asignacionVariables() is not None:
            asign = instruction.asignacionVariables()
            assign_variable(asign.VAR().getText(), eval_expr(asign.expr()))
            return

        if instruction.condicional() is not None:
            cond = instruction.condicional()
            condition = eval_expr(cond.expr())
            blocks = collect_instruction_blocks(cond)
            if condition:
                for instr in blocks[0]:
                    execute_instruction(instr)
            elif len(blocks) > 1:
                for instr in blocks[1]:
                    execute_instruction(instr)
            return

        if instruction.ciclo() is not None:
            ciclo = instruction.ciclo()
            blocks = collect_instruction_blocks(ciclo)
            while eval_expr(ciclo.expr()):
                for instr in blocks[0]:
                    execute_instruction(instr)
            return

        raise ValueError("Instrucción no reconocida o no soportada")

    try:
        instrucciones_nodes = tree.instrucciones()
        if instrucciones_nodes is not None:
            if isinstance(instrucciones_nodes, list):
                for instr in instrucciones_nodes:
                    execute_instruction(instr)
            else:
                execute_instruction(instrucciones_nodes)
    except Exception as exc:
        error_listener.errors.append(f"Error de ejecución: {exc}")

    if error_listener.errors:
        output_lines = ["Errores de sintaxis o ejecución:"]
        output_lines.extend(f"- {err}" for err in error_listener.errors)
        return CompilerReport(
            success=False,
            output="\n".join(output_lines),
            errors=error_listener.errors,
            tokens=tokens,
            symbols=symbols,
            values=values,
        )

    tree_text = tree.toStringTree(recog=parser)
    output = "Análisis completo sin errores."
    return CompilerReport(
        success=True,
        output=output,
        tree_text=tree_text,
        tree=tree,
        tokens=tokens,
        symbols=symbols,
        values=values,
    )
