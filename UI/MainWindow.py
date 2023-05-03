#
# Purpur Tentakel
# Cocking Book
# 18.04.2023
#
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, QMessageBox
from PyQt5.QtWidgets import QLineEdit, QPushButton, QListWidget, QListWidgetItem, QTextEdit, QLabel
from UI.RawTypesWindow import RawTypesWindow

from database import add as a
from database import select as s
from database import update as u
from database import delete as d


class Colors:
    grey: QColor = QColor(0, 0, 0, 50)
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


class IngredientItem(QListWidgetItem):
    def __init__(self, ID: int, amount: str, unit: str, ingredient: str) -> None:
        super().__init__()

        self.ID: int = ID
        self.amount: str = amount
        self.unit: str = unit
        self.ingredient: str = ingredient

    def _set_text(self) -> None:
        text: str = f"{self.amount}"
        if len(self.unit) != 0:
            text += self.unit
        text += f" {self.ingredient}"

        self.setText(text)

    def update(self, amount: str, unit: str, ingredient: str) -> None:
        self.amount = amount
        self.unit = unit
        self.ingredient = ingredient
        self._set_text()


class RecipeItem(QListWidgetItem):
    def __init__(self, ID: int, title: str, description: str) -> None:
        super().__init__()
        self.ID: int = ID
        self.title: str = title
        self.description: str = description

        self.set_title(self.title)

    def set_title(self, new_title: str) -> None:
        self.title = new_title
        self.setText(self.title)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._init_UI()
        self._ini_layout()
        self._init_data()

        self._raw_types_window: RawTypesWindow | None = None

    # init
    def _init_UI(self) -> None:
        self.setWindowTitle("Cooking Book - Purpur Tentakel")

        # left
        self._recipe_label: QLabel = QLabel("recipes:")
        self._recipe_search_le: QLineEdit = QLineEdit()
        self._recipe_search_le.setPlaceholderText("recipe search")
        self._recipe_search_le.textChanged.connect(self._chanced_recipe_search)
        self._clear_recipe_search_btn: QPushButton = QPushButton("clear")
        self._clear_recipe_search_btn.setEnabled(False)
        self._clear_recipe_search_btn.clicked.connect(self._clear_recipe_search)
        self._delete_recipe_btn: QPushButton = QPushButton("delete")
        self._delete_recipe_btn.clicked.connect(self._delete_recipe)
        self._add_recipe_btn: QPushButton = QPushButton("add")
        self._add_recipe_btn.clicked.connect(self._add_recipe)
        self._recipes_list: QListWidget = QListWidget()
        self._recipes_list.currentItemChanged.connect(self._chanced_recipe)

        # middle
        self._title_label: QLabel = QLabel("title:")
        self._title_le: QLineEdit = QLineEdit()
        self._title_le.setPlaceholderText("title")
        self._title_le.textChanged.connect(self._chanced_title)
        self._title_le.returnPressed.connect(self._clicked_save_title)
        self._save_title_btn: QPushButton = QPushButton("save")
        self._save_title_btn.setEnabled(False)
        self._save_title_btn.clicked.connect(self._clicked_save_title)
        self._types_label: QLabel = QLabel("types:")
        self._types_search_le: QLineEdit = QLineEdit()
        self._types_search_le.setPlaceholderText("types search")
        self._types_search_le.textChanged.connect(self._chanced_text_type_search)
        self._clear_types_search_btn: QPushButton = QPushButton("clear")
        self._clear_types_search_btn.clicked.connect(self._clear_type_search)
        self._clear_types_search_btn.setEnabled(False)
        self._types_btn: QPushButton = QPushButton("types")
        self._types_btn.clicked.connect(self._set_raw_type_window)
        self._types_list: QListWidget = QListWidget()
        self._types_list.itemClicked.connect(self._clicked_type)

        self._ingredient_label: QLabel = QLabel("ingredients:")
        self._amount_le: QLineEdit = QLineEdit()
        self._amount_le.setPlaceholderText("amount")
        self._amount_le.textChanged.connect(self._chanced_ingredient_le)
        self._unit_le: QLineEdit = QLineEdit()
        self._unit_le.setPlaceholderText("unit")
        self._unit_le.textChanged.connect(self._chanced_ingredient_le)
        self._ingredient_le: QLineEdit = QLineEdit()
        self._ingredient_le.setPlaceholderText("ingredient")
        self._ingredient_le.textChanged.connect(self._chanced_ingredient_le)
        self._delete_ingredient_btn: QPushButton = QPushButton("delete")
        self._delete_ingredient_btn.setEnabled(False)
        self._cancel_ingredient_btn: QPushButton = QPushButton("cancel")
        self._cancel_ingredient_btn.clicked.connect(self._clear_cancel_ingredients)
        self._add_ingredient_btn: QPushButton = QPushButton("commit")
        self._add_ingredient_btn.setEnabled(False)
        self._ingredients_list: QListWidget = QListWidget()

        # right
        self._recipe_entry_label: QLabel = QLabel("recipe:")
        self._save_recipe_text_btn: QPushButton = QPushButton("save")
        self._save_recipe_text_btn.setEnabled(False)
        self._save_recipe_text_btn.clicked.connect(self._clicked_save_description)
        self._recipe_entry_te: QTextEdit = QTextEdit()
        self._recipe_entry_te.setPlaceholderText("enter the recipe description")
        self._recipe_entry_te.textChanged.connect(self._chanced_description)

        self._global_save_btn: QPushButton = QPushButton("save all")
        self._global_save_btn.setEnabled(False)
        self._export_btn: QPushButton = QPushButton("export")

    def _ini_layout(self) -> None:
        # left
        left_v_box: QVBoxLayout = QVBoxLayout()
        left_v_box.addWidget(self._recipe_label)

        left_h_box_1: QHBoxLayout = QHBoxLayout()
        left_h_box_1.addWidget(self._recipe_search_le)
        left_h_box_1.addWidget(self._clear_recipe_search_btn)

        left_v_box.addLayout(left_h_box_1)

        left_h_box_2: QHBoxLayout = QHBoxLayout()
        left_h_box_2.addWidget(self._delete_recipe_btn)
        left_h_box_2.addWidget(self._add_recipe_btn)

        left_v_box.addLayout(left_h_box_2)
        left_v_box.addWidget(self._recipes_list)

        # mid
        mid_v_box: QVBoxLayout = QVBoxLayout()
        mid_v_box.addWidget(self._title_label)

        mid_h_box_1: QHBoxLayout = QHBoxLayout()
        mid_h_box_1.addWidget(self._title_le)
        mid_h_box_1.addWidget(self._save_title_btn)

        mid_v_box.addLayout(mid_h_box_1)
        mid_v_box.addWidget(self._types_label)

        mid_h_box_2: QHBoxLayout = QHBoxLayout()
        mid_h_box_2.addWidget(self._types_search_le)
        mid_h_box_2.addWidget(self._clear_types_search_btn)
        mid_h_box_2.addWidget(self._types_btn)

        mid_v_box.addLayout(mid_h_box_2)
        mid_v_box.addWidget(self._types_list)
        mid_v_box.addWidget(self._ingredient_label)

        mid_bottom_grid: QGridLayout = QGridLayout()
        mid_bottom_grid.addWidget(self._amount_le, 0, 0)
        mid_bottom_grid.addWidget(self._unit_le, 0, 1)
        mid_bottom_grid.addWidget(self._ingredient_le, 0, 2)
        mid_bottom_grid.addWidget(self._delete_ingredient_btn, 1, 0)
        mid_bottom_grid.addWidget(self._cancel_ingredient_btn, 1, 1)
        mid_bottom_grid.addWidget(self._add_ingredient_btn, 1, 2)

        mid_v_box.addLayout(mid_bottom_grid)
        mid_v_box.addWidget(self._ingredients_list)

        # right
        right_v_box: QVBoxLayout = QVBoxLayout()

        right_h_box_1: QHBoxLayout = QHBoxLayout()
        right_h_box_1.addWidget(self._recipe_entry_label)
        right_h_box_1.addStretch()
        right_h_box_1.addWidget(self._save_recipe_text_btn)

        right_v_box.addLayout(right_h_box_1)
        right_v_box.addWidget(self._recipe_entry_te)

        right_h_box2: QHBoxLayout = QHBoxLayout()
        right_h_box2.addWidget(self._global_save_btn)
        right_h_box2.addWidget(self._export_btn)

        right_v_box.addLayout(right_h_box2)

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

    def _init_data(self) -> None:
        self._load_recipes()
        self._load_raw_types()

        self._check_valid_recipe()
        self._chanced_recipe()

    # check
    def _check_valid_recipe(self) -> None:
        count: int = self._recipes_list.count()
        if count <= 0:
            self._add_recipe()
        else:
            self._recipes_list.setCurrentRow(0)

    # add
    def _add_recipe(self) -> None:
        new_name: str = f"new recipe {self._recipes_list.count() + 1}"
        result = a.add.add_recipe(new_name, "description")
        if not result.valid:
            self._display_message(result.entry)
            return

        recipe: RecipeItem = RecipeItem(result.entry, new_name, "description")
        self._recipes_list.addItem(recipe)
        self._recipes_list.setCurrentItem(recipe)

    # update
    def _update_recipe(self) -> bool:
        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if not current_recipe:
            self._display_message("no selected recipe to update")
            return False

        result = u.update.update_recipe_by_ID(current_recipe.ID, current_recipe.title, current_recipe.description)
        if not result.valid:
            self._display_message(result.entry)
            return False

        return True

    # delete
    def _delete_recipe(self) -> None:
        current_item: RecipeItem = self._recipes_list.currentItem()
        if not current_item:
            self._display_message("no selected recipe to delete")
            return

        if not self._display_accept_message("Delete?", f"Do you want to delete {current_item.title}", str()):
            return

        result = d.delete.delete_recipe_by_ID(current_item.ID)

        if not result.valid:
            self._display_message(result.entry)
            return

        self._recipes_list.takeItem(self._recipes_list.row(current_item))
        self._check_valid_recipe()

    # load
    def _load_raw_types(self) -> None:
        result = s.select.select_all_raw_types()
        if not result.valid:
            self._display_message(result.entry)
            return

        self._types_list.clear()
        for ID, entry in result.entry:
            item: RawTypeItem = RawTypeItem(ID, entry, False)
            self._types_list.addItem(item)

    def _load_recipes(self) -> None:
        result = s.select.select_all_recipes()
        if not result.valid:
            self._display_message(result.entry)
            return

        self._recipes_list.clear()
        for ID, title, description in result.entry:
            recipe: RecipeItem = RecipeItem(ID, title, description)
            self._recipes_list.addItem(recipe)

    def _load_types(self, recipe: RecipeItem) -> None:
        result = s.select.select_type_by_recipe_ID(recipe.ID)
        if not result.valid:
            self._display_message(result.entry)
            return

        for i in range(self._types_list.count()):
            current_type: RawTypeItem = self._types_list.item(i)

            selected: bool = False
            for _, _, raw_type_ID in result.entry:
                if raw_type_ID == current_type.ID:
                    current_type.set_selected(True)
                    selected = True
                    break

            if not selected:
                current_type.set_selected(False)

    # clear
    def _clear_type_search(self) -> None:
        self._types_search_le.clear()

    def _clear_recipe_search(self) -> None:
        self._recipe_search_le.clear()

    def _clear_cancel_ingredients(self) -> None:
        self._amount_le.clear()
        self._unit_le.clear()
        self._ingredient_le.clear()
        self._ingredients_list.clearSelection()

    # clicked
    def _clicked_save_title(self) -> None:
        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if not current_recipe:
            self._display_message("no current recipe for saving title")
            return

        old_title: str = current_recipe.title
        current_recipe.set_title(self._title_le.text())
        if not self._update_recipe():
            current_recipe.set_title(old_title)
            return
        self._save_title_btn.setEnabled(False)
        self._recipes_list.sortItems()

    def _clicked_save_description(self) -> None:
        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if not current_recipe:
            self._display_message("no selected recipe for saving description")
            return

        old_text: str = current_recipe.description
        current_recipe.description = self._recipe_entry_te.toPlainText()
        if not self._update_recipe():
            current_recipe.description = old_text
            return
        self._save_recipe_text_btn.setEnabled(False)

    def _clicked_type(self) -> None:
        current_type: RawTypeItem = self._types_list.currentItem()
        if not current_type:
            return
        current_type.toggle_selected()

        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if not current_recipe:
            return

        if current_type.selected:
            a.add.add_type(current_recipe.ID, current_type.ID)
        else:
            d.delete.delete_type_by_recipe_ID_and_raw_type_ID(current_recipe.ID, current_type.ID)

        self._types_list.clearSelection()

    # chanced
    def _chanced_recipe(self) -> None:
        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if not current_recipe:
            return

        self._title_le.setText(current_recipe.title)
        self._recipe_entry_te.setText(current_recipe.description)
        self._load_types(current_recipe)

    def _chanced_recipe_search(self) -> None:
        current_text: str = self._recipe_search_le.text().strip()
        self._clear_recipe_search_btn.setEnabled(len(current_text) != 0)

        for i in range(self._recipes_list.count()):
            current_item: RecipeItem = self._recipes_list.item(i)
            found: bool = current_text.lower() in current_item.title.lower()
            current_item.setHidden(not found)

    def _chanced_title(self) -> None:
        current_text: str = self._title_le.text().strip()
        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if not current_recipe:
            self._display_message("no selected recipe for title chance")
            return

        self._save_title_btn.setEnabled(current_text != current_recipe.title and len(current_text) != 0)

    def _chanced_ingredient_le(self) -> None:
        amount: str = self._amount_le.text().strip()
        unit: str = self._unit_le.text().strip()
        ingredient: str = self._ingredient_le.text().strip()
        has_entry: bool = len(amount) != 0 and len(unit) != 0 and len(ingredient) != 0

        if not has_entry:
            self._add_ingredient_btn.setEnabled(False)
            return

        current_ingredient: IngredientItem = self._ingredients_list.currentItem()
        if not current_ingredient:
            self._add_ingredient_btn.setEnabled(True)
            return

    def _chanced_description(self) -> None:
        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if not current_recipe:
            self._display_message("no selected recipe for description chance")
            return
        current_text: str = self._recipe_entry_te.toPlainText()
        self._save_recipe_text_btn.setEnabled(current_recipe.description != current_text)

    def _chanced_text_type_search(self) -> None:
        text: str = self._types_search_le.text().strip()
        self._clear_types_search_btn.setEnabled(len(text) != 0)

        for i in range(self._types_list.count()):
            item: RawTypeItem = self._types_list.item(i)
            found: bool = text.lower() in item.entry.lower()
            item.setHidden(not found)

    # raw type window
    def _set_raw_type_window(self) -> None:
        self.window().setEnabled(False)
        self._raw_types_window = RawTypesWindow(self._raw_types_callback)

    def _raw_types_callback(self) -> None:
        self._load_raw_types()
        self._types_search_le.clear()
        self._raw_types_window = None
        current_recipe: RecipeItem = self._recipes_list.currentItem()
        if current_recipe:
            self._load_types(current_recipe)

        self.window().setEnabled(True)

    # statics
    @staticmethod
    def _display_message(message: str) -> None:
        msg: QMessageBox = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        x = msg.exec_()

    @staticmethod
    def _display_accept_message(title: str, message: str, sub_message: str) -> bool:
        msg: QMessageBox = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setInformativeText(sub_message)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        result = msg.exec_()

        return result == QMessageBox.Ok
