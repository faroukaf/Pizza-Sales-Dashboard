import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
from sqlite3 import Cursor

from ...utilities import ids, fetch2df
from ...utilities.get_metadata import get_month_num


def render(
    cursor: Cursor, title: str,
) -> dbc.Col:
  '''
  Create the card that hold horizontal bar chart
  '''

  # def 2

  data = fetch2df.get_quire_result(
    cursor,
    'Select gmn(order_date) as Month,'+\
      'sum(total_price)/1000 as Revenue from pizza group by gmn(order_date);'
    )

  data.sort_values(by=['Month'], key=lambda s: [get_month_num(m) for m in s], inplace=True)

  plot = px.line(
    x=data['Month'],
    y=data['Revenue'],
    labels={
      'x': 'Month',
      'y': 'Revenue (k)'
    },
    orientation='h',
  )

  print('data', data, data.columns, sep='\n')

  # plot.update_layout(yaxis={'visible': False, 'showticklabels': False})
  # plot.update_traces(marker_color=color)

  return dbc.Col(
    dbc.Card(
      dbc.CardBody(
        [
          dcc.Graph(
            id=ids.MONTH_LINEAR,
            figure=plot
          ),
          html.H3(title)
        ],
        className='text-center w-45'
      )
    )
  )