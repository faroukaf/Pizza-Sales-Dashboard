from dash import Dash, dcc, html
from sqlite3 import Cursor
from . import months_checklist
from ..utilities import classes_names

THEME = 'dark'


def render(app: Dash, cursor: Cursor) -> html.Div:
  '''(Dash) -> Div
  Create the layout of the app
  '''

  cursor.execute('select gmn(order_date) from pizza limit 1;')
  result = cursor.fetchone()

  return html.Div(
    children=[
      html.Div(
        children=[html.H1(result[0])]
      ),
      months_checklist.render()
    ],
    className= classes_names.MAIN_LAYOUT + THEME
  )