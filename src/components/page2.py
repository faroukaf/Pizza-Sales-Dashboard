'''
Create the page 2 "Best/Worst Sale layout of the app
'''
import dash_bootstrap_components as dbc
from dash import register_page
from .cards import barh_cards

register_page(__name__)#, path='/')


layout = dbc.Row(
  barh_cards.render(cursor)
)
