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

  data = source.quantity_summary('category')
  
  data.sort_values('Quantity', inplace=True, ascending=False)

  plot = px.funnel(
    x=data['Category'],
    y=data['Quantity'],
    title=title
    # orientation='h',
    # width=550,
    # height=550
  )

  return common_card.render(plot, ids.CATEGORY_FUNNEL, .7,  .94, 3)

