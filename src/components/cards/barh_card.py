import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
from sqlite3 import Cursor

from ...utilities import fetch2df


def render(
    cursor: Cursor, title: str,
    x: str, y: str, color: str,
    quire: str
) -> dbc.Col:
  '''
  Create the card that hold horizontal bar chart
  '''

  data = fetch2df.get_quire_result(cursor, quire)
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
  )

  # print('data', data)

  plot.update_layout(yaxis={'visible': False, 'showticklabels': False})
  plot.update_traces(marker_color=color)

  return dbc.Col(
    dbc.Card(
      dbc.CardBody(
        [
          dcc.Graph(
            figure=plot
          ),
          html.H3(title)
        ],
        className='text-center w-30'
      )
    )
  )