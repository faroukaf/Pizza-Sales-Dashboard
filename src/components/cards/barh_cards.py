import dash_bootstrap_components as dbc
from dash import html
from sqlite3 import Cursor
from . import barh_card


def render(cursor: Cursor) -> dbc.Col:
  '''(Cursor) -> Col
  Create the card that hold horizontal bar chart
  '''

  plot1 = barh_card.render(
      cursor, 'Top 5 Pizzas by Revenue',
      'Revenue', 'Pizza Name', 'blue',
      """
      SELECT pizza_name As `Pizza Name`,
      sum(total_price)
      AS `Revenue` FROM pizza
      GROUP BY pizza_name
      ORDER BY sum(total_price) DESC
      LIMIT 5;
      """
    )

  plot2 = barh_card.render(
      cursor, 'Top 5 Pizzas by Quantity',
      'Quantity', 'Pizza Name', 'green',
      """
      SELECT pizza_name As `Pizza Name`,
      sum(quantity)
      AS `Quantity` FROM pizza
      GROUP BY pizza_name
      ORDER BY sum(quantity) DESC
      LIMIT 5;
      """
    )

  plot3 = barh_card.render(
      cursor, 'Top 5 Pizzas by Total Orders',
      'Total Order', 'Pizza Name', 'brown',
      """
      SELECT pizza_name As `Pizza Name`,
      count(DISTINCT order_id)
      AS `Total Order` FROM pizza
      GROUP BY pizza_name
      ORDER BY count(DISTINCT order_id) DESC
      LIMIT 5;
      """
    )

  plot4 = barh_card.render(
        cursor, 'Worst 5 Pizzas by Revenue',
        'Revenue', 'Pizza Name', 'blue',
        """
        SELECT pizza_name As `Pizza Name`,
        sum(total_price)
        AS `Revenue` FROM pizza
        GROUP BY pizza_name
        ORDER BY sum(total_price)
        LIMIT 5;
        """
      )

  plot5 = barh_card.render(
        cursor, 'Worst 5 Pizzas by Quantity',
        'Quantity', 'Pizza Name', 'green',
        """
        SELECT pizza_name As `Pizza Name`,
        sum(quantity)
        AS `Quantity` FROM pizza
        GROUP BY pizza_name
        ORDER BY sum(quantity)
        LIMIT 5;
        """
      )

  plot6 = barh_card.render(
      cursor, 'Worst 5 Pizzas by Total Orders',
      'Total Order', 'Pizza Name', 'brown',
      """
      SELECT pizza_name As `Pizza Name`,
      count(DISTINCT order_id)
      AS `Total Order` FROM pizza
      GROUP BY pizza_name
      ORDER BY count(DISTINCT order_id)
      LIMIT 5;
      """
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