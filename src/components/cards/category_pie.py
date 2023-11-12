import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
from sqlite3 import Cursor

from ...utilities import ids, fetch2df


def render(
    cursor: Cursor, title: str,
) -> dbc.Col:
  '''
  Create the card that hold % of each category revenue represented in pie chart
  '''

  # def 2

  data = fetch2df.get_quire_result(
    cursor,
    'Select pizza_category as Category,'+\
      'sum(total_price) as Revenue from pizza group by pizza_category;'
    )

  plot = px.pie(
    names=data['Category'],
    values=data['Revenue'],
  )

  # print('data', data, data.columns, sep='\n')

  return dbc.Col(
    dbc.Card(
      dbc.CardBody(
        [
          dcc.Graph(
            id=ids.CATEGORY_PIE,
            figure=plot
          ),
          html.H3(title)
        ],
        className='text-center w-30'
      )
    )
  )