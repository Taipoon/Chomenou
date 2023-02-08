import dotenv

from domain.exceptions import InvalidConfigException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    ui_debug = False
    repository_debug = False
    sqlite_path = None
    output_excel_filepath = None
    output_csv_filepath = None

    @classmethod
    def parse(cls):
        try:
            envs = dotenv.dotenv_values()
            cls.ui_debug = envs.get("UI_DEBUG").lower() == "true"
            cls.repository_debug = envs.get("REPOSITORY_DEBUG").lower() == "true"

            cls.sqlite_path = envs.get("SQLITE_PATH")

            cls.output_excel_filepath = envs.get("OUTPUT_EXCEL_FILENAME")
            cls.output_csv_filepath = envs.get("OUTPUT_CSV_FILENAME")

        except AttributeError:
            raise InvalidConfigException
