import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from . import (
  month_linear, daily_bar,
  category_pie, size_pie,
  category_funnel
)
from ...utilities import classes_names, ids


def render(cursor: Cursor) -> dbc.Col:
  '''(Dash) -> Col
  Create collections of cards in page 1 layout of the app
  '''

  return dbc.Col(
    children=[
      dbc.Row(
        children=[
          daily_bar.render(cursor, 'Daily Trend for Total Order'),
          month_linear.render(cursor, 'Monthly Trend for Total Order'),
        ]
      ),
      html.Br(),
      dbc.Row(
        children=[
          category_pie.render(cursor, '% of Sale by Category'),
          size_pie.render(cursor, '% of Sale by Size'),
          category_funnel.render(cursor, 'Total Pizza Soled by Pizza Category')
        ]
      ),
    ],
  )