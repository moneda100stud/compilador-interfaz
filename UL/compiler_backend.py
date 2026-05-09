import os
import sys
from dataclasses import dataclass, field
from typing import List, Optional
from antlr4 import InputStream, CommonTokenStream
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

    # Capturar símbolos (variables declaradas) - búsqueda más robusta
    symbols = []
    try:
        # Buscar todas las declaraciones de variables en el árbol
        def find_variables(node):
            # Buscamos nodos que correspondan a la regla de declaración
            # Se usa el nombre de la clase para mayor robustez si cambian los índices
            class_name = node.__class__.__name__
            if 'Declaracion' in class_name:
                if hasattr(node, 'children') and node.children and len(node.children) >= 2:
                    # Buscar el token VAR en los hijos
                    for child in node.children:
                        if hasattr(child, 'getText') and hasattr(child, 'getSymbol'):
                            symbol = child.getSymbol()
                            if symbol and symbol.type == compiladorLexer.VAR:
                                var_name = child.getText()
                                symbols.append(f"Variable: {var_name} (tipo: entero)")
                                break
            # Recursión en hijos
            if hasattr(node, 'children') and node.children:
                for child in node.children:
                    find_variables(child)

        find_variables(tree)
    except Exception:
        # Si hay algún error en la extracción de símbolos, continuar sin ellos
        pass

    if error_listener.errors:
        output_lines = ["Errores de sintaxis:"]
        output_lines.extend(f"- {err}" for err in error_listener.errors)
        return CompilerReport(
            success=False,
            output="\n".join(output_lines),
            errors=error_listener.errors,
            tokens=tokens,
            symbols=symbols,
        )

    tree_text = tree.toStringTree(recog=parser)
    output = "Análisis completo sin errores.\n\nÁrbol sintáctico:\n" + tree_text
    return CompilerReport(
        success=True,
        output=output,
        tree_text=tree_text,
        tree=tree,
        tokens=tokens,
        symbols=symbols,
    )
