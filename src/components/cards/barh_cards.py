from plotly.subplots import make_subplots
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from . import barh_card
from ...utilities import classes_names, ids


def render(
    app: Dash, cursor: Cursor, theme: str,
) -> html.Div:
  '''(Dash) -> Div
  Create the card that hold horizontal bar chart
  '''

  fig = make_subplots(
    rows=2, cols=3,
    # specs=[[{}, {}, {}], [{}, {}, {}]],
    # shared_xaxes=False, shared_yaxes=False,
    vertical_spacing=.1,
    # horizontal_spacing=.5
  )

  all_annotations = []
  axis_updates = {}

  fig.add_trace(
    barh_card.render(
        all_annotations ,axis_updates,
        cursor, 'Top 5 Pizzas by Revenue',
        'Revenue', 'Pizza Name', 'blue',
        """
        SELECT pizza_name As `Pizza Name`,
        sum(total_price)
        AS `Revenue` FROM pizza
        GROUP BY pizza_name
        ORDER BY sum(total_price) DESC
        LIMIT 5;
        """,
        1
      ),
      1, 1
  )

  fig.add_trace(
    barh_card.render(
        all_annotations ,axis_updates,
        cursor, 'Top 5 Pizzas by Quantity',
        'Quantity', 'Pizza Name', 'green',
        """
        SELECT pizza_name As `Pizza Name`,
        sum(quantity)
        AS `Quantity` FROM pizza
        GROUP BY pizza_name
        ORDER BY sum(quantity) DESC
        LIMIT 5;
        """,
        2
      ),
      1, 2
  )

  fig.add_trace(
    barh_card.render(
        all_annotations ,axis_updates,
        cursor, 'Top 5 Pizzas by Total Orders',
        'Total Order', 'Pizza Name', 'brown',
        """
        SELECT pizza_name As `Pizza Name`,
        count(DISTINCT order_id)
        AS `Total Order` FROM pizza
        GROUP BY pizza_name
        ORDER BY count(DISTINCT order_id) DESC
        LIMIT 5;
        """,
        3
      ),
      1, 3
  )

  fig.add_trace(
    barh_card.render(
        all_annotations ,axis_updates,
        cursor, 'Worst 5 Pizzas by Revenue',
        'Revenue', 'Pizza Name', 'blue',
        """
        SELECT pizza_name As `Pizza Name`,
        sum(total_price)
        AS `Revenue` FROM pizza
        GROUP BY pizza_name
        ORDER BY sum(total_price)
        LIMIT 5;
        """,
        4
      ),
      2, 1
  )

  fig.add_trace(
    barh_card.render(
        all_annotations ,axis_updates,
        cursor, 'Worst 5 Pizzas by Quantity',
        'Quantity', 'Pizza Name', 'green',
        """
        SELECT pizza_name As `Pizza Name`,
        sum(quantity)
        AS `Quantity` FROM pizza
        GROUP BY pizza_name
        ORDER BY sum(quantity)
        LIMIT 5;
        """,
        5
      ),
      2, 2
  )

  fig.add_trace(
    barh_card.render(
        all_annotations ,axis_updates,
        cursor, 'Worst 5 Pizzas by Total Orders',
        'Total Order', 'Pizza Name', 'brown',
        """
        SELECT pizza_name As `Pizza Name`,
        count(DISTINCT order_id)
        AS `Total Order` FROM pizza
        GROUP BY pizza_name
        ORDER BY count(DISTINCT order_id)
        LIMIT 5;
        """,
        6
      ),
      2, 3
  )

  annotations = []

  # print('>>>>>>>>>>>>>>>>>>>>>')

  # # for j in range(len(all_annotations[0])):
  # #   for i in range(len(all_annotations)):
  # #     print(all_annotations[i][j])
  # #     annotations.append(all_annotations[i][j])
  
  # for i in axis_updates:
  #   print(i)
  #   print(axis_updates[i])

  fig.update_layout(**axis_updates)
  fig.update_layout(annotations=annotations)

  return html.Div(
    # id=ids.PAGE2,
    children=[
      dcc.Graph(
        figure=fig,
        config={
          # "fillFrame": True,
          # 'frameMargins': True,
          # 'plotGlPixelRatio': True,
          # 'staticPlot': True
        },
        # style={'width': 1000}
        className= classes_names.BARH_CARD+theme,
      )
    ],
    hidden=False
  )