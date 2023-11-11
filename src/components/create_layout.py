from dash import Dash, dcc, html
from sqlite3 import Cursor
from . import page1, page2, swap_pages
from .cards import top_cards
from ..utilities import classes_names, swap_pages_logic

THEME = 'dark'


def render(app: Dash, cursor: Cursor) -> html.Div:
  '''(Dash) -> Div
  Create the layout of the app
  '''

  # swap_pages_logic.swap(app)

  return html.Div(
    children=[
      page1.render(app, cursor, THEME),
      # page2.render(app, cursor, THEME),
      # swap_pages.render(app, cursor, THEME)
      # months_checklist.render()
    ],
    className= classes_names.MAIN_LAYOUT + THEME
  )