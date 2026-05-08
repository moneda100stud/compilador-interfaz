# Ejemplo de uso de GRUN con ANTLR4 (para Java)
# Este script muestra cómo usar grun si generas archivos Java en lugar de Python

# 1. Generar archivos Java con ANTLR4:
# antlr4 -Dlanguage=Java grammar/compilador.g4 -o outputgrammar_java/

# 2. Compilar los archivos Java:
# javac -cp "path/to/antlr4.jar:outputgrammar_java" outputgrammar_java/*.java

# 3. Usar grun para testing interactivo:
# echo "Lenguaje { entero a; a = 5; }" | grun compilador inicio -tokens
# echo "Lenguaje { entero a; a = 5; }" | grun compilador inicio -tree
# echo "Lenguaje { entero a; a = 5; }" | grun compilador inicio -gui

# Nota: Para Python, usa la interfaz gráfica que proporciona funcionalidad equivalente
# python run.py