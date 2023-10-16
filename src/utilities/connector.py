import sqlite3


def connect(path: str) -> sqlite3.Cursor:
    """(str) -> Cursor
    return cursor object of required database
    """
    # sqlite3.connect(path)
    return sqlite3.connect(path).cursor()