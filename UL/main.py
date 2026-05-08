import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from PyQt6.QtWidgets import QApplication
from UL.ui import CompiladorApp


def main():
    app = QApplication(sys.argv)
    window = CompiladorApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
