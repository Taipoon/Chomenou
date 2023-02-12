from domain.helpers.metaclass_resolver import make_cls
from domain.views import BulkInsertionView
from presenters.bulk_insertion_presenter import BulkInsertionPresenter
from pyqt6.ui_files.ui_bulk_insertion_dialog import Ui_BulkInsertionDialog


class BulkInsertionDialog(Ui_BulkInsertionDialog, BulkInsertionView, metaclass=make_cls()):

    def __init__(self):
        super().__init__()
        self._presenter = BulkInsertionPresenter(view=self)

    def initialize_ui(self):
        pass

    def update_line_edit(self, value: int):
        pass
