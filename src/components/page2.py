from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from .cards import barh_cards
from ..utilities import ids
from ..utilities.source import DataSource


def render(
    source: DataSource
  ) -> html.Div:
  '''(Dash) -> Div
  Create the page 2 layout of the app
  '''

  return html.Div(
    id=ids.PAGE2,
    children=[
      barh_cards.render(source),
    ],
  )