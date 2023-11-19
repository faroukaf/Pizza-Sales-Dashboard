import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

from . import (
  month_linear, daily_bar,
  category_pie, size_pie,
  category_funnel
)
from ...utilities.source import DataSource


def render(source: DataSource) -> dbc.Col:
  '''(Cursor) -> Col
  Create collections of carts in page 1 layout of the app
  '''

  return dbc.Col(
    children=[
      dbc.Row(
        children=[
          daily_bar.render(source, 'Daily Trend for Total Order'),
          month_linear.render(source, 'Monthly Trend for Total Order'),
        ]
      ),
      html.Br(),
      dbc.Row(
        children=[
          category_pie.render(source, '% of Sale by Category'),
          size_pie.render(source, '% of Sale by Size'),
          category_funnel.render(source, 'Total Pizza Soled by Pizza Category')
        ]
      )
    ],
    className='w-100',
    # width=12
  )