import dash_bootstrap_components as dbc
from dash import Dash, html
from sqlite3 import Cursor

from . import barh_card
from ...utilities import ids, database_map as d_map
from ...utilities.source import DataSource


def render(
    source: DataSource
) -> dbc.Col:
  '''(Cursor) -> Col
  Create the card that hold horizontal bar chart
  '''

  data1 = source.order_sale_product(
    d_map.PRICE, 'Revenue', 'Pizza Name',
    True
  )

  plot1 = barh_card.render(
      'Top 5 Pizzas by Revenue',
      'Revenue', 'Pizza Name', 'blue',
      data1, ids.TOP_REVENUE
    )


  data2 = source.order_sale_product(
    d_map.QUANTITY, 'Quantity', 'Pizza Name',
    True
  )

  plot2 = barh_card.render(
      'Top 5 Pizzas by Quantity',
      'Quantity', 'Pizza Name', 'green',
      data2, ids.TOP_QUANTITY
    )

  data3 = source.order_sale_product(
    d_map.ORDER_ID, 'Total Order', 'Pizza Name',
    True, 'COUNT'
  )

  plot3 = barh_card.render(
      'Top 5 Pizzas by Total Orders',
      'Total Order', 'Pizza Name', 'brown',
      data3, ids.TOP_TOTAL
    )

  data4 = source.order_sale_product(
    d_map.PRICE, 'Revenue', 'Pizza Name',
  )

  plot4 = barh_card.render(
      'Worst 5 Pizzas by Revenue',
      'Revenue', 'Pizza Name', 'blue',
      data4, ids.WORST_REVENUE
    )

  data5 = source.order_sale_product(
    d_map.QUANTITY, 'Quantity', 'Pizza Name'
  )

  plot5 = barh_card.render(
      'Worst 5 Pizzas by Quantity',
      'Quantity', 'Pizza Name', 'green',
      data5, ids.WORST_QUANTITY
    )

  data6 = source.order_sale_product(
    d_map.ORDER_ID, 'Total Order', 'Pizza Name',
    func='COUNT'
  )

  plot6 = barh_card.render(
      'Worst 5 Pizzas by Total Orders',
      'Total Order', 'Pizza Name', 'brown',
      data6, ids.WORST_TOTAL
    )

  return dbc.Col(
    [
      dbc.Row(
        [
          plot1,
          plot2,
          plot3
        ],
      ),
      html.Br(),
      dbc.Row(
        [
          plot4,
          plot5,
          plot6
        ],
      )
    ],
    className='d-flex flex-column w-100'
  )