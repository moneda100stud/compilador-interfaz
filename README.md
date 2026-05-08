# Compilador Interfaz

Este proyecto contiene una interfaz gráfica para compilar programas escritos en un lenguaje llamado `Lenguaje`.

## Estructura

- `grammar/`: gramática ANTLR fuente (`compilador.g4`).
- `outputgrammar/`: archivos generados por ANTLR para Python.
- `UL/`: módulo de la interfaz gráfica y el backend del compilador.

## Requisitos

- Python 3.10+ (recomendado)
- `PyQt6`
- `antlr4-python3-runtime`

## Uso

1. Genera los archivos de ANTLR desde el directorio raíz del proyecto:

```bash
python generate_antlr.py
```

2. Ejecuta la interfaz desde el directorio raíz:

```bash
python run.py
```

Alternativamente, también funciona con:

```bash
python -m UL.main
```

## Compilación

La aplicación analiza el código de entrada y muestra el árbol sintáctico si no hay errores.
