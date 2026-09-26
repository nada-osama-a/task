from PySide6.QtWidgets import QApplication
from task.gui.window import Window

def main() -> None:
    app = QApplication()
    window = Window()
    app.exec()
