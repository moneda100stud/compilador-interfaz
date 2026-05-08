import os
import sys
from dataclasses import dataclass, field
from typing import List, Optional
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

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
    tree: Optional[str] = None
    errors: List[str] = field(default_factory=list)

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
    parser = compiladorParser(token_stream)
    parser.removeErrorListeners()

    error_listener = ParserErrorListener()
    parser.addErrorListener(error_listener)

    tree = parser.inicio()
    if error_listener.errors:
        output_lines = ["Errores de sintaxis:"]
        output_lines.extend(f"- {err}" for err in error_listener.errors)
        return CompilerReport(success=False, output="\n".join(output_lines), errors=error_listener.errors)

    tree_text = tree.toStringTree(recog=parser)
    output = "Análisis completo sin errores.\n\nÁrbol sintáctico:\n" + tree_text
    return CompilerReport(success=True, output=output, tree=tree_text)
