import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from . import top_cards
from ...utilities import classes_names, ids, fetch2df


def render(
    all_annotations: list[list] ,axis_updates: dict,
    cursor: Cursor, title: str,
    x: str, y: str, color: str,
    quire: str, order: int
) -> go.Bar:
  '''
  Create the card that hold horizontal bar chart
  '''

  data = fetch2df.get_quire_result(cursor, quire)

  plot = go.Bar(
    x=data[x],
    y=data[y],
    marker_color=color,
    marker={
      'colorbar': {
        'borderwidth': 20
      }
    },
    orientation='h',
    width=60,
    name=title
  )

  x_axis_layout = dict(
        visible=False,
        zeroline=False,
        showline=False,
        # ,
        showticklabels=False,
        showgrid=False,
        domain=[((order-1)%3)/3, (((order-1)%3)+1)/3],
    )
  
  y_axis_layout = dict(
        visible=False,
        zeroline=False,
        showline=False,
        # showlabel=False,
        showticklabels=False,
        showgrid=False,
        domain=[(order//4)/2, ((order//4)+1)/2],
    )

  annotations = []

  for i in range(data.shape[0]):
    # print(i)
    temp = data.iloc[i, :]
    annotation = {
      'xref': f'x{order}', 'yref': f'y{order}',
      'x': temp[x], 'y': temp[y],
      'bgcolor': '#fff',
      'text': str(temp[x]),
      'font': {
        'family': 'Arial', 'size' : 20,
        # 'color': 'rgb(50, 171, 96)'
      },
      'showarrow': False
    }

    if temp[x] >= 1000:
      annotation['text'] = str(temp[x]/1000) + 'K'

    annotations.append(annotation)

  all_annotations.append(annotations)
  
  axis_updates[f'xaxis{order}'] = x_axis_layout
  axis_updates[f'yaxis{order}'] = y_axis_layout

  return plot