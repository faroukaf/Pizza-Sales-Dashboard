import dash_bootstrap_components as dbc
from sqlite3 import Cursor
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output

from . import page1, page2, side_nev
from .cards import top_cards
from ..utilities import ids, pages
from ..utilities.source import DataSource


THEME = 'dark'


def render(app: Dash, source: DataSource) -> html.Div:
  '''(DataSource) -> Div
  Create the layout of the app
  '''

  @callback(
        Output(ids.MY_LAYOUT, 'children'),
        Input(ids.CURRENT_URL, 'pathname')
  )
  def display_page(pathname: str):
      page_path = pathname.split('/')[-1]
      if page_path == pages.HOME:
        return page1.render(source)
      elif page_path == pages.TOP_AND_WORST:
        return page2.render(source)

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
        side_nev.render(source),
        dbc.Col(
          [
            top_cards.render(app, source),
            dbc.Container(id=ids.MY_LAYOUT)

          ],
          width=10
        ),
      ]
    )
    ]
  )