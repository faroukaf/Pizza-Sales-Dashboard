from dash import Dash
import dash_bootstrap_components as dbc
from src.components import create_layout
from src.utilities import connector
# from .src.components.create_layout import render as create_layout

def main() -> None:
  """
  The main app
  """

  app = Dash(
    __name__,
    external_stylesheets=[
      dbc.themes.DARKLY,
      dbc.icons.BOOTSTRAP
    ]
  )
  cursor = connector.connect('data/pizza.db')
  app.layout = create_layout.render(app, cursor)

  app.run(port=4000, debug=True)


if __name__ == '__main__':
  main()