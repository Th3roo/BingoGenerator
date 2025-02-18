import random
from PyQt6.QtWidgets import QMessageBox, QFileDialog, QLabel, QWidget, QGridLayout, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtCore import Qt, QSize


class BingoGeneratorLogic:
    def __init__(self):
        self.original_button_styles = {} # Словарь для хранения оригинальных стилей кнопок

    def setup_logic(self):
        self.add_theme_button.clicked.connect(self.add_theme)
        self.generate_bingo_button.clicked.connect(self.generate_bingo)
        self.export_button.clicked.connect(self.export_to_image)

    def add_theme(self):
        themes_text = self.theme_input.toPlainText()
        if themes_text:
            new_themes = themes_text.strip().split('\n')
            added_count = 0
            for theme_text in new_themes:
                theme_text = theme_text.strip()
                if theme_text and theme_text not in self.themes:
                    self.themes.append(theme_text)
                    self.theme_list_widget.addItem(theme_text)
                    added_count += 1

            if added_count > 0:
                self.theme_input.clear()
            else:
                QMessageBox.warning(self, "Внимание", "Нет новых тем для добавления или все темы уже в списке!")
        else:
            QMessageBox.warning(self, "Внимание", "Введите темы!")


    def generate_bingo(self):
        if not self.themes:
            QMessageBox.warning(self, "Внимание", "Добавьте темы для бинго!")
            return

        grid_size = self.grid_size_spinbox.value()
        num_squares = grid_size * grid_size

        if len(self.themes) < num_squares:
            QMessageBox.warning(self, "Внимание", f"Добавьте больше тем (минимум {num_squares} для бинго {grid_size}x{grid_size})!")
            return

        # Очищаем предыдущее бинго
        for button in self.bingo_buttons:
            button.deleteLater()
        self.bingo_buttons = []
        self.bingo_squares = []
        self.original_button_styles = {} # Очищаем словарь стилей при новой генерации

        selected_themes = random.sample(self.themes, num_squares)

        row = 0
        col = 0
        for theme in selected_themes:
            button = QPushButton()
            button.setFixedSize(QSize(100, 100))
            
            # Создаем QLabel для текста с переносом
            label = QLabel(theme)
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setFixedSize(90, 90)  # Фиксированный размер для label
            
            # Создаем layout для кнопки
            button_layout = QVBoxLayout(button)
            button_layout.addWidget(label)
            button_layout.setContentsMargins(5, 5, 5, 5)
            button_layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetFixedSize)  # Фиксируем размер layout
            
            button.setStyleSheet("""
                QPushButton {
                    text-align: center;
                    min-height: 100px;
                    max-height: 100px;
                }
            """)
            
            self.original_button_styles[button] = button.styleSheet()
            button.setCheckable(True)
            button.clicked.connect(lambda checked, btn=button: self.mark_bingo_square(btn, checked))
            self.bingo_grid_layout.addWidget(button, row, col)
            self.bingo_buttons.append(button)
            self.bingo_squares.append(theme)

            col += 1
            if col >= grid_size:
                col = 0
                row += 1

    def mark_bingo_square(self, button, checked): # Добавили параметр checked
        if checked: # Если кнопка была нажата и стала "checked" (зачеркнута)
            # Используем HTML-подобное форматирование для добавления "крестика" (зачеркивания)
            button.setStyleSheet(f"""
                QPushButton {{
                    {self.original_button_styles[button]} /* Восстанавливаем оригинальный стиль */
                    color: red; /* Цвет текста красный */
                    text-decoration: line-through; /* Зачеркивание текста */
                }}
            """)
        else: # Если кнопка была отжата и стала "unchecked" (вернули в исходное состояние)
            button.setStyleSheet(self.original_button_styles[button]) # Восстанавливаем оригинальный стиль


    def export_to_image(self):
        if not self.bingo_buttons:
            QMessageBox.warning(self, "Внимание", "Сначала сгенерируйте бинго!")
            return

        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить бинго как изображение", "", "PNG Files (*.png);;All Files (*)")

        if file_name:
            bingo_widget = QWidget()
            bingo_grid_export_layout = QGridLayout(bingo_widget)

            row = 0
            col = 0
            grid_size = self.grid_size_spinbox.value()
            
            for i, theme in enumerate(self.bingo_squares):
                export_button = QPushButton()
                export_button.setFixedSize(QSize(100, 100))
                
                # Создаем QLabel для текста с переносом
                label = QLabel(theme)
                label.setWordWrap(True)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setFixedSize(90, 90)
                
                # Создаем layout для кнопки
                button_layout = QVBoxLayout(export_button)
                button_layout.addWidget(label)
                button_layout.setContentsMargins(5, 5, 5, 5)
                button_layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetFixedSize)
                
                if self.bingo_buttons[i].isChecked():
                    export_button.setStyleSheet("""
                        QPushButton {
                            text-align: center;
                            min-height: 100px;
                            max-height: 100px;
                            min-width: 100px;
                            max-width: 100px;
                            color: red;
                            text-decoration: line-through;
                        }
                    """)
                else:
                    export_button.setStyleSheet("""
                        QPushButton {
                            text-align: center;
                            min-height: 100px;
                            max-height: 100px;
                            min-width: 100px;
                            max-width: 100px;
                        }
                    """)

                bingo_grid_export_layout.addWidget(export_button, row, col)
                
                col += 1
                if col >= grid_size:
                    col = 0
                    row += 1

            bingo_widget.adjustSize()
            pixmap = bingo_widget.grab()
            pixmap.save(file_name, "PNG")
            QMessageBox.information(self, "Успех", "Бинго экспортировано в изображение!")