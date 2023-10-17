import sqlite3

from .get_months_names import get_months_names as gmn


def get_month_name(date: str) -> str:
    """
    Will add as function in the connection of 
    data base
    """
    months = gmn()
    m = date.split('-')[1]
    m = int(m)
    return months[m]


def connect(path: str) -> sqlite3.Cursor:
    """(str) -> Cursor
    return cursor object of required database
    """
    con = sqlite3.connect(path)
    con.create_function('gmn', 1, get_month_name)
    return con.cursor()
