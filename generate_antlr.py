import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAMMAR_DIR = os.path.join(ROOT, 'grammar')
OUTPUT_DIR = os.path.join(ROOT, 'outputgrammar')
GRAMMAR_FILE = os.path.join(GRAMMAR_DIR, 'compilador.g4')

if not os.path.isfile(GRAMMAR_FILE):
    raise FileNotFoundError(f'No se encuentra el archivo de gramática: {GRAMMAR_FILE}')

os.makedirs(OUTPUT_DIR, exist_ok=True)
init_file = os.path.join(OUTPUT_DIR, '__init__.py')
if not os.path.exists(init_file):
    open(init_file, 'w', encoding='utf-8').close()

antlr_executable = shutil.which('antlr4') or shutil.which('antlr4.bat')
if not antlr_executable:
    raise FileNotFoundError(
        'No se encontró el ejecutable ANTLR. Asegúrate de tener antlr4 en el PATH o instala ANTLR.'
    )

command = [
    antlr_executable,
    '-Dlanguage=Python3',
    GRAMMAR_FILE,
    '-o',
    OUTPUT_DIR,
]

print('Ejecutando ANTLR...')
print(' '.join(command))
result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
if result.returncode != 0:
    print(result.stdout)
    print(result.stderr)
    sys.exit(result.returncode)

print('Generación completada. Archivos ubicados en outputgrammar/')
