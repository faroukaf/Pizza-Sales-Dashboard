from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ...utilities import classes_names


def render(app: Dash, value: str, title:str, src: str, theme: str) -> html.Div:
  """(Dash, str, str, str, str) -> Div
  create the card of the single value 
  app: is the app
  value: is the value shown in the middle
  title: is title shown in the bottom
  src: the src of the picture
  """
  return html.Div(
    children=[
      html.Img(
        src=src,
        className=classes_names.SMALL_CARD_ICON
      ),
      html.H2(value),
      html.H5(title)
    ],
    className=classes_names.SINGLE_VALUE_CARD+theme,
  )
# '..assets/test.png'