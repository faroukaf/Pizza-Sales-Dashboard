import dash_daq as daq
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

from .cards import page1_cards
from ..utilities import ids
from ..utilities.get_metadata import get_months_names as gmn
from ..utilities.source import DataSource


def render(
    # app: Dash, 
    source: DataSource
  ) -> dbc.Col:
  '''(DataSource) -> Col
  Create the top bar of the app
  '''
  MONTHS = gmn()

  return html.Div(
    # id=ids.PAGE1,
    children=[
      dcc.Dropdown(
        id=ids.MONTHS_DROPDOWN,
        options=[
          {'label': x, 'value': MONTHS[x]} for x in MONTHS
        ],
        # title='months'
      ),
      dcc.Dropdown(
        id=ids.CATEGORY_DROPDOWN,
        options=[],
        # title='category'
      ),
      dcc.Dropdown(
        id=ids.LOCALE,
        options=[],
        # title='locale'
      ),
      daq.BooleanSwitch(id=ids.THEME_BUTTON, )
    ],
    className='d-flex w-100'
  )