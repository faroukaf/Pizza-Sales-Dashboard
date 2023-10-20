import pandas as pd
from sqlite3 import Cursor


def get_columns_names(lis: list[tuple[str]]) -> list[str]:
  """(list[tuple(str)]) -> list[str]
  Return all columns names from cursor
  """
  out = []

  for i in lis:
    out.append(i[0])

  return out

def fetch2df(cursor: Cursor) -> pd.DataFrame:
  """(Cursor) -> DataFrame
  Turn the fetch result to pandas DataFrame
  """
  result = cursor.fetchall()
  df = pd.DataFrame(result, columns=get_columns_names(cursor.description))

  return df

def get_quire_result(cursor: Cursor, quire: str) -> pd.DataFrame:
  """
  Get the result of the quire wanted

  quire: is the quire wanted
  cursor: cursor which execute the quire in
  """
  cursor.execute(quire)
  data = fetch2df(cursor)
  # print(data)
  return data
