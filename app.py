from dash import Dash, dcc, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from src.components import create_layout
from src.utilities import connector, ids
from src.utilities.source import DataSource
# from .src.components.create_layout import render as create_layout

def main() -> None:
  """
  The main app
  """

  themes = {'dark': dbc.themes.DARKLY, 'light': dbc.themes.QUARTZ}
  theme = 'dark'

  # @callback(
  #   Output(ids.PAGE1, 'style'),
  #   Input(ids.THEME_BUTTON, 'on'),
  # )
  # def change_theme(what: bool) -> dict:
  #   if what:
  #     theme = 'dark'
  #   else:
  #     theme = 'light'

  #   return {}

  LOCALE = 'en'
  app = Dash(
    __name__,
    external_stylesheets=[
      themes[theme],
      dbc.icons.BOOTSTRAP,
      dbc.icons.FONT_AWESOME
    ]
  )
  # cursor = connector.connect('data/pizza.db')
  source = DataSource('data/pizza.db')
  # 
  app.layout = create_layout.render(app, source)

  app.run(port=4000, debug=True)


if __name__ == '__main__':
  main()