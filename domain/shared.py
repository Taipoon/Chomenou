import dotenv

from domain.exceptions import InvalidConfigException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# TODO: .ini ファイルに変更 configparser を用いる
class Config(metaclass=Singleton):
    is_fake = None
    sqlite_path = None
    output_excel_filepath = None
    output_csv_filepath = None

    @classmethod
    def parse(cls, force_debug=False, dotenv_path=None):
        try:
            envs = dotenv.dotenv_values(dotenv_path=dotenv_path)
            # use fake data
            cls.is_fake = envs.get("IS_FAKE").lower() == "true" or force_debug
            # path to sqlite database for production
            cls.sqlite_path = envs.get("SQLITE_PATH")
            # path to output files
            cls.output_excel_filepath = envs.get("OUTPUT_EXCEL_FILENAME")
            cls.output_csv_filepath = envs.get("OUTPUT_CSV_FILENAME")

        except AttributeError:
            raise InvalidConfigException


class Signal(object):
    ABOUT = 100
    INFO = 200
    WARNING = 300
    CRITICAL = 400
