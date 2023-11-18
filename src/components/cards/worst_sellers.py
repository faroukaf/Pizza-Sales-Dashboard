import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import insight_content
from ...utilities import ids, database_map as d_map
from ...utilities.source import DataSource


def render(
    source: DataSource
  ) -> dbc.Row:
  '''(DataSource) -> Col
  Create insight of which is the worst sellers pizza
  '''

  data1 = source.order_sale_product(
    d_map.PRICE, 'Revenue', 'Pizza Name',
    False, limit=1
  )

  p1 = insight_content.render(data1, 'Revenue', 'text-primary', 'text-warning')

  data2 = source.order_sale_product(
    d_map.QUANTITY, 'Quantity', 'Pizza Name',
    False, limit=1
  )

  p2 = insight_content.render(data2, 'Quantity', 'text-primary', 'text-warning')

  data3 = source.order_sale_product(
    d_map.ORDER_ID, 'Total Order', 'Pizza Name',
    False, 'COUNT', 1
  )

  p3 = insight_content.render(data3, 'Total Order', 'text-primary', 'text-warning')

  return dbc.Row(
          id=ids.WORST_SALES,
          children=[
            dbc.Card(
              dbc.CardHeader(
                html.H3('Worst Sales')
              ),
              className='mb-3 text-center'
            ),
            html.Br(),
            dbc.CardBody(
              [
                p1,
                html.Br(),
                p2,
                html.Br(),
                p3,
                html.Br(),
              ]
            )
          ],
        )