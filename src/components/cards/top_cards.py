import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor

from . import single_value_card
from ...utilities import classes_names


def render(app: Dash, data: Cursor, theme: str) -> html.Div:
  """(Dash, Cursor, str) -> Div
  create the card that hold the single value card 
  """

  data.execute('''
  SELECT CAST(printf("%.2f",SUM(total_price)) AS REAL)
  AS `Total Revenue` FROM pizza;
  ''')

  title1 = data.description[0][0]
  value1 = data.fetchone()[0]
  value1 = str(int(value1/1000)) + 'K'
  icon1 = 'bi bi-cash-stack'

  data.execute('''
  SELECT CAST(printf("%.2f",(SUM(total_price) /
  COUNT(DISTINCT order_id))) 
  AS REAL) AS `Average Total Order` FROM pizza;
  ''')

  title2 = data.description[0][0]
  value2 = data.fetchone()[0]
  icon2 = 'bi bi-card-list'

  data.execute('''
  SELECT SUM(quantity) AS `Total Pizza Sold` FROM pizza
  ''')

  title3 = data.description[0][0]
  value3 = data.fetchone()[0]
  value3 = str(int(value3/1000)) + 'K'
  icon3 = 'bi bi-bicycle'

  data.execute('''
  SELECT COUNT(DISTINCT order_id)
  AS `Total Orders` FROM pizza;
  ''')

  title4 = data.description[0][0]
  value4 = data.fetchone()[0]
  value4 = str(int(value4/1000)) + 'K'
  icon4 = 'bi bi-cart-check-fill'


  data.execute('''
  SELECT CAST(printf("%.2f",(SUM(quantity) /
  COUNT(DISTINCT order_id))) 
  AS REAL) AS `Average Pizza per Order` FROM pizza;
  ''')

  title5 = data.description[0][0]
  value5 = data.fetchone()[0]
  icon5 = 'fa-solid fa-pizza-slice mt-2 mb-3'

  return dbc.Row(
    children=[
      single_value_card.render(app, value1, title1, icon1, theme),
      single_value_card.render(app, value2, title2, icon2, theme),
      single_value_card.render(app, value3, title3, icon3, theme),
      single_value_card.render(app, value4, title4, icon4, theme),
      single_value_card.render(app, value5, title5, icon5, theme),
    ],
    className='d-flex align-items-stretch'
  )
