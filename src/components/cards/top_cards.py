from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor

from . import single_value_card
from ...utilities import classes_names


def render(app: Dash, data: Cursor, theme: str) -> html.Div:
  """(Dash, Cursor, str) -> Div
  create the card that hold the single value card 
  """

  pics_src = 'assets/'

  data.execute('''
  SELECT CAST(printf("%.2f",SUM(total_price)) AS REAL)
  AS `Total Revenue` FROM pizza;
  ''')

  title1 = data.description[0][0]
  value1 = data.fetchone()[0]
  value1 = str(int(value1/1000)) + 'K'
  pic1 = pics_src + 'profit-growth.png'

  data.execute('''
  SELECT CAST(printf("%.2f",(SUM(total_price) /
  COUNT(DISTINCT order_id))) 
  AS REAL) AS `Average Total Order` FROM pizza;
  ''')

  title2 = data.description[0][0]
  value2 = data.fetchone()[0]
  pic2 = pics_src + 'order-delivery.png'

  data.execute('''
  SELECT SUM(quantity) AS `Total Pizza Sold` FROM pizza
  ''')

  title3 = data.description[0][0]
  value3 = data.fetchone()[0]
  value3 = str(int(value3/1000)) + 'K'
  pic3 = pics_src + 'delivery-man.png'

  data.execute('''
  SELECT COUNT(DISTINCT order_id)
  AS `Total Orders` FROM pizza;
  ''')

  title4 = data.description[0][0]
  value4 = data.fetchone()[0]
  value4 = str(int(value4/1000)) + 'K'
  pic4 = pics_src + 'order-delivery.png'

  data.execute('''
  SELECT CAST(printf("%.2f",(SUM(quantity) /
  COUNT(DISTINCT order_id))) 
  AS REAL) AS `Average Pizza per Order` FROM pizza;
  ''')

  title5 = data.description[0][0]
  value5 = data.fetchone()[0]
  pic5 = pics_src + 'test.png'

  return html.Div(
    children=[
      single_value_card.render(app, value1, title1, pic1, theme),
      single_value_card.render(app, value2, title2, pic2, theme),
      single_value_card.render(app, value3, title3, pic3, theme),
      single_value_card.render(app, value4, title4, pic4, theme),
      single_value_card.render(app, value5, title5, pic5, theme),
    ],
    className=classes_names.SINGLE_VALUE_CARDS+theme
  )
