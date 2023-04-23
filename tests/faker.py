import os.path
import sqlite3

from tests.csv2sql import csv_to_sql


class TestDB(object):
    def __init__(self, dummy_csv_files: list[str], db_path: str):
        self._db_path = os.path.abspath(db_path)
        self._csv_files = dummy_csv_files
        self._conn = sqlite3.connect(self._db_path)

    def reset(self):
        self._setup_schema()
        self._setup_data()

    def _setup_schema(self):
        statements = [
            "PRAGMA foreign_keys=false;",
            "DROP TABLE IF EXISTS `account_types`;",
            "DROP TABLE IF EXISTS `accounts`;",
            "DROP TABLE IF EXISTS `statements`;",
            "PRAGMA foreign_keys=true;",
            "CREATE TABLE IF NOT EXISTS `account_types` (`id` INTEGER PRIMARY KEY AUTOINCREMENT ,`type_name` TEXT NOT "
            "NULL UNIQUE ,`type_name_hepburn` TEXT NOT NULL UNIQUE);",
            "CREATE TABLE IF NOT EXISTS `accounts` (`id` INTEGER PRIMARY KEY AUTOINCREMENT ,`account_name` TEXT NOT "
            "NULL UNIQUE ,`account_name_hepburn` TEXT NOT NULL UNIQUE ,`account_type_id` INTEGER NOT NULL ,"
            "`default_amount` INTEGER NOT NULL DEFAULT 0 ,FOREIGN KEY (`account_type_id`) REFERENCES `account_types`("
            "`id`));",
            "CREATE TABLE IF NOT EXISTS `statements` (`id` INTEGER PRIMARY KEY AUTOINCREMENT ,`year` INTEGER NOT NULL "
            ",`month` INTEGER NOT NULL ,`day` INTEGER NOT NULL ,`account_id` INTEGER NOT NULL ,`amount` INTEGER NOT "
            "NULL ,`created_at` TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')) ,FOREIGN KEY (`account_id`) "
            "REFERENCES `accounts`(`id`));",
        ]

        for statement in statements:
            self._conn.execute(statement)

    def _setup_data(self):
        for fp in self._csv_files:
            abs_fp = os.path.abspath(fp)
            dir_name = os.path.dirname(abs_fp)

            tbl_name, ext = os.path.basename(abs_fp).split(os.path.extsep)
            sql_file_path = os.path.join(dir_name, tbl_name + ".sql")

            query = csv_to_sql(table_name=tbl_name, csv_file=abs_fp,
                               sql_file=sql_file_path)
            query = query.replace("\n", "")
            self._conn.execute(query)
            self._conn.commit()

    def __del__(self):
        if self._conn:
            self._conn.close()
