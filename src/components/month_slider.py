from dash import dcc, html

from ..utilities import ids


def render() -> html.Div:
  '''
  Create slider to chose the month
  '''
  return html.Div(
    children=[
      dcc.Slider(
        min=1,
        max=12,
        step=1,
        marks=get_month(),
        value=1,
        tooltip=(lambda x:{i: x[i] for i in range(len(x))})(get_month()),

      )
    ]
  )

def get_month() -> list[str]:
  """
  Get month name for month slider
  """

  return [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'June',
    'July',
    'Aug',
    'Sept',
    'Oct',
    'Nov',
    'Dec',
  ]
