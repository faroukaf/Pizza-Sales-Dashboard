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

  # def 2

  # data = fetch2df.get_quire_result(
  #   cursor,
  #   'Select gdn(order_date) as Day,'+\
  #     'sum(total_price)/1000 as Revenue from pizza group by gdn(order_date);'
  #   )
  
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

  # print('data', data, data.columns, sep='\n')

  # plot.update_layout(yaxis={'visible': False, 'showticklabels': False})
  return common_card.render(plot, ids.DAILY_BAR, .45,  .94, 5)

  # return dbc.Col(
  #   dbc.Card(
  #     dbc.CardBody(
  #       [
  #         dcc.Graph(
  #           id=ids.DAILY_BAR,
  #           figure=plot
  #         ),
  #         html.H3(title)
  #       ],
  #       className='text-center w-47'
  #     )
  #   )
  # )