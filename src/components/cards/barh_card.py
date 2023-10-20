import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from . import top_cards
from ...utilities import classes_names, ids, fetch2df


def render(
    app: Dash, cursor: Cursor, title: str,
    x: str, y: str, theme: str,
    quire: str
) -> html.Div:
  '''(Dash) -> Div
  Create the card that hold horizontal bar chart
  '''

  data = fetch2df.get_quire_result(cursor, quire)

  fig = px.bar(
    data_frame=data,
    x=x,
    y=y,
    orientation='h',
    width='full',
  )

  fig.update_layout(
    # bgcolor='#000',
    xaxis=dict(
        visible=False,
        zeroline=False,
        showline=False,
        # showlabel=False,
        showticklabels=False,
        showgrid=False,
        domain=[0, 0.42],
    )
  )

  annotations = []

  for i in range(data.shape[0]):
    print(i)
    temp = data.iloc[i, :]
    annotation = {
      'xref': 'x1', 'yref': 'y1',
      'x': temp[x], 'y': temp[y],
      'bgcolor': '#fff',
      'text': str(temp[x]),
      'font': {
        'family': 'Arial', 'size' : 20,
        # 'color': 'rgb(50, 171, 96)'
      },
      'showarrow': False
    }

    if temp[x] > 1000:
      annotation['text'] = str(temp[x]/1000) + 'K'

    annotations.append(annotation)

  for a in annotations:
    print(a['text'])

  fig.update_layout(annotations=annotations)

  return html.Div(
    # id=ids.PAGE2,
    children=[
      html.H3(title),
      dcc.Graph(
        figure=fig,
        config={
          # "fillFrame": True,
          # 'frameMargins': True,
          # 'plotGlPixelRatio': True,
          'staticPlot': True
        }
        # style={'width': 1000}
      )
    ],
    className= classes_names.BARH_CARD+theme,
    hidden=False
  )