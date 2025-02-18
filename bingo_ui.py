from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QTextEdit, QPushButton,
                             QListWidget, QGridLayout, QMessageBox, QSpinBox)
from PyQt6.QtCore import Qt, QSize  # Импортируем QSize


class BingoGeneratorUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор Бинго")
        self.setGeometry(100, 100, 800, 600)

        self.themes = []
        self.bingo_squares = []
        self.bingo_buttons = []
        self.grid_size = 5

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout(self.central_widget)

        # --- Левая часть (Темы) ---
        self.themes_layout = QVBoxLayout()
        self.themes_label = QLabel("Темы для бинго (по одной на строку):")
        self.themes_layout.addWidget(self.themes_label)

        self.theme_input = QTextEdit()
        self.themes_layout.addWidget(self.theme_input)

        self.add_theme_button = QPushButton("Добавить темы")
        self.themes_layout.addWidget(self.add_theme_button)

        self.theme_list_widget = QListWidget()
        self.themes_layout.addWidget(self.theme_list_widget)

        self.main_layout.addLayout(self.themes_layout)

        # --- Правая часть (Бинго) ---
        self.bingo_layout = QVBoxLayout()
        self.bingo_label = QLabel("Бинго:")
        self.bingo_layout.addWidget(self.bingo_label)

        # --- Выбор размера сетки ---
        self.grid_size_layout = QHBoxLayout()
        self.grid_size_label = QLabel("Размер сетки:")
        self.grid_size_layout.addWidget(self.grid_size_label)
        self.grid_size_spinbox = QSpinBox()
        self.grid_size_spinbox.setMinimum(3)
        self.grid_size_spinbox.setMaximum(7)
        self.grid_size_spinbox.setValue(self.grid_size)
        self.grid_size_layout.addWidget(self.grid_size_spinbox)
        self.bingo_layout.addLayout(self.grid_size_layout)

        self.bingo_grid_layout = QGridLayout()
        self.bingo_layout.addLayout(self.bingo_grid_layout)

        self.generate_bingo_button = QPushButton("Сгенерировать бинго")
        self.bingo_layout.addWidget(self.generate_bingo_button)

        self.export_button = QPushButton("Экспортировать в картинку")
        self.bingo_layout.addWidget(self.export_button)

        self.main_layout.addLayout(self.bingo_layout)

    def setup_ui(self):
        self.show()