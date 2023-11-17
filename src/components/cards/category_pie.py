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
  Create the card that hold % of each category revenue represented in pie chart
  '''

  data = source.revenue_summary('category')

  plot = px.pie(
    names=data['Category'],
    values=data['Revenue'],
    hole=.6,
    title=title
  )

  plot.update_traces(
    textinfo='label+text+percent',
    textposition='outside'
  )

  return common_card.render(plot, ids.CATEGORY_PIE, .65,  .94, 3)

