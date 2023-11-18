import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ...utilities import ids, database_map as d_map
from ...utilities.source import DataSource


def render(
    data: pd.DataFrame, based_on: str,
    h4_color: str, p_color: str,
    row: int=0
  ) -> dbc.Row:
  '''(DataSource) -> Col
  Create the content of insight
  '''

  # p3 = f'{data.iloc[0, 0]} is Maximum Total Order'

  head = html.H4(
    based_on,
    className='text-center '+h4_color
  )
  insight = html.Span(
    data.iloc[row, 0],
    className=''+p_color
  )
  maximum = html.Span(
    'The Maximum',
    className='text-danger'
  )

  based = html.Span(
    based_on,
    className='text-info'
  )

  return html.P(
    [
      head,
      insight,
      ' is ',
      maximum,
      ' by ',
      based
    ]
  )