from dash import Dash

from src.components import create_layout
from src.utilities import connector
# from .src.components.create_layout import render as create_layout

def main() -> None:
  """
  The main app
  """

  app = Dash()
  cursor = connector.connect('data/pizza.db')
  app.layout = create_layout.render(app, cursor)

  app.run(port=4000)


if __name__ == '__main__':
  main()