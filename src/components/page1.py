import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, register_page
from dash.dependencies import Input, Output
from sqlite3 import Cursor
from .cards import top_cards, page1_cards
from ..utilities import classes_names, ids


register_page(__name__, path='/')


layout = dbc.Row(
  page1_cards.render(cursor)
)
