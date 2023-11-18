import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from .cards import links_card
from ..utilities import ids
from ..utilities.source import DataSource


def render(
    source: DataSource
  ) -> dbc.Col:
  '''(DataSource) -> Col
  Create the side navigator layout of the app
  '''

  return dbc.Col(
          [
            links_card.render(),
            dbc.Container(
              id=ids.SIDE_NIV
            )
          ],
          width=2
        )