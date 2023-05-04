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

    def toggle_selected(self) -> None:
        self.selected = not self.selected
        self._set_background()

    def set_selected(self, selected: bool) -> None:
        self.selected = selected
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
        self._search_le.textChanged.connect(self._search_type)
        self._clear_search_btn: QPushButton = QPushButton("clear search")
        self._clear_search_btn.clicked.connect(self._clear_search)

        self._type_list: QListWidget = QListWidget()
        self._type_list.itemClicked.connect(self._type_clicked)

        self._accept_btn: QPushButton = QPushButton("set filter")
        self._accept_btn.clicked.connect(self._set_filter)
        self._clear_selection_btn: QPushButton = QPushButton("clear selection")
        self._clear_selection_btn.clicked.connect(self._clear_selection)

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

    def _type_clicked(self) -> None:
        current_type: TypeItem = self._type_list.currentItem()
        if not current_type:
            return

        current_type.toggle_selected()
        self._type_list.clearSelection()

    def _clear_selection(self) -> None:
        for i in range(self._type_list.count()):
            item: TypeItem = self._type_list.item(i)
            item.set_selected(False)

    def _clear_search(self) -> None:
        self._search_le.clear()

    def _search_type(self) -> None:
        search_text: str = self._search_le.text().strip()
        for i in range(self._type_list.count()):
            item: TypeItem = self._type_list.item(i)
            contains: bool = search_text.lower() in item.value.lower()
            item.setHidden(not contains)

    def _set_filter(self) -> None:
        self.close()

    def _get_current_selected_IDs(self) -> list[int, ...]:
        to_return: list[int, ...] = list()

        for i in range(self._type_list.count()):
            item: TypeItem = self._type_list.item(i)
            if item.selected:
                to_return.append(item.ID)

        return to_return

    def closeEvent(self, event) -> None:
        self._close_callback(self._get_current_selected_IDs())
        event.accept()
