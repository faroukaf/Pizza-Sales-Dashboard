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
      'sum(quantity) as Quantity from pizza group by pizza_category;'
    )
  
  data.sort_values('Quantity', inplace=True, ascending=False)

  plot = px.funnel(
    x=data['Category'],
    y=data['Quantity'],
    title=title
    # orientation='h',
    # width=550,
    # height=550
  )

  # plot.update_traces(
  #   textinfo='label+text+percent',
  #   textposition='outside'
  # )

  # print('data', data, data.columns, sep='\n')

  return dbc.Col(
    dbc.Card(
      dbc.CardBody(
        [
          dcc.Graph(
            id=ids.CATEGORY_FUNNEL,
            figure=plot
          ),
          html.H3(title)
        ],
        className='text-center w-30'
      )
    )
  )