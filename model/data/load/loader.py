from model.data import db


def get_stations_rows() -> int:
    """
    Retrieve the number of rows in the Cities table.
    :return: the number of rows in the Cities table
    """

    return get_row_count('Stations')


def get_row_count(table_name: str) -> int:
    """
    Retrieve the number of rows in the specified table/view from the sqlite
    database.
    :param table_name: the name of the table/view
    :return: the number of rows in the table
    """

    with db.get_conn() as conn:
        rows = conn.execute('SELECT COUNT(*) FROM {t};'.format(t=table_name))
        return rows.fetchall()[0][0]
