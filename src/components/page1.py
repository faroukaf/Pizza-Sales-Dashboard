from dash import Dash, dcc, html

from .cards import page1_cards
from ..utilities import ids
from ..utilities.source import DataSource


def render(
    # app: Dash, 
    source: DataSource
  ) -> html.Div:
  '''(Dash) -> Div
  Create the page 1 layout of the app
  '''

  return html.Div(
    id=ids.PAGE1,
    children=[
      page1_cards.render(source)
    ],
  )