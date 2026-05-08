import html
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QTextEdit, QPushButton, QLabel, QGroupBox,
                               QTabWidget, QTreeWidget, QTreeWidgetItem)
from PyQt6.QtGui import QFont
from .compiler_backend import parse_source

class CompiladorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('IDE Lenguaje - ANTLR4 + PyQt6')
        self.setGeometry(100, 100, 1100, 700)

        container = QWidget()
        self.setCentralWidget(container)
        main_layout = QHBoxLayout(container)

        left_panel = QVBoxLayout()
        right_panel = QVBoxLayout()

        left_panel.addWidget(QLabel('Editor de Código (Lenguaje):'))
        self.code_editor = QTextEdit()
        self.code_editor.setFont(QFont('Consolas', 12))
        self.code_editor.setPlaceholderText(
            'Lenguaje {\n    entero x;\n    x = 10 + 5;\n}')
        self.code_editor.setText(
            'Lenguaje {\n'
            '    entero a;\n'
            '    entero b;\n'
            '    a = 5;\n'
            '    b = a * (2 + 3);\n'
            '}')
        left_panel.addWidget(self.code_editor)

        button_bar = QHBoxLayout()
        self.compile_btn = QPushButton('Ejecutar Análisis (Compilar)')
        self.compile_btn.setMinimumHeight(40)
        self.compile_btn.setStyleSheet('background-color: #2b5797; color: white; font-weight: bold;')
        self.compile_btn.clicked.connect(self.analizar_codigo)
        button_bar.addWidget(self.compile_btn)

        self.example_btn = QPushButton('Cargar Ejercicio de Ejemplo')
        self.example_btn.setMinimumHeight(40)
        self.example_btn.setStyleSheet('background-color: #4a8f24; color: white; font-weight: bold;')
        self.example_btn.clicked.connect(self.cargar_ejemplo)
        button_bar.addWidget(self.example_btn)

        left_panel.addLayout(button_bar)

        self.results_tabs = QTabWidget()

        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setStyleSheet('background-color: #1e1e1e; color: #d4d4d4;')
        self.console_output.setFont(QFont('Consolas', 10))
        self.results_tabs.addTab(self.console_output, 'Consola')

        self.tree_view = QTreeWidget()
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setFont(QFont('Consolas', 10))
        self.results_tabs.addTab(self.tree_view, 'Árbol GUI')

        left_panel.addWidget(QLabel('Resultados:'))
        left_panel.addWidget(self.results_tabs)

        right_panel.addWidget(QLabel('Ejercicio de ejemplo'))
        self.example_info = QTextEdit()
        self.example_info.setReadOnly(True)
        self.example_info.setFont(QFont('Consolas', 10))
        self.example_info.setStyleSheet('background-color: #f5f5f5; color: #101010;')
        self.example_info.setHtml(
            '<b>Ejercicio:</b><br>'
            '1. Declara dos variables enteras.<br>'
            '2. Asigna un valor a la primera variable.<br>'
            '3. Asigna una expresión aritmética con paréntesis a la segunda.<br>'
            '4. Observa el árbol sintáctico generado.<br><br>'
            '<b>Ejemplo válido:</b><br>'
            'Lenguaje {<br>'
            '&nbsp;&nbsp;entero a;<br>'
            '&nbsp;&nbsp;entero b;<br>'
            '&nbsp;&nbsp;a = 5;<br>'
            '&nbsp;&nbsp;b = a * (2 + 3);<br>'
            '}'
        )
        right_panel.addWidget(self.example_info)

        # Grupo desplegable para opciones de ANTLR4
        self.antlr_group = QGroupBox('Opciones de ANTLR4')
        self.antlr_group.setCheckable(True)
        self.antlr_group.setChecked(False)  # Inicialmente cerrado
        self.antlr_group.setStyleSheet('QGroupBox { font-weight: bold; }')

        antlr_layout = QVBoxLayout()
        self.antlr_options = QTextEdit()
        self.antlr_options.setReadOnly(True)
        self.antlr_options.setFont(QFont('Consolas', 10))
        self.antlr_options.setStyleSheet('background-color: #ffffff; color: #101010;')
        self.antlr_options.setPlainText(
            'antlr4 -Dlanguage=Python3 grammar/compilador.g4 -o outputgrammar\n\n'
            'Opciones útiles:\n'
            '  -Dlanguage=<Python3|Java|CSharp|C++|JavaScript>  Define el lenguaje de salida\n'
            '  -o <directorio>                                 Directorio de salida\n'
            '  -lib <directorio>                                Ruta de importación de gramáticas\n'
            '  -package <nombre>                                Paquete de salida para Java/Python\n'
            '  -visitor                                         Genera clases visitor\n'
            '  -listener                                        Genera clases listener\n'
            '  -no-listener                                     Omite el listener\n'
            '  -no-visitor                                      Omite el visitor\n'
            '  -Xexact-output-dir                               Mantiene la salida exacta en el directorio indicado\n'
            '  -Werror                                          Trata advertencias como errores\n'
            '  -Xlog                                            Muestra logs adicionales\n'
            '  -Xmaxerrs <n>                                    Límite de errores\n'
            '  -encoding <codificación>                         Codificación de entrada\n'
            '  -help                                            Muestra ayuda completa\n'
            '  -version                                         Muestra la versión de ANTLR4\n\n'
            'GRUN - Herramienta de testing interactivo (Java):\n'
            '  Nota: GRUN es principalmente para testing con Java. Para Python,\n'
            '  esta interfaz proporciona funcionalidad similar.\n\n'
            '  Sintaxis: grun GrammarName startRuleName [options] [input-filename(s)]\n'
            '  Ejemplos:\n'
            '    grun compilador inicio -tokens              Muestra tokens\n'
            '    grun compilador inicio -tree                Muestra árbol de parseo\n'
            '    grun compilador inicio -gui                 Interfaz gráfica del árbol\n'
            '    echo "Lenguaje { entero a; }" | grun compilador inicio\n'
            '  Opciones grun:\n'
            '    -tokens          Muestra la secuencia de tokens\n'
            '    -tree            Muestra el árbol de parseo en texto\n'
            '    -gui             Muestra el árbol en interfaz gráfica\n'
            '    -ps file.ps      Genera árbol en PostScript\n'
            '    -trace           Muestra el trace del parser\n'
            '    -diagnostics     Muestra diagnósticos detallados\n'
            '    -SLL             Usa estrategia SLL en lugar de LL(*)\n'
            '    -encoding name   Codificación de entrada\n'
        )
        antlr_layout.addWidget(self.antlr_options)
        self.antlr_group.setLayout(antlr_layout)
        right_panel.addWidget(self.antlr_group)

        main_layout.addLayout(left_panel, 3)
        main_layout.addLayout(right_panel, 2)

    def cargar_ejemplo(self):
        ejemplo = (
            'Lenguaje {\n'
            '    entero a;\n'
            '    entero b;\n'
            '    a = 5;\n'
            '    b = a * (2 + 3);\n'
            '}'
        )
        self.code_editor.setText(ejemplo)
        self.console_output.clear()

    def analizar_codigo(self):
        codigo = self.code_editor.toPlainText()
        report = parse_source(codigo)
        self.console_output.clear()

        if report.success:
            self.console_output.append("<span style='color:green;'><b>✔ Análisis Exitoso</b></span>")
        else:
            self.console_output.append("<span style='color:red;'><b>✘ Errores encontrados</b></span>")

        # Mostrar tokens si existen
        self.tree_view.clear()

        if report.tokens:
            self.console_output.append("\n<b>Tokens reconocidos:</b>")
            for token in report.tokens:
                self.console_output.append(f"  {token}")

        if report.symbols:
            self.console_output.append("\n<b>Tabla de símbolos:</b>")
            for symbol in report.symbols:
                self.console_output.append(f"  {symbol}")

        if report.tree_text:
            self.console_output.append("\n<b>Árbol sintáctico (texto):</b>")
            safe_tree = html.escape(report.tree_text).replace('\n', '<br>')
            self.console_output.append(f"<span style='color:#d4d4d4; font-family: Consolas;'>{safe_tree}</span>")
        else:
            safe_output = html.escape(report.output).replace('\n', '<br>')
            self.console_output.append(f"<span style='color:#d4d4d4; font-family: Consolas;'>{safe_output}</span>")

        if report.tree:
            self._populate_tree_widget(report.tree)

    def _populate_tree_widget(self, tree_root):
        self.tree_view.clear()
        root_item = QTreeWidgetItem([self._format_tree_node(tree_root)])
        self.tree_view.addTopLevelItem(root_item)
        self._add_children_to_item(tree_root, root_item)
        self.tree_view.expandToDepth(1)

    def _format_tree_node(self, node):
        if hasattr(node, 'getChildCount') and node.getChildCount() == 0:
            return node.getText()
        label = node.__class__.__name__
        if label.endswith('Context'):
            label = label[:-7]
        return label

    def _add_children_to_item(self, node, item):
        if not hasattr(node, 'getChildCount'):
            return
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_item = QTreeWidgetItem([self._format_tree_node(child)])
            item.addChild(child_item)
            self._add_children_to_item(child, child_item)


def run_app():
    import sys
    app = QApplication(sys.argv)
    window = CompiladorApp()
    window.show()
    sys.exit(app.exec())
