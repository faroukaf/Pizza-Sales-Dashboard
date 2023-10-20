from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from .cards import top_cards
from ..utilities import classes_names, ids


def render(app: Dash, cursor: Cursor, theme: str) -> html.Div:
  '''(Dash) -> Div
  Create the page 1 layout of the app
  '''

  # @app.callback(
  #     [
  #       Output(ids.SWAP_CONTAINER, 'style'),
  #       Output(ids.PAGE1, 'hidden'),
  #       Output(ids.PAGE2, 'hidden'),
  #       # Output(ids.RIGHT_PAGE_SWAP, 'disable_n_clicks')
  #     ],
  #     [
  #       Input(ids.SWAP_CONTAINER, 'style'),
  #       Input(ids.RIGHT_PAGE_SWAP, 'n_clicks')
  #     ]
  # )
  # def do_right(style: dict, _: int) -> (bool, bool, bool):
  #   print(style)
  #   if style['page-number'] == 1:
  #     return {'page-number': 2}, True, False#, True
  #   return {'page-number': 1}, False, True#, False

  return html.Div(
    id=ids.PAGE1,
    children=[
      top_cards.render(app, cursor, theme),
      html.H1('page1')
      # months_checklist.render()
    ],
    className= classes_names.PAGE1_LAYOUT+theme,
    hidden=True
  )