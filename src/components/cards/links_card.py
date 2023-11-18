import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ...utilities import ids, pages
# from ...utilities.source import DataSource


def render(
    # source: DataSource
  ) -> dbc.Col:
  '''(DataSource) -> Col
  Create the side navigator layout of the app
  '''

  return dbc.Col(
          [
            html.A(
              children=[
                html.I(className='bi bi-house-door fa-2x'),
                html.H4(
                  'Home',
                  className='text-primary mt-2'
                )
              ],
              href=f'/{pages.HOME}',
              className='bg-success text-primary d-flex justify-content-around w-100'
            ),
            html.Br(),
            html.A(
              children=[
                html.I(className='bi bi-bar-chart-steps fa-2x'),
                html.H4(
                  'Top/Worst',
                  className='color-secondary mt-2'
                )
              ],
              href=f'/{pages.TOP_AND_WORST}',
              className='bg-primary color-secondary d-flex justify-content-around w-100'
            )
          ],
          # className='d-flex align-items-center'
        )