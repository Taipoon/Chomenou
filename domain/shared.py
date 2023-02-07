import dotenv

from domain.exceptions import InvalidConfigException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    def __init__(self):
        self._ui_debug = False
        self._repository_debug = False
        self._sqlite_path = None
        self._output_excel_filepath = None
        self._output_csv_filepath = None

        envs = dotenv.dotenv_values()
        self._parse(envs)

    def _parse(self, envs: dict):
        try:
            self._ui_debug = envs.get("UI_DEBUG").lower() == "true"
            self._repository_debug = envs.get("REPOSITORY_DEBUG").lower() == "true"

            self._sqlite_path = envs.get("SQLITE_PATH")

            self._output_excel_filepath = envs.get("OUTPUT_EXCEL_FILENAME")
            self._output_csv_filepath = envs.get("OUTPUT_CSV_FILENAME")

        except AttributeError:
            raise InvalidConfigException

    @property
    def ui_debug(self) -> bool:
        return self._ui_debug

    @property
    def repository_debug(self) -> bool:
        return self._repository_debug
