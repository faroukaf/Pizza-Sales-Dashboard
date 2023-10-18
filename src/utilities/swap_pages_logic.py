from dash import Dash
from dash.dependencies import Input, Output
from . import ids

def swap(app: Dash) -> None:
  """(Dash) -> None
  This responsal of the logic of swap pages
  """

  # @app.callback(
  #     [
  #       Output(ids.SWAP_CONTAINER, 'style'),
  #       Output(ids.PAGE1, 'hidden'),
  #       Output(ids.PAGE2, 'hidden'),
  #       # Output(ids.RIGHT_PAGE_SWAP, 'disable_n_clicks')
  #     ],
  #     [
  #       Input(ids.SWAP_CONTAINER, 'style'),
  #       Input(ids.RIGHT_PAGE_SWAP, 'n_clicks')
  #     ]
  # )
  # def do_right(style: dict, _: int) -> (bool, bool, bool):
  #   print(style)
  #   if style['page-number'] == 1:
  #     return {'page-number': 2}, True, False#, True
  #   return {'page-number': 1}, False, True#, False

  # @app.callback(
  #     # Output(ids.SWAP_CONTAINER, 'style'),
  #     [
  #       Input(ids.SWAP_CONTAINER, 'style'),
  #       Input(ids.LEFT_PAGE_SWAP, 'n_clicks')
  #     ]
  # )
  # def do_left(style: dict, right: int) -> dict:
  #   print(style)
  #   # if style['page-number'] == 1:
  #   # return {'page-number': 2}

  @app.callback(
    [
      Output(ids.PAGE1, 'hidden'),
      Output(ids.PAGE2, 'hidden'),
      # Output(ids.HIDDEN_DIV1, 'style')
    ],
    [
      Input(ids.LEFT_PAGE_SWAP, 'n_clicks_timestamp '),
      Input(ids.RIGHT_PAGE_SWAP, 'n_clicks_timestamp ')
    ]
  )
  def do(left: int, right: int) -> (bool, bool, dict):
    if left is not None and right is not None:
      if left > right:
        return False, True
      elif left < right:
        return True, False
    else: 
      print(233)
      return False, False