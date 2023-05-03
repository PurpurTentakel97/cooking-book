#
# Purpur Tentakel
# Cocking Book
# 03.05.2023
#

from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit

from UI.Color import Colors

from database import select as s


class TypeItem(QListWidgetItem):
    def __init__(self, ID: int, value: str):
        super().__init__()
        self.ID = ID
        self.value = value
        self.selected = False

        self.setText(self.value)

    def _set_background(self) -> None:
        if self.selected:
            self.setBackground(Colors.grey)
        else:
            self.setBackground(Colors.white)

    def _toggle_selected(self) -> None:
        self.selected = not self.selected
        self._set_background()


class FilterRecipeWindow(QWidget):
    def __init__(self, close_callback):
        super().__init__()

        self._close_callback = close_callback

        self._initialize()
        self._set_layout()
        self._load_data()

    # init
    def _initialize(self) -> None:
        self._search_le: QLineEdit = QLineEdit()
        self._search_le.setPlaceholderText("search type")
        self._clear_search_btn: QPushButton = QPushButton("clear search")

        self._type_list: QListWidget = QListWidget()

        self._accept_btn: QPushButton = QPushButton("filter")
        self._clear_selection_btn: QPushButton = QPushButton("clear selection")

    def _set_layout(self) -> None:
        top_h_box: QHBoxLayout = QHBoxLayout()
        top_h_box.addWidget(self._search_le)
        top_h_box.addWidget(self._clear_search_btn)

        bottom_h_box: QHBoxLayout = QHBoxLayout()
        bottom_h_box.addWidget(self._clear_selection_btn)
        bottom_h_box.addWidget(self._accept_btn)

        global_v_box: QVBoxLayout = QVBoxLayout()
        global_v_box.addLayout(top_h_box)
        global_v_box.addWidget(self._type_list)
        global_v_box.addLayout(bottom_h_box)

        self.setLayout(global_v_box)
        self.show()

    def _load_data(self) -> None:
        result = s.select.select_all_raw_types()
        if not result.valid:
            return

        for ID, value in result.entry:
            item: TypeItem = TypeItem(ID, value)
            self._type_list.addItem(item)

    def closeEvent(self, event) -> None:
        self._close_callback()
        event.accept()
