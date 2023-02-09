import os.path
import sqlite3


class DummyInserter(object):
    def __init__(self, path):
        self._conn = sqlite3.connect(path)

    def insert_statements(self, columns: list[str], rows: list[list[str]]):
        self._insert(table_name="statements", columns=columns, rows=rows)

    def _insert(self, table_name: str, columns: list[str], rows: list[list[str]]):
        sql = f"INSERT INTO `{table_name}` "
        sql += "(" + ','.join(columns) + ")"

        tokens = []
        for row in rows:
            v = []
            for value in row:
                try:
                    value = int(value)
                    v.append(value)
                except ValueError:
                    v.append(value)
            token = "(" + ",".join(v) + ")"
            tokens.append(token)

        sql += " VALUES " + ",".join(tokens)

        cursor = self._conn.cursor()
        cursor.execute(sql)


if __name__ == '__main__':
    inserter = DummyInserter(path="test.db")

    cols = ["id", "year", "month", "day", "amount", "account_id", "created_at"]
    rows = [
        [1, 2000, 1, 1, 3000, 1, "2000-01-01 12:13:14"],
        [1, 2000, 1, 1, 3000, 1, "2000-01-01 12:13:14"],
        [1, 2000, 1, 1, 3000, 1, "2000-01-01 12:13:14"],
        [1, 2000, 1, 1, 3000, 1, "2000-01-01 12:13:14"],
        [1, 2000, 1, 1, 3000, 1, "2000-01-01 12:13:14"],
    ]

    inserter.insert_statements(cols, rows)
