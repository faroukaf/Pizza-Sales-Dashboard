import dash_bootstrap_components as dbc
from sqlite3 import Cursor
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output

from . import page1, page2, side_nev
from .cards import (
  sale_performance, top_cards, links_card,
  top_sellers, when_busiest, worst_sellers
)
from ..utilities import ids, pages
from ..utilities.source import DataSource


THEME = 'dark'


def render(app: Dash, source: DataSource) -> html.Div:
  '''(DataSource) -> Div
  Create the layout of the app
  '''

  @callback(
        [
          Output(ids.MY_LAYOUT, 'children'),
          Output(ids.SIDE_NIV, 'children')
        ],
        Input(ids.CURRENT_URL, 'pathname')
  )
  def display_page(pathname: str):
      page_path = pathname.split('/')[-1]
      if page_path == pages.HOME:
        page = page1.render(source)

        down_nav = dbc.Container(
          [
            sale_performance.render(source),
            html.Br(),
            html.Br(),
            when_busiest.render(source)
          ]
        )
      elif page_path == pages.TOP_AND_WORST:
        page = page2.render(source)

        down_nav = dbc.Container(
          [
            top_sellers.render(source),
            html.Br(),
            html.Br(),
            worst_sellers.render(source)
          ]
        )
      
      return page, down_nav

  return dbc.Col(
    [
      dcc.Location(
        id=ids.CURRENT_URL,
        refresh=False
      ),
      dbc.Row(
        [
          # Top bar for filter and language and theme
        ]
      ),
      html.Br(),
      dbc.Row(
      [
        dbc.Col(
          [
            links_card.render(),
            html.Br(),
            html.Br(),
            dbc.Container(
              id=ids.SIDE_NIV
            )
          ],
          width=2
        ),
        dbc.Col(
          [
            top_cards.render(app, source),
            html.Br(),
            dbc.Container(id=ids.MY_LAYOUT)

          ],
          width=10
        ),
      ]
    )
    ],
    className='w-100'
  )