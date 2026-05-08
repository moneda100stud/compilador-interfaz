try:
    from .compiladorLexer import compiladorLexer
    from .compiladorParser import compiladorParser
except ImportError:
    # Los archivos se generan con ANTLR y pueden no estar presentes aún.
    pass
