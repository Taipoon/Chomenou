import configparser
import os

from domain.exceptions import InvalidConfigException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    is_fake = None
    sqlite_filepath = None
    output_excel_filepath = None
    output_csv_filepath = None

    @classmethod
    def parse(cls, ini_filepath: str, section: str = "DEFAULT", force_debug=False):
        try:
            parser = configparser.ConfigParser()
            parser.read(ini_filepath, encoding="utf-8")

            envs = parser[section]
            # fake data
            cls.is_fake = envs.get("IS_FAKE").lower() == "true" or force_debug
            # path to sqlite database for production
            cls.sqlite_filepath = os.path.abspath(envs.get("SQLITE_FILEPATH"))
            # path to output files
            cls.output_excel_filepath = os.path.abspath(envs.get("OUTPUT_EXCEL_FILEPATH"))
            cls.output_csv_filepath = os.path.abspath(envs.get("OUTPUT_CSV_FILEPATH"))

        except AttributeError:
            raise InvalidConfigException
