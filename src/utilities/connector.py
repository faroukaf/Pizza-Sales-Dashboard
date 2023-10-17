import sqlite3

from .get_metadata import get_sizes_name as gzn, get_months_names as gmn


METADATA = {
    'months': gmn(),
    'sizes': gzn()
}


def get_month_name(date: str) -> str:
    """(str) -> str
    Will add as function in the connection of 
    data base to know the month name

    date: is the date in string format
    """
    
    m = date.split('-')[1]
    m = int(m)
    return METADATA['months'][m]

def get_size_name(s: str) -> str:
    """(str) -> str
    Will add as function in the connection of 
    data base to know the size name
    from his shorten

    s: is the shorten of the size
    """
    return METADATA['sizes'][s]


def connect(path: str) -> sqlite3.Cursor:
    """(str) -> Cursor
    return cursor object of required database
    """
    con = sqlite3.connect(path)
    con.create_function('gmn', 1, get_month_name)
    con.create_function('gzn', 1, get_size_name)
    return con.cursor()
