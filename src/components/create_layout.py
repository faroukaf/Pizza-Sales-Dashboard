from dash import (
  Dash,
  dcc, html,
  page_container, page_registry
)
from sqlite3 import Cursor
import dash_bootstrap_components as dbc
from . import page1, page2, swap_pages
from .cards import top_cards
from .cards import top_cards
from ..utilities import classes_names, swap_pages_logic


def render(app: Dash, cursor: Cursor) -> dbc.Container:
  '''(Dash) -> Container
  Create the layout of the app
  '''

  # swap_pages_logic.swap(app)

  return dbc.Container(
    [
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
            top_cards.render(app, cursor),
            page_container

          ],
          width=10
        ),
        dbc.Col(
          [
            # Navigation buttons,
            # Inside container
          ],
          width=2
        )
      ]
    )
    ]
  )