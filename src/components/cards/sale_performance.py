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
  Create insight of which is the best sellers pizza
  '''

  category_revenue = source.revenue_summary('category')
  # print(day)
  category_revenue = category_revenue.nlargest(1, category_revenue.columns[1])

  category_quantity = source.quantity_summary('category')
  # print(day)
  category_quantity = category_quantity.nlargest(1, category_quantity.columns[1])

  crp =  insight_content.render(category_revenue, 'Category Revenue', 'text-primary', 'text-warning')
  cqp =  insight_content.render(category_quantity, 'Category Quantity', 'text-primary', 'text-warning')

  size_revenue = source.revenue_summary('size')
  # print(day)
  size_revenue = size_revenue.nlargest(1, size_revenue.columns[1])

  size_quantity = source.quantity_summary('size')
  # print(day)
  size_quantity = size_quantity.nlargest(1, size_quantity.columns[1])

  srp =  insight_content.render(size_revenue, 'Size Revenue', 'text-primary', 'text-warning')
  sqp =  insight_content.render(size_quantity, 'Size Quantity', 'text-primary', 'text-warning')

  return dbc.Row(
          id=ids.SALE_PERFORMANCE,
          children=[
            dbc.Card(
              dbc.CardHeader(
                html.H3('Sales Performance')
              ),
              className='mb-4 text-center'
            ),
            html.Br(),
            dbc.CardBody(
              [
                crp,
                cqp,
                srp,
                sqp
              ]
            )
          ],
        )