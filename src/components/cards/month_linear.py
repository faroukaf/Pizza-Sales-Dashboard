import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html

from . import common_card
from ...utilities import ids
from ...utilities.source import DataSource
from ...utilities.get_metadata import get_month_num


def render(
    source: DataSource, title: str,
) -> dbc.Col:
  '''
  Create the card that hold horizontal bar chart
  '''

  data = source.revenue_summary('month')

  data.sort_values(by=['Month'], key=lambda s: [get_month_num(m) for m in s], inplace=True)

  plot = px.line(
    x=data['Month'],
    y=data['Revenue'],
    labels={
      'x': 'Month',
      'y': 'Revenue (k)'
    },
    orientation='h',
    title=title
  )

  return common_card.render(plot, ids.MONTH_LINEAR, .5,  .94, 5)
