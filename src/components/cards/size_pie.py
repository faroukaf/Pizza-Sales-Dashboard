import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html

from . import common_card
from ...utilities import ids, fetch2df
from ...utilities.source import DataSource


def render(
    source: DataSource, title: str,
) -> dbc.Col:
  '''
  Create the card that hold % of each size revenue represented in pie chart
  '''

  data = source.revenue_summary('size')

  plot = px.pie(
    names=data['Size'],
    values=data['Revenue'],
    hole=.6,
    title=title
  )

  plot.update_traces(
    textinfo='label+text+percent',
    textposition='outside'
  )

  print('data', data, data.columns, sep='\n')

  return common_card.render(plot, ids.SIZE_PIE, .52,  .94, 3)

