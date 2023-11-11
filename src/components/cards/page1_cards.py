import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from . import month_linear
from ...utilities import classes_names, ids


def render(app: Dash, cursor: Cursor, theme: str) -> dbc.Col:
  '''(Dash) -> Col
  Create collections of carts in page 1 layout of the app
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


  return dbc.Col(
    children=[
      dbc.Row(
        children=[
          month_linear.render(cursor, 'Monthly Trend for Total Order'),
          #daily bar
        ]
      ),
      dbc.Row(
        children=[
          #pie size,
          #pie category,
          #tunnel category
        ]
      )
    ],
    className='w-70'
  )