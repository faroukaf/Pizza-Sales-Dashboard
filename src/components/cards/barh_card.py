import plotly.express as px
import dash_bootstrap_components as dbc
from pandas import DataFrame
from dash import dcc, html
from sqlite3 import Cursor

from . import common_card
from ...utilities import fetch2df

def ids_generator():
    for i in range(1, 7):
      yield f'barh {i}'

ids = ids_generator()

def render(
    title: str, x: str, y: str,
    color: str, data: DataFrame
) -> dbc.Col:
  '''
  Create the card that hold horizontal bar chart
  '''

  data['text'] = data[y] + data[x].apply(lambda x: ' ' + str(x/1000)+'K' if x > 100 else ' ' + str(x))

  plot = px.bar(
    x=data[x],
    y=data[y],
    text=data['text'],
    # marker={
    #   'colorbar': {
    #     'borderwidth': 20
    #   }
    # },
    orientation='h',
    title=title
  )

  # print('data', data)

  plot.update_layout(yaxis={'visible': False, 'showticklabels': False})
  plot.update_traces(marker_color=color)

  return common_card.render(plot, next(ids), .45,  .94, 4)
  # return dbc.Col(
  #   dbc.Card(
  #     dbc.CardBody(
  #       [
  #         dcc.Graph(
  #           figure=plot
  #         ),
  #         # html.H3(title)
  #       ],
  #       className='text-center w-30'
  #     )
  #   )
  # )