#
# Purpur Tentakel
# Cocking Book
# 18.04.2023
#
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, QMessageBox
from PyQt5.QtWidgets import QLineEdit, QPushButton, QListWidget, QListWidgetItem, QTextEdit, QLabel
from UI.RawTypesWindow import RawTypesWindow

from database import select as s


class Colors:
    grey: QColor = QColor(0, 0, 0, 100)
    white: QColor = QColor(255, 255, 255, 255)


class RawTypeItem(QListWidgetItem):
    def __init__(self, ID: int, entry: str, selected: bool) -> None:
        super().__init__()
        self.ID = ID
        self.entry = entry
        self.selected = selected

        self.setText(entry)
        self.set_selected(self.selected)

    def toggle_selected(self) -> None:
        self.set_selected(not self.selected)

    def set_selected(self, selected: bool) -> None:
        self.selected = selected
        if self.selected:
            self.setBackground(Colors.grey)
        else:
            self.setBackground(Colors.white)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._init_UI()
        self._ini_layout()

        self._raw_types_window: RawTypesWindow | None = None

        self._load_raw_types()

    def _init_UI(self) -> None:
        self.setWindowTitle("Cooking Book - Purpur Tentakel")

        # left
        self._recipe_label: QLabel = QLabel("recipes:")
        self._recipe_search: QLineEdit = QLineEdit()
        self._recipe_search.setPlaceholderText("recipe search")
        self._clear_recipe_search: QPushButton = QPushButton("clear")
        self._delete_recipe_btn: QPushButton = QPushButton("delete")
        self._cancel_recipe_btn: QPushButton = QPushButton("cancel")
        self._add_recipe_btn: QPushButton = QPushButton("add")
        self._recipes: QListWidget = QListWidget()

        # middle
        self._title_label: QLabel = QLabel("title:")
        self._title: QLineEdit = QLineEdit()
        self._title.setPlaceholderText("title")
        self._save_title_btn: QPushButton = QPushButton("save")
        self._types_label: QLabel = QLabel("types:")
        self._types_search: QLineEdit = QLineEdit()
        self._types_search.setPlaceholderText("types search")
        self._types_search.textChanged.connect(self._chanced_text_type_search)
        self._clear_types_search: QPushButton = QPushButton("clear")
        self._clear_types_search.clicked.connect(self._clicked_clear_type_search)
        self._clear_types_search.setEnabled(False)
        self._types_button: QPushButton = QPushButton("types")
        self._types_button.clicked.connect(self._set_raw_type_window)
        self._types: QListWidget = QListWidget()

        self._ingredient_label: QLabel = QLabel("ingredients:")
        self._amount: QLineEdit = QLineEdit()
        self._amount.setPlaceholderText("amount")
        self._unit: QLineEdit = QLineEdit()
        self._unit.setPlaceholderText("unit")
        self._ingredient: QLineEdit = QLineEdit()
        self._ingredient.setPlaceholderText("ingredient")
        self._delete_ingredient_btn: QPushButton = QPushButton("delete")
        self._cancel_ingredient_btn: QPushButton = QPushButton("cancel")
        self._add_ingredient_btn: QPushButton = QPushButton("add")
        self._ingredients: QListWidget = QListWidget()

        # right
        self._recipe_entry_label: QLabel = QLabel("recipe:")
        self._save_recipe_text_btn: QPushButton = QPushButton("save")
        self._recipe_entry: QTextEdit = QTextEdit()
        self._recipe_entry.setPlaceholderText("enter the recipe description")

        self._global_save_btn: QPushButton = QPushButton("save all")

    def _ini_layout(self) -> None:
        # left
        left_v_box: QVBoxLayout = QVBoxLayout()
        left_v_box.addWidget(self._recipe_label)

        left_h_box_1: QHBoxLayout = QHBoxLayout()
        left_h_box_1.addWidget(self._recipe_search)
        left_h_box_1.addWidget(self._clear_recipe_search)

        left_v_box.addLayout(left_h_box_1)

        left_h_box_2: QHBoxLayout = QHBoxLayout()
        left_h_box_2.addWidget(self._delete_recipe_btn)
        left_h_box_2.addWidget(self._cancel_recipe_btn)
        left_h_box_2.addWidget(self._add_recipe_btn)

        left_v_box.addLayout(left_h_box_2)
        left_v_box.addWidget(self._recipes)

        # mid
        mid_v_box: QVBoxLayout = QVBoxLayout()
        mid_v_box.addWidget(self._title_label)

        mid_h_box_1: QHBoxLayout = QHBoxLayout()
        mid_h_box_1.addWidget(self._title)
        mid_h_box_1.addWidget(self._save_title_btn)

        mid_v_box.addLayout(mid_h_box_1)
        mid_v_box.addWidget(self._types_label)

        mid_h_box_2: QHBoxLayout = QHBoxLayout()
        mid_h_box_2.addWidget(self._types_search)
        mid_h_box_2.addWidget(self._clear_types_search)
        mid_h_box_2.addWidget(self._types_button)

        mid_v_box.addLayout(mid_h_box_2)
        mid_v_box.addWidget(self._types)
        mid_v_box.addWidget(self._ingredient_label)

        mid_bottom_grid: QGridLayout = QGridLayout()
        mid_bottom_grid.addWidget(self._amount, 0, 0)
        mid_bottom_grid.addWidget(self._unit, 0, 1)
        mid_bottom_grid.addWidget(self._ingredient, 0, 2)
        mid_bottom_grid.addWidget(self._delete_ingredient_btn, 1, 0)
        mid_bottom_grid.addWidget(self._cancel_ingredient_btn, 1, 1)
        mid_bottom_grid.addWidget(self._add_ingredient_btn, 1, 2)

        mid_v_box.addLayout(mid_bottom_grid)
        mid_v_box.addWidget(self._ingredients)

        # right
        right_v_box: QVBoxLayout = QVBoxLayout()

        right_h_box: QHBoxLayout = QHBoxLayout()
        right_h_box.addWidget(self._recipe_entry_label)
        right_h_box.addStretch()
        right_h_box.addWidget(self._save_recipe_text_btn)

        right_v_box.addLayout(right_h_box)
        right_v_box.addWidget(self._recipe_entry)
        right_v_box.addWidget(self._global_save_btn)

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

    def _load_raw_types(self) -> None:
        result = s.select.select_all_raw_types()
        if not result.valid:
            self._display_message(result.entry)
            return

        self._types.clear()
        for ID, entry in result.entry:
            item: RawTypeItem = RawTypeItem(ID, entry, False)
            self._types.addItem(item)

    def _clicked_clear_type_search(self) -> None:
        self._types_search.clear()

    def _chanced_text_type_search(self) -> None:
        text: str = self._types_search.text().strip()
        self._clear_types_search.setEnabled(len(text) != 0)
        self._display_raw_types()

    def _display_raw_types(self) -> None:
        pass

    def _set_raw_type_window(self) -> None:
        self.window().setEnabled(False)
        self._raw_types_window = RawTypesWindow(self._raw_types_callback)

    def _raw_types_callback(self) -> None:
        self._load_raw_types()
        self._types_search.clear()
        self._raw_types_window = None
        self.window().setEnabled(True)

    @staticmethod
    def _display_message(message: str) -> None:
        msg: QMessageBox = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        x = msg.exec_()
