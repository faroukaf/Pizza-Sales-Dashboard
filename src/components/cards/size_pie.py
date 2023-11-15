import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
from sqlite3 import Cursor

from . import common_card
from ...utilities import ids, fetch2df


def render(
    cursor: Cursor, title: str,
) -> dbc.Col:
  '''
  Create the card that hold % of each size revenue represented in pie chart
  '''

  # def 2

  data = fetch2df.get_quire_result(
    cursor,
    'Select gzn(pizza_size) as Size,'+\
      'sum(total_price) as Revenue from pizza group by gzn(pizza_size);'
    )

  plot = px.pie(
    names=data['Size'],
    values=data['Revenue'],
    hole=.6,
    title=title
  )

  plot.update_traces(
    textinfo='label+text+percent',
    textposition='outside'
  )
  # plot.add_annotation(dict(x=1, y=0.4,  align='center',
  #                       xref = "paper", yref = "paper",
  #                       showarrow = False, font_size=22,
  #                       text="Gender"))

  print('data', data, data.columns, sep='\n')

  return common_card.render(plot, ids.SIZE_PIE, .52,  .94, 3)


  # return dbc.Col(
  #   dbc.Card(
  #     dbc.CardBody(
  #       [
  #         dcc.Graph(
  #           id=ids.SIZE_PIE,
  #           figure=plot
  #         ),
  #         html.H3(title)
  #       ],
  #       className='text-center w-30'
  #     )
  #   )
  # )