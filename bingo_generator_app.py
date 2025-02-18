import sys
from PyQt6.QtWidgets import QApplication
from bingo_ui import BingoGeneratorUI  # Импортируем класс UI
from bingo_logic import BingoGeneratorLogic # Импортируем логику

class BingoGeneratorApp(BingoGeneratorUI, BingoGeneratorLogic): # Множественное наследование для объединения UI и логики
    def __init__(self):
        super().__init__() # Вызываем конструкторы обоих классов (UI и Logic)
        self.setup_ui() # Инициализация UI из bingo_ui.py
        self.setup_logic() # Инициализация логики (подключение кнопок) из bingo_logic.py

# Блок if __name__ == '__main__': УДАЛЕН отсюда