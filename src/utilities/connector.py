import sqlite3
import babel.dates as bd
from datetime import datetime

from .get_metadata import (
    get_sizes_name as gzn, get_months_names as gmn,
    get_days_names as gdn
)


METADATA = {
    'months': gmn(),
    'days': gdn(),
    'sizes': gzn()
}

def get_day_name(date: str) -> str:
    """( , str) -> str
    get the day name using babel
    local: localization language
    """
    str2date = datetime.strptime(date, '%d-%m-%Y')
    day_num = str2date.weekday()

    return METADATA['days'][day_num]

    # return lambda temp: bd.format_date(str2date(temp), 'E', locale=locale)

# get_day_name_func = lambda locale: lambda d: bd.format_date(
#     datetime.strptime(d, '%m-%d-%Y'), 'E', locale=locale
# )


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
    """(str, str) -> Cursor
    path: path of the database to connect
    local: localization language
    return cursor object of required database
    """
    con = sqlite3.connect(path)
    con.create_function('gmn', 1, get_month_name)
    con.create_function('gdn', 1, get_day_name)
    con.create_function('gzn', 1, get_size_name)
    return con.cursor()
