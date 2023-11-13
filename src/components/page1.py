'''
Create the page 1 "Home" layout of the app
'''
import dash_bootstrap_components as dbc
from dash import register_page
from .cards import page1_cards
from src.utilities import connector



for i in range(100000):
    1+1


def w():
  for i in range(100000):
    1+1

  cursor = connector.connect('data/pizza.db')

  register_page(__name__)#, path='/')


  return dbc.Row(
    page1_cards.render(cursor)
  )


layout = w()
