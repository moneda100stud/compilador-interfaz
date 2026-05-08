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

## Testing con GRUN

Para testing interactivo con Java, consulta `grun_example.sh` que muestra cómo usar GRUN con archivos Java generados por ANTLR4.

Para Python, esta interfaz proporciona funcionalidad equivalente con análisis detallado de tokens, símbolos y árbol sintáctico.

La interfaz incluye un panel lateral con:
- Ejercicio de ejemplo con instrucciones
- Opciones de ANTLR4 (desplegable para ahorrar espacio)
- Información sobre GRUN (herramienta de testing Java - esta interfaz Python proporciona funcionalidad equivalente)
