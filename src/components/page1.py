'''
Create the page 1 "Home" layout of the app
'''
import dash_bootstrap_components as dbc
from dash import register_page
from .cards import page1_cards


register_page(__name__, path='/')


layout = dbc.Row(
  page1_cards.render(cursor)
)
