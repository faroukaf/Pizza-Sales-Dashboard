import dash_bootstrap_components as dbc
from dash import Dash


from . import single_value_card
from ...utilities import database_map as d_map
from ...utilities.source import DataSource

def render(app: Dash, source: DataSource) -> dbc.Row:
  """(Dash, Cursor, str) -> Row
  create the card that hold the single value card 
  """

  title1 = 'Total Revenue'
  value1 = source.summary(d_map.PRICE)
  value1 = '{:.2f}'.format(value1/1000) + 'K'
  icon1 = 'bi bi-cash-stack'

  title2 = 'Average Total Order'
  value2 = source.summary(d_map.PRICE, 'AVG')
  value2 = '{:.2f}'.format(value2)
  icon2 = 'bi bi-card-list'

  title3 = 'Total Pizza Sold'
  value3 = source.summary(d_map.QUANTITY)
  value3 = '{:.2f}'.format(value3/1000) + 'K'
  icon3 = 'bi bi-bicycle'

  title4 = 'Total Orders'
  value4 = source.summary(d_map.ORDER_ID, 'COUNT D')
  value4 = '{:.2f}'.format(value4/1000) + 'K'
  icon4 = 'bi bi-cart-check-fill'

  title5 = 'Pizza per Order'
  value5 = source.summary(d_map.QUANTITY, 'AVG')
  value5 = '{:.2f}'.format(value5)
  icon5 = 'fa-solid fa-pizza-slice mt-2 mb-3'

  return dbc.Row(
    children=[
      single_value_card.render(app, value1, title1, icon1),
      single_value_card.render(app, value2, title2, icon2),
      single_value_card.render(app, value3, title3, icon3),
      single_value_card.render(app, value4, title4, icon4),
      single_value_card.render(app, value5, title5, icon5),
    ],
    className='d-flex align-items-stretch w-70'
  )
