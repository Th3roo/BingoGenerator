import sys
from PyQt6.QtWidgets import QApplication
from bingo_generator_app import BingoGeneratorApp  # Импорт класса BingoGeneratorApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bingo_app = BingoGeneratorApp()
    sys.exit(app.exec())