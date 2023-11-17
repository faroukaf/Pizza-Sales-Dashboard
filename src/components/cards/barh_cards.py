import dash_bootstrap_components as dbc
from dash import Dash, html
from sqlite3 import Cursor

from . import barh_card
from ...utilities import database_map as d_map
from ...utilities.source import DataSource


def render(
    source: DataSource
) -> dbc.Col:
  '''(Cursor) -> Col
  Create the card that hold horizontal bar chart
  '''

  # cursor = connector.connect('....data/pizza.db')

  # plot1 = barh_card.render(
  #     cursor, 'Top 5 Pizzas by Revenue',
  #     'Revenue', 'Pizza Name', 'blue',
  #     """
  #     SELECT pizza_name As `Pizza Name`,
  #     sum(total_price)
  #     AS `Revenue` FROM pizza
  #     GROUP BY pizza_name
  #     ORDER BY sum(total_price) DESC
  #     LIMIT 5;
  #     """
  #   )
  

  data1 = source.order_sale_product(
    d_map.PRICE, 'Revenue', 'Pizza Name',
    True
  )

  plot1 = barh_card.render(
      'Top 5 Pizzas by Revenue',
      'Revenue', 'Pizza Name', 'blue',
      data1
    )

  # plot2 = barh_card.render(
  #     cursor, 'Top 5 Pizzas by Quantity',
  #     'Quantity', 'Pizza Name', 'green',
  #     """
  #     SELECT pizza_name As `Pizza Name`,
  #     sum(quantity)
  #     AS `Quantity` FROM pizza
  #     GROUP BY pizza_name
  #     ORDER BY sum(quantity) DESC
  #     LIMIT 5;
  #     """
  #   )
  

  data2 = source.order_sale_product(
    d_map.QUANTITY, 'Quantity', 'Pizza Name',
    True
  )

  plot2 = barh_card.render(
      'Top 5 Pizzas by Quantity',
      'Quantity', 'Pizza Name', 'green',
      data2
    )

  # plot3 = barh_card.render(
  #     cursor, 'Top 5 Pizzas by Total Orders',
  #     'Total Order', 'Pizza Name', 'brown',
  #     """
  #     SELECT pizza_name As `Pizza Name`,
  #     count(DISTINCT order_id)
  #     AS `Total Order` FROM pizza
  #     GROUP BY pizza_name
  #     ORDER BY count(DISTINCT order_id) DESC
  #     LIMIT 5;
  #     """
  #   )
  

  data3 = source.order_sale_product(
    d_map.ORDER_ID, 'Total Order', 'Pizza Name',
    True, 'COUNT'
  )

  plot3 = barh_card.render(
      'Top 5 Pizzas by Total Orders',
      'Total Order', 'Pizza Name', 'brown',
      data3
    )

  # plot4 = barh_card.render(
  #       cursor, 'Worst 5 Pizzas by Revenue',
  #       'Revenue', 'Pizza Name', 'blue',
  #       """
  #       SELECT pizza_name As `Pizza Name`,
  #       sum(total_price)
  #       AS `Revenue` FROM pizza
  #       GROUP BY pizza_name
  #       ORDER BY sum(total_price)
  #       LIMIT 5;
  #       """
  #     )

  data4 = source.order_sale_product(
    d_map.PRICE, 'Revenue', 'Pizza Name',
  )

  plot4 = barh_card.render(
      'Worst 5 Pizzas by Revenue',
      'Revenue', 'Pizza Name', 'blue',
      data4
    )

  # plot5 = barh_card.render(
  #       cursor, 'Worst 5 Pizzas by Quantity',
  #       'Quantity', 'Pizza Name', 'green',
  #       """
  #       SELECT pizza_name As `Pizza Name`,
  #       sum(quantity)
  #       AS `Quantity` FROM pizza
  #       GROUP BY pizza_name
  #       ORDER BY sum(quantity)
  #       LIMIT 5;
  #       """
  #     )
  
  data5 = source.order_sale_product(
    d_map.QUANTITY, 'Quantity', 'Pizza Name'
  )

  plot5 = barh_card.render(
      'Worst 5 Pizzas by Quantity',
      'Quantity', 'Pizza Name', 'green',
      data5
    )

  # plot6 = barh_card.render(
  #     cursor, 'Worst 5 Pizzas by Total Orders',
  #     'Total Order', 'Pizza Name', 'brown',
  #     """
  #     SELECT pizza_name As `Pizza Name`,
  #     count(DISTINCT order_id)
  #     AS `Total Order` FROM pizza
  #     GROUP BY pizza_name
  #     ORDER BY count(DISTINCT order_id)
  #     LIMIT 5;
  #     """
  #   )
  
  data6 = source.order_sale_product(
    d_map.ORDER_ID, 'Total Order', 'Pizza Name',
    func='COUNT'
  )

  plot6 = barh_card.render(
      'Worst 5 Pizzas by Total Orders',
      'Total Order', 'Pizza Name', 'brown',
      data6
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
    className='d-flex flex-column'
  )