import html
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QTextEdit, QPushButton, QLabel, QGroupBox,
                               QTabWidget, QTreeWidget, QTreeWidgetItem, QComboBox, QStyleFactory)
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
            'Lenguaje {\n    entero x;\n    si (x > 0) { ... }\n}')
        self.code_editor.setText(
            'Lenguaje {\n'
            '    entero a;\n'
            '    entero b;\n'
            '    a = 5;\n'
            '    mientras (a > 0) {\n'
            '        a = a - 1;\n'
            '    }\n'
            '    si (a == 0) {\n'
            '        b = 10;\n'
            '    }\n'
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

        # Nueva sección de resumen (después del árbol/pestañas)
        left_panel.addWidget(QLabel('Resumen de Ejecución:'))
        self.summary_output = QTextEdit()
        self.summary_output.setReadOnly(True)
        self.summary_output.setStyleSheet('background-color: #252526; color: #00ff00; border: 1px solid #333;')
        self.summary_output.setFont(QFont('Consolas', 10))
        left_panel.addWidget(self.summary_output)

        # Sección de Cambio de Temas
        self.theme_group = QGroupBox('Apariencia del Sistema')
        theme_layout = QHBoxLayout()
        self.theme_combo = QComboBox()
        # Obtener todos los temas disponibles en el sistema (Fusion, Windows, etc.)
        available_styles = QStyleFactory.keys()
        self.theme_combo.addItems(available_styles)
        
        # Agregar temas personalizados
        self.custom_themes = {
            "Neon Personalizado": self._get_neon_qss(),
            "Estilo Plasma": self._get_plasma_qss(),
            "Material Neon": self._get_material_neon_qss(),
            "Futurista QSS": self._get_futuristic_qss()
        }
        self.theme_combo.addItems(self.custom_themes.keys())
        
        self.theme_combo.currentTextChanged.connect(self.cambiar_tema)
        theme_layout.addWidget(QLabel('Tema:'))
        theme_layout.addWidget(self.theme_combo)
        self.theme_group.setLayout(theme_layout)
        right_panel.addWidget(self.theme_group)

        right_panel.addWidget(QLabel('Ejercicio de ejemplo'))
        self.example_info = QTextEdit()
        self.example_info.setReadOnly(True)
        self.example_info.setFont(QFont('Consolas', 10))
        self.example_info.setStyleSheet('background-color: #f5f5f5; color: #101010;')
        self.example_info.setHtml(
            '<b>Ejercicio:</b><br>'
            '1. Declara dos variables enteras.<br>'
            '2. Asigna un valor a la primera variable.<br>'
            '3. Crea un ciclo <b>mientras</b> que reduzca el valor.<br>'
            '4. Usa un condicional <b>si</b> para verificar el resultado.<br>'
            '5. Observa el árbol sintáctico generado.<br><br>'
            '<b>Ejemplo válido:</b><br>'
            'Lenguaje {<br>'
            '&nbsp;&nbsp;entero a;<br>'
            '&nbsp;&nbsp;a = 5;<br>'
            '&nbsp;&nbsp;mientras (a > 0) {<br>'
            '&nbsp;&nbsp;&nbsp;&nbsp;a = a - 1;<br>'
            '&nbsp;&nbsp;}<br>'
            '&nbsp;&nbsp;si (a == 0) {<br>'
            '&nbsp;&nbsp;&nbsp;&nbsp;entero b;<br>'
            '&nbsp;&nbsp;&nbsp;&nbsp;b = 1;<br>'
            '&nbsp;&nbsp;}<br>'
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
            '    a = 10;\n'
            '    mientras (a > 0) {\n'
            '        a = a - 1;\n'
            '    }\n'
            '    si (a == 0) {\n'
            '        b = 100;\n'
            '    } sino {\n'
            '        b = 0;\n'
            '    }\n'
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

        # Mostrar resultados reales de las variables
        self.tree_view.clear()

        if report.values:
            self.console_output.append("\n<b>Valores finales de variables:</b>")
            for name, value in report.values.items():
                self.console_output.append(f"  {name} = {value}")
        elif report.symbols:
            self.console_output.append("\n<b>Variables declaradas:</b>")
            for symbol in report.symbols:
                self.console_output.append(f"  {symbol}")
        else:
            safe_output = html.escape(report.output).replace('\n', '<br>')
            self.console_output.append(f"<span style='color:#d4d4d4; font-family: Consolas;'>{safe_output}</span>")

        if report.tree:
            self._populate_tree_widget(report.tree)
        # Mostrar la sección de resumen adaptada
        self._mostrar_resumen_final(report)

    def cambiar_tema(self, nombre_tema):
        """Cambia el estilo de la aplicación dinámicamente"""
        if nombre_tema in self.custom_themes:
            # Aplicar QSS personalizado sobre el estilo Fusion para consistencia
            QApplication.setStyle("Fusion")
            self.setStyleSheet(self.custom_themes[nombre_tema])
        else:
            # Limpiar estilos personalizados y usar tema del sistema
            self.setStyleSheet("")
            QApplication.setStyle(nombre_tema)

    def _get_neon_qss(self):
        return """
            QMainWindow { background-color: #050505; }
            QLabel { color: #ff00ff; font-weight: bold; }
            QTextEdit { background-color: #121212; color: #00ffff; border: 2px solid #ff00ff; border-radius: 5px; }
            QPushButton { background-color: #121212; color: #ff00ff; border: 2px solid #ff00ff; border-radius: 10px; padding: 5px; }
            QPushButton:hover { background-color: #ff00ff; color: black; }
            QGroupBox { color: #00ffff; border: 1px solid #00ffff; margin-top: 10px; }
        """

    def _get_plasma_qss(self):
        return """
            QMainWindow { background-color: #eff0f1; }
            QWidget { color: #232629; font-family: 'Segoe UI'; }
            QTextEdit { background-color: #ffffff; border: 1px solid #babdbf; border-radius: 3px; color: #232629; }
            QPushButton { background-color: #3daee9; color: white; border-radius: 4px; padding: 6px; border: none; }
            QPushButton:hover { background-color: #2980b9; }
            QTabWidget::pane { border: 1px solid #babdbf; }
            QTabBar::tab { background: #d1d4d6; padding: 8px; margin-right: 2px; }
            QTabBar::tab:selected { background: #ffffff; border-bottom: 2px solid #3daee9; }
        """

    def _get_material_neon_qss(self):
        return """
            QMainWindow { background-color: #212121; }
            QLabel { color: #bb86fc; }
            QTextEdit { background-color: #2c2c2c; color: #e0e0e0; border-radius: 4px; border-bottom: 2px solid #03dac6; }
            QPushButton { background-color: #6200ee; color: #03dac6; border-radius: 8px; font-weight: bold; padding: 8px; }
            QPushButton#compile_btn { background-color: #3700b3; border: 1px solid #03dac6; }
            QGroupBox { border: 1px solid #444; color: #03dac6; border-radius: 10px; padding-top: 15px; }
        """

    def _get_futuristic_qss(self):
        return """
            QMainWindow { background-color: #0d0d0d; }
            QWidget { color: #e0e0e0; }
            QTextEdit { background-color: #1a1a1a; color: #00ffcc; border: 1px solid #00ffcc; border-radius: 2px; }
            QPushButton { 
                background-color: #1a1a1a; 
                color: #00ffcc; 
                border: 1px solid #00ffcc; 
                padding: 10px;
                font-family: 'Consolas';
            }
            QPushButton:hover { 
                background-color: #00ffcc; 
                color: #0d0d0d;
                border: 1px solid #ffffff;
            }
            QTreeWidget { background-color: #1a1a1a; border: 1px solid #00ffcc; color: #00ffcc; }
            QHeaderView::section { background-color: #333; color: #00ffcc; }
        """

    def ejecutar_logica(self, valor=None, funcion=None, *args, **kwargs):
        """
        Devuelve el resultado de funcion(*args, **kwargs) si existe,
        de lo contrario devuelve valor.
        """
        if funcion is not None:
            if args or kwargs:
                return funcion(*args, **kwargs)
            if valor is not None:
                try:
                    return funcion(valor)
                except TypeError:
                    return funcion()
            return funcion()
        return valor

    def ejecutar_y_formatear(self, *f_args, formato="{}", **f_kwargs):
        """Envuélve el resultado de la lógica y lo formatea para la interfaz gráfica"""
        valor = self.ejecutar_logica(*f_args, **f_kwargs)
        return formato.format(valor)

    def _mostrar_resumen_final(self, report):
        self.summary_output.clear()

        # Calculamos el conteo de tokens usando la lógica de ejecución flexible
        token_count = self.ejecutar_y_formatear(
            funcion=lambda r: len(r.tokens),
            r=report,
            formato="{}"
        )

        self._append_seccion_ui("RESULTADO PRINCIPAL (Tokens)", token_count)

        # Requisito: Mostrar el código del árbol sintáctico en la consola
        if report.tree_text:
            self.console_output.append("\n<b>Representación del Árbol (Texto):</b>")
            self.console_output.append(f"<code style='color:#ce9178;'>{html.escape(report.tree_text)}</code>")

        stats = (
            f"Tokens totales: {token_count}\n"
            f"Variables: {len(report.values)}\n"
            f"Declaraciones: {len(report.symbols)}\n"
            f"Errores: {len(report.errors)}"
        )
        self._append_seccion_ui("ESTADÍSTICAS", stats)

    def _append_seccion_ui(self, titulo, texto):
        self.summary_output.append(f"--- {titulo} ---")
        self.summary_output.append(texto)
        self.summary_output.append("-" * (len(titulo) + 8) + "\n")


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

if __name__ == "__main__":
    run_app()
