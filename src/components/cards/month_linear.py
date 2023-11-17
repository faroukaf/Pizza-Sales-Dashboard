import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html

from . import common_card
from ...utilities import ids, fetch2df
from ...utilities.source import DataSource
from ...utilities.get_metadata import get_month_num


def render(
    source: DataSource, title: str,
) -> dbc.Col:
  '''
  Create the card that hold horizontal bar chart
  '''

  # data = fetch2df.get_quire_result(
  #   cursor,
  #   'Select gmn(order_date) as Month,'+\
  #     'sum(total_price)/1000 as Revenue from pizza group by gmn(order_date);'
  #   )
  
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

  # print('data', data, data.columns, sep='\n')

  # plot.update_layout(yaxis={'visible': False, 'showticklabels': False})
  return common_card.render(plot, ids.MONTH_LINEAR, .5,  .94, 5)

  # return dbc.Col(
  #   dbc.Card(
  #     dbc.CardBody(
  #       [
  #         dcc.Graph(
  #           id=ids.MONTH_LINEAR,
  #           figure=plot
  #         ),
  #         html.H3(title)
  #       ],
  #       className='text-center w-47'
  #     )
  #   )
  # )