from dash import Dash, dcc, html

from . import month_slider
from ..utilities import classes_names

THEME = 'dark'


def render(app: Dash) -> html.Div:
  '''(Dash) -> Div
  Create the layout of the app
  '''
  return html.Div(
    children=[
      month_slider.render()
    ],
    className= classes_names.MAIN_LAYOUT + THEME
  )