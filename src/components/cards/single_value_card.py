import dash_bootstrap_components as dbc
from dash import Dash, html


def render(app: Dash, value: str, title:str, icon: str) -> dbc.Col:
  """(Dash, str, str, str, str) -> Col
  create the card of the single value 
  app: is the app
  value: is the value shown in the middle
  title: is title shown in the bottom
  src: the src of the picture
  """
  return dbc.Col(
    dbc.Card(
      html.Div(
        children=[
          html.I(
            className=icon+' fa-3x'
          ),
          html.H2(value),
          html.H5(title)
        ],
        className="d-flex flex-column text-center h-100",
      )
    )
  )
# '..assets/test.png'