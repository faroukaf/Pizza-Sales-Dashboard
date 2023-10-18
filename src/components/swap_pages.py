from dash import Dash, dcc, html
from sqlite3 import Cursor
from .cards import top_cards
from ..utilities import classes_names, ids


def render(app: Dash, cursor: Cursor, theme: str) -> html.Div:
  '''(Dash) -> Div
  Create the page 1 layout of the app
  '''

  return html.Div(
    id=ids.SWAP_CONTAINER,
    children=[
      html.Button(
        id=ids.LEFT_PAGE_SWAP,
        children=[html.Img(src='/assets/arrow-left-1.svg')],
        className=classes_names.SWAP_BUTTON+theme
      ),
      html.H1('   '),
      html.Button(
        id=ids.RIGHT_PAGE_SWAP,
        children=[html.Img(src='/assets/arrow-right-1.svg')],
        className=classes_names.SWAP_BUTTON+theme
      ),
      html.Div(
        id=ids.HIDDEN_DIV1,
        hidden=True,
        style={'page-number': 1}
      )
    ],
    className= classes_names.SWAP_BUTTON_CONTAINER+theme,
    style={'page-number': 1}
  )