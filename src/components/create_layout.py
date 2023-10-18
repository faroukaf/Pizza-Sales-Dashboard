from dash import Dash, dcc, html
from sqlite3 import Cursor
from . import months_checklist
from .cards import top_cards
from ..utilities import classes_names

THEME = 'dark'


def render(app: Dash, cursor: Cursor) -> html.Div:
  '''(Dash) -> Div
  Create the layout of the app
  '''

  return html.Div(
    children=[
      top_cards.render(app, cursor, THEME)
      # months_checklist.render()
    ],
    className= classes_names.MAIN_LAYOUT + THEME
  )