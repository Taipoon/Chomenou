import os

from PyQt6 import uic

from pyqt6.ui_files.ui_bulk_insertion_dialog import Ui_BulkInsertionDialog


class BulkInsertionDialog(Ui_BulkInsertionDialog):
    def __init__(self):
        super().__init__()

        if os.environ.get("UI_DEBUG"):
            uic.loadUi(os.path.join(os.path.dirname(__file__),
                                    "ui_files",
                                    "accountsEditorDialog.ui"), self)

        self._initialize_ui()

    def _initialize_ui(self):
        pass

