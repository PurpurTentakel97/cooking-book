#
# Purpur Tentakel
# Cocking Book
# 25.04.2023
#

from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QHBoxLayout, QVBoxLayout, \
    QMessageBox
from database import select as s
from database import add as a
from database import update as u
from database import delete as d


class RawTypeEntry(QListWidgetItem):
    def __init__(self, ID: int, entry: str) -> None:
        super().__init__()
        self.ID: int = ID
        self.entry: str = entry

        self.setText(self.entry)


class RawTypesWindow(QWidget):
    def __init__(self, close_callback) -> None:
        super().__init__()
        self._close_callback = close_callback

        self._initialize()
        self._setLayout()
        self._load_raw_types()

    def _initialize(self) -> None:
        self.setWindowTitle("types")
        self._input: QLineEdit = QLineEdit()
        self._input.setPlaceholderText("typename")
        self._input.returnPressed.connect(self._accept_clicked)
        self._input.textChanged.connect(self._input_changed)

        self._delete_btn: QPushButton = QPushButton("delete")
        self._delete_btn.clicked.connect(self._delete_clicked)
        self._delete_btn.setEnabled(False)
        self._cancel_btn: QPushButton = QPushButton("cancel")
        self._cancel_btn.clicked.connect(self._cancel_clicked)
        self._accept_btn: QPushButton = QPushButton("accept")
        self._accept_btn.clicked.connect(self._accept_clicked)
        self._accept_btn.setEnabled(False)

        self._list: QListWidget = QListWidget()
        self._list.clicked.connect(self._list_clicked)

    def _setLayout(self) -> None:
        global_vbox: QVBoxLayout = QVBoxLayout()
        global_vbox.addWidget(self._input)

        btn_hbox: QHBoxLayout = QHBoxLayout()
        btn_hbox.addWidget(self._delete_btn)
        btn_hbox.addWidget(self._cancel_btn)
        btn_hbox.addWidget(self._accept_btn)

        global_vbox.addLayout(btn_hbox)
        global_vbox.addWidget(self._list)

        self.setLayout(global_vbox)
        self.setFixedSize(500, 800)
        self.show()

    def _load_raw_types(self) -> None:
        self._list.clear()
        data = s.select.select_all_raw_types()
        if not data.valid:
            self._display_message(data.entry)
            return
        for ID, raw_type in data.entry:
            entry: RawTypeEntry = RawTypeEntry(ID, raw_type)
            self._list.addItem(entry)

    def _list_clicked(self) -> None:
        current_item: RawTypeEntry = self._list.currentItem()
        if not current_item:
            return

        self._input.setText(current_item.entry)
        self._delete_btn.setEnabled(True)

    def _cancel_clicked(self) -> None:
        self._clear()

    def _accept_clicked(self) -> None:
        current_item: RawTypeEntry = self._list.currentItem()
        if not current_item:
            self._add_type(self._input.text())
            return

        self._update_type(current_item.ID, self._input.text())

    def _delete_clicked(self) -> None:
        current_item: RawTypeEntry = self._list.currentItem()
        if not current_item:
            self._display_message("no entry selected")
            return

        msg: QMessageBox = QMessageBox()
        msg.setWindowTitle("Delete?")
        msg.setText(f"Do you wan to delete {current_item.entry}")
        msg.setInformativeText("when an type gets deleted it will be deleted from all recipes.")
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        result = msg.exec_()

        if result != QMessageBox.Ok:
            return

        self._delete_type(current_item.ID)

    def _add_type(self, new_type: str) -> None:
        result = a.add.add_raw_type(new_type)
        if not result.valid:
            self._display_message(result.entry)
            return
        self._clear()
        self._load_raw_types()

    def _update_type(self, ID: int, new_type: str) -> None:
        result = u.update.update_raw_type_by_ID(ID, new_type)
        if not result.valid:
            self._display_message(result.entry)
            return
        self._clear()
        self._load_raw_types()

    def _delete_type(self, ID: int) -> None:

        result = d.delete.delete_raw_type_by_ID(ID)
        if not result.valid:
            self._display_message(result.entry)
            return
        self._clear()
        self._load_raw_types()

    def _clear(self) -> None:
        self._input.clear()
        self._list.clearSelection()
        self._delete_btn.setEnabled(False)

    def _input_changed(self) -> None:
        current_input: str = self._input.text().strip()
        self._accept_btn.setEnabled(len(current_input) != 0)

    @staticmethod
    def _display_message(message: str) -> None:
        msg: QMessageBox = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        x = msg.exec_()

    def closeEvent(self, event) -> None:
        self._close_callback()
        event.accept()
