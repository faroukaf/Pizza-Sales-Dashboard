'''
Create the page 2 "Best/Worst Sale layout of the app
'''
import dash_bootstrap_components as dbc
from dash import register_page
from .cards import barh_cards
from src.utilities import connector


for i in range(100000):
    1+1


def w():
  for i in range(100000):
    1+1

  cursor = connector.connect('data/pizza.db')

  register_page(__name__)#, path='/')


  return dbc.Row(
    barh_cards.render(cursor)
  )

layout = w()

