import dash_bootstrap_components as dbc
from sqlite3 import Cursor
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output

from . import page1, page2, swap_pages
from .cards import top_cards
from ..utilities import classes_names, swap_pages_logic, ids


THEME = 'dark'


def render(app: Dash, cursor: Cursor) -> html.Div:
  '''(Dash) -> Div
  Create the layout of the app
  '''

  @callback(
        Output(ids.MY_LAYOUT, 'children'),
        Input(ids.CURRENT_URL, 'pathname')
  )
  def display_page(pathname):
      if '1':
        return page1.render()
      elif '2':
        return page2.render()

  return dbc.Container(
    [
      dcc.Location(
        id=ids.CURRENT_URL,
        refresh=False
      ),
      dbc.Row(
        [
          # Top bar for filter and language and theme
        ]
      ),
      html.Br(),
      dbc.Row(
      [
        dbc.Col(
          [
            top_cards.render(app, cursor, 'dark'),
            dbc.Container(id=ids.MY_LAYOUT)

          ],
          width=10
        ),
        dbc.Col(
          [
            # Navigation buttons,
            # Inside container
          ],
          width=2
        )
      ]
    )
    ]
  )