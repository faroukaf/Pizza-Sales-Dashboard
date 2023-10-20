from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from .cards import top_cards, barh_card
from ..utilities import classes_names, ids


def render(app: Dash, cursor: Cursor, theme: str) -> html.Div:
  '''(Dash) -> Div
  Create the page 2 layout of the app
  '''

  # @app.callback(
  #   Output(ids.PAGE2, 'children'),
  #   Input(ids.LEFT_PAGE_SWAP, 'n_clicks')
  # )
  # def pfo(_: int) -> list[html.H2]:
  #   print(11)
  #   return [html.H2(44)]

  return html.Div(
    id=ids.PAGE2,
    children=[
      top_cards.render(app, cursor, theme),
      barh_card.render(
        app, cursor, 'Top 5 Pizzas by Total Orders',
        'Total Order', 'Pizza Name', theme,
        """
        SELECT pizza_name As `Pizza Name`,
        count(DISTINCT order_id)
        AS `Total Order` FROM pizza
        GROUP BY pizza_name
        ORDER BY count(DISTINCT order_id) DESC
        LIMIT 5;
        """
      )
    ],
    className= classes_names.PAGE2_LAYOUT+theme,
    hidden=False
  )