import csv


def create_dummy_sql(table_name: str, input_file: str, output_file: str, cleanup=False):
    tokens = [f"INSERT INTO `{table_name}`"]

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        columns = []
        for column_name in reader.fieldnames:
            columns.append(f"`{column_name}`")
        tokens.append("(" + ",".join(columns) + ")")

        tokens.append("VALUES")

        values = []
        for row in reader:
            col = []
            for v in row.values():
                col.append(f"{v}")

            values.append("(" + ", ".join(col) + ")")
        tokens.append(", \n".join(values))

    with open(output_file, "w", encoding="utf-8") as f:
        if cleanup:
            f.write(f"DELETE FROM `{table_name}`;\n")

        f.write(" \n".join(tokens) + ";")


if __name__ == '__main__':
    create_dummy_sql("statements", "../infrastructure/mock/statements_fake.csv", "dummy_statements.sql", cleanup=True)
