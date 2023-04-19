#
# Purpur Tentakel
# Cocking Book
# 18.04.2023
#

from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from PyQt5.QtWidgets import QLineEdit, QPushButton, QListWidget, QListWidgetItem, QTextEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._init_UI()
        self._ini_layout()

    def _init_UI(self) -> None:
        self.setWindowTitle("Cooking Book - Purpur Tentakel")

        # left
        self._recipe_search: QLineEdit = QLineEdit()
        self._recipe_search.setPlaceholderText("recipe search")
        self._recipe_label: QLabel = QLabel("recipes:")
        self._recipes: QListWidget = QListWidget()

        # middle
        self._title: QLineEdit = QLineEdit()
        self._title.setPlaceholderText("title")
        self._title_label: QLabel = QLabel("title:")
        self._types_button: QPushButton = QPushButton("types")
        self._types_search: QLineEdit = QLineEdit()
        self._types_search.setPlaceholderText("types search")
        self._types_label: QLabel = QLabel("types:")
        self._types: QListWidget = QListWidget()

        self._amount: QLineEdit = QLineEdit()
        self._amount.setPlaceholderText("amount")
        self._unit: QLineEdit = QLineEdit()
        self._unit.setPlaceholderText("unit")
        self._ingredient: QLineEdit = QLineEdit()
        self._ingredient.setPlaceholderText("ingredient")

        self._ingredient_label: QLabel = QLabel("ingredients:")
        self._ingredients: QListWidget = QListWidget()

        # right
        self._recipe_entry: QTextEdit = QTextEdit()
        self._recipe_entry.setPlaceholderText("enter the recipe description")
        self._recipe_entry_label: QLabel = QLabel("recipe:")

        self._save: QPushButton() = QPushButton("save")

    def _ini_layout(self) -> None:
        # left
        left_v_box: QVBoxLayout = QVBoxLayout()
        left_v_box.addWidget(self._recipe_label)
        left_v_box.addWidget(self._recipe_search)
        left_v_box.addWidget(self._recipes)

        # mid
        mid_v_box: QVBoxLayout = QVBoxLayout()
        mid_v_box.addWidget(self._title_label)
        mid_v_box.addWidget(self._title)
        mid_v_box.addWidget(self._types_label)

        mid_top_grid: QGridLayout = QGridLayout()
        mid_top_grid.addWidget(self._types_search, 0, 0, 0, 8)
        mid_top_grid.addWidget(self._types_button, 0, 8)

        mid_v_box.addLayout(mid_top_grid)
        mid_v_box.addWidget(self._types)
        mid_v_box.addWidget(self._ingredient_label)

        mid_bottom_grid: QGridLayout = QGridLayout()
        mid_bottom_grid.addWidget(self._amount, 0, 0)
        mid_bottom_grid.addWidget(self._unit, 0, 1)
        mid_bottom_grid.addWidget(self._ingredient, 0, 2)

        mid_v_box.addLayout(mid_bottom_grid)
        mid_v_box.addWidget(self._ingredients)

        # right
        right_v_box: QVBoxLayout = QVBoxLayout()
        right_v_box.addWidget(self._recipe_entry_label)
        right_v_box.addWidget(self._recipe_entry)
        right_v_box.addWidget(self._save)

        # global
        global_h_box: QVBoxLayout = QHBoxLayout()
        global_h_box.addLayout(left_v_box)
        global_h_box.addLayout(mid_v_box)
        global_h_box.addLayout(right_v_box)

        widget: QWidget = QWidget()
        widget.setLayout(global_h_box)
        self.setCentralWidget(widget)

        self.setMinimumSize(1280, 720)
        self.showMaximized()
        self.show()
