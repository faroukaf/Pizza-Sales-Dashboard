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

  day = source.revenue_summary('day')
  day = day.nlargest(2, day.columns[1])

  day_p1 =  insight_content.render(day, 'First Seller Day', 'text-primary', 'text-warning')
  day_p2 =  insight_content.render(day, 'Second Seller Day', 'text-primary', 'text-warning', 1)

  month = source.revenue_summary('month')
  month = month.nlargest(2, month.columns[1])

  month_p1 =  insight_content.render(month, 'First Seller Month', 'text-primary', 'text-warning')
  month_p2 =  insight_content.render(month, 'Second Seller Month', 'text-primary', 'text-warning', 1)

  return dbc.Row(
          id=ids.SALE_PERFORMANCE,
          children=[
            dbc.Card(
              dbc.CardHeader(
                html.H3('Busiest Day & Month')
              ),
              className='mb-3 text-center'
            ),
            html.Br(),
            dbc.CardBody(
              [
                day_p1,
                day_p2,
                month_p1,
                month_p2
              ]
            )
          ],
        )