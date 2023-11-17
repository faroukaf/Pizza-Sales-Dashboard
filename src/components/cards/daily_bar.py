import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html

from . import common_card
from ...utilities import ids, fetch2df
from ...utilities.source import DataSource, d_map
from ...utilities.get_metadata import get_day_num


def render(
    source: DataSource, title: str,
) -> dbc.Col:
  '''
  Create the card that hold horizontal bar chart
  '''

  data = source.revenue_summary('day')

  data.sort_values(by=['Day'], key=lambda s: [get_day_num(m) for m in s], inplace=True)

  plot = px.bar(
    x=data['Day'],
    y=data['Revenue'],
    labels={
      'x': 'Day',
      'y': 'Revenue (k)'
    },
    title=title
  )

  return common_card.render(plot, ids.DAILY_BAR, .45,  .94, 5)
