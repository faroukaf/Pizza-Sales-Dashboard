from dash import dcc, html

from ..utilities import ids, get_metadata


def render() -> html.Div:
  '''
  Create checklist to chose the months
  '''

  months = get_metadata.get_months_names()

  return html.Div(
    children=[
      dcc.Checklist(
        id=ids.MONTHS_CHECKLIST,
        options=[
          {'label': months[m], 'value': m} for m in months
        ]
      )
    ]
  )

