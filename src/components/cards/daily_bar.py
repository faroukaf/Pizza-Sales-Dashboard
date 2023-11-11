import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
from sqlite3 import Cursor

from ...utilities import ids, fetch2df
from ...utilities.get_metadata import get_day_num


def render(
    cursor: Cursor, title: str,
) -> dbc.Col:
  '''
  Create the card that hold horizontal bar chart
  '''

  # def 2

  data = fetch2df.get_quire_result(
    cursor,
    'Select gdn(order_date) as Day,'+\
      'sum(total_price)/1000 as Revenue from pizza group by gdn(order_date);'
    )

  data.sort_values(by=['Day'], key=lambda s: [get_day_num(m) for m in s], inplace=True)

  plot = px.bar(
    x=data['Day'],
    y=data['Revenue'],
    labels={
      'x': 'Day',
      'y': 'Revenue (k)'
    },
  )

  print('data', data, data.columns, sep='\n')

  # plot.update_layout(yaxis={'visible': False, 'showticklabels': False})
  # plot.update_traces(marker_color=color)

  return dbc.Col(
    dbc.Card(
      dbc.CardBody(
        [
          dcc.Graph(
            id=ids.DAILY_BAR,
            figure=plot
          ),
          html.H3(title)
        ],
        className='text-center w-47'
      )
    )
  )