import dash_bootstrap_components as dbc
from plotly.graph_objects import Figure
from dash import dcc, html


def render(
    plot: Figure, id: str,
    x: float, y: float, width,

) -> dbc.Col:
  '''
  Create a common card for all home page charts
  '''

  

  plot.update_layout(
    title={
      'x': x,
      'y': .94,
      'xanchor': 'right',
      'yanchor': 'top',
      'font': {
        'size': 30,
        'family': 'Times New Roman'
        }
      },
    # title_font_family='Times New Roman',
  )

  plot.layout.template = 'plotly_dark'

  # print('data', data, data.columns, sep='\n')

  return dbc.Col(
    dbc.Card(
      dbc.CardBody(
        [
          dcc.Graph(
            id=id,
            figure=plot
          ),
        ]
      )
    ),
    width=width
  )