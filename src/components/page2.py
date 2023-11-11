from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from .cards import top_cards, barh_cards
from ..utilities import classes_names, ids


def render(app: Dash, cursor: Cursor, theme: str) -> html.Div:
  '''(Dash) -> Div
  Create the page 2 layout of the app
  '''

  # @app.callback(
  #   Output(ids.PAGE2, 'children'),
  #   Input(ids.LEFT_PAGE_SWAP, 'n_clicks')
  # )
  # def pfo(_: int) -> list[html.H2]:
  #   print(11)
  #   return [html.H2(44)]

  return html.Div(
    id=ids.PAGE2,
    children=[
      top_cards.render(app, cursor, theme),
      html.Br(),
      barh_cards.render(app, cursor, theme)
    ],
    className= classes_names.PAGE2_LAYOUT+theme,
    hidden=False
  )