import abc


class IAccountBookExporter(abc.ABC):
    def __init__(self, year: int, output_dir: str = None):
        self.year = year
        self.output_dir = output_dir or "."

    @abc.abstractmethod
    def export(self) -> None:
        """
        明細データを外部にエクスポートします。
        :return: None
        """
        raise NotImplementedError
