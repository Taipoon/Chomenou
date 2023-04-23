import csv


def csv_to_sql(table_name: str, csv_file: str, sql_file: str or None = None, cleanup=False):
    # Read the csv file
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        tokens = [f"INSERT INTO `{table_name}`"]

        columns = []
        for column_name in reader.fieldnames:
            columns.append(f"`{column_name}`")
        tokens.append("(" + ",".join(columns) + ")")

        tokens.append("VALUES")

        # data type of column
        column_types: dict = next(reader)

        values = []
        for row in reader:
            col = "("

            for t, v in zip(column_types.values(), row.values()):
                if t == "int":
                    d = int(v)
                elif t == "float":
                    d = float(v)
                else:
                    d = f"'{v}'"
                col += str(d) + ", "

            col = col[:-2] + ")"
            values.append(col)

        tokens.append(", \n".join(values))

    queries = []

    # Write the SQL file
    with open(sql_file, "w", encoding="utf-8") as f:
        if cleanup:
            # all existing data is deleted before the data is inserted.
            queries.append(f"DELETE FROM `{table_name}`;")

        queries.append(" \n".join(tokens) + ";\n")
        sql_text = "\n".join(queries)

        f.write(sql_text)

    return sql_text
