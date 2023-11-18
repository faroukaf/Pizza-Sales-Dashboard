"""
This module have DataSource object that help handel data the right way
"""
import pandas as pd
from dataclasses import dataclass

from . import database_map as d_map
from .connector import connect

@dataclass
class DataSource:
    """
    DataSource object help handel data the right way
    """
    # _cursor: sqlite3.Cursor

    def __init__(self, path):
        """(str) -> DataSource
        Create a data source to deal with the data from the path of the database 
        """

        self._cursor = connect(path=path)
        self.table = 'pizza'
        self.SELF_DICT = {
                    'Id': 'pizza_id',
                    'Order Id': 'order_id',
                    'Name Id': 'pizza_name_id',
                    'Quantity': 'quantity',
                    'Order Date': 'order_date',
                    'Order Time': 'order_time',
                    '1s Price': 'unit_price',
                    'Price': 'total_price',
                    'Size': 'pizza_size',
                    'Category': 'pizza_category',
                    'Components/Ingredients': 'pizza_ingredients',
                    'Name': 'pizza_name'
                    }
        self.filter = ''

    def doit(self):
        pass

    def get_columns_names(self) -> list[str]:
        """(list[tuple(str)]) -> list[str]
        Return all columns names from cursor
        """
        out = []

        lis = self._cursor.description

        for i in lis:
            out.append(i[0])

        return out

    def fetch2df(self) -> pd.DataFrame:
        """(Cursor) -> DataFrame
        Turn the fetch result to pandas DataFrame
        """
        result = self._cursor.fetchall()
        df = pd.DataFrame(result, columns=self.get_columns_names())

        return df

    def get_quire_result(self, quire: str) -> pd.DataFrame:
        """
        Get the result of the quire wanted

        quire: is the quire wanted
        cursor: cursor which execute the quire in
        """
        self._cursor.execute(quire)
        data = self.fetch2df()
        # print(data)
        return data

    def order_sale_product(
            self, order_by: str, order_name: str,
            products_category: str='Name', desc: bool=False, func: str='SUM',
            limit: int=5
    ) -> pd.DataFrame:
        """(str, str, bool, int) -> DataFrame
        Return Top or Worst tier for certain characteristics

        order_by: str
        Define which characteristic to order according

        order_name: str
        Define the name of the characteristic on which we order

        products_category: str='Name
        Define how to reference the product

        desc: bool=False
        Define use descending order
        True -> descending -> Top
        False -> ascending -> Worst

        limit: int=5
        Define how want to get

        func: str='SUM'
        Define which function to order according to
        'SUM' -> sum on the attribute
        'COUNT' -> count the attribute distinct appearance
        """

        do = ''

        match func.upper():
            case 'SUM':
                do = f'SUM({self.SELF_DICT[order_by]})'

            case 'COUNT':
                do = f'COUNT(DISTINCT {self.SELF_DICT[order_by]})'

        quire = f'''
                SELECT {self.SELF_DICT[d_map.NAME]} As `{products_category}`,
                {do} AS `{order_name}` FROM {self.table}
                GROUP BY {self.SELF_DICT[d_map.NAME]}
                ORDER BY {do} {int(desc) * 'DESC'}
                LIMIT {limit}
                {self.filter};
                '''
        
        df = self.get_quire_result(quire)

        return df
    
    def summary(self, on_which: str ,func: str='SUM') -> list[str, float]:
        """(str, str) -> list[str, float]
        Return a summary on an attribute

        on_which: str
        Which attribute to get summary on

        func: str='SUM'
        The method of the summary
        'SUM' -> sum on the attribute
        'COUNT' -> count the attribute appearance
        'COUNT D' -> count the attribute distinct appearance
        'AVG' -> evaluate the average of attribute
        """

        do = ''

        match func.upper():
            case 'SUM':
                do = f'SUM({self.SELF_DICT[on_which]})'

            case 'COUNT':
                do = f'COUNT({self.SELF_DICT[on_which]})'

            case 'COUNT D':
                do = f'COUNT(DISTINCT {self.SELF_DICT[on_which]})'

            case'AVG':
                do = f'(SUM({self.SELF_DICT[on_which]}) / COUNT(DISTINCT order_id))'


        quire = f'SELECT {do} from {self.table} {self.filter};'
        print(quire)

        df = self.get_quire_result(quire)
        out = df.iloc[0, 0]

        return out
    
    def revenue_summary(self, based_on: str) -> pd.DataFrame:
        """(str, str) -> list[str, float]
        Return a revenue summary based on an attribute

        based_on: str
        Define over what calculate the revenue
        'day' -> get the daily revenue summary
        'month' -> get the monthly revenue summary
        'year' -> get the yearly revenue summary # not implement yet
        'size' -> get the revenue summary based on size
        'category' -> get the revenue summary based on category
        """

        do = ''
        group_by = ''

        match based_on.lower():
            case 'day':
                do = f'gdn({self.SELF_DICT["Order Date"]}) as Day'
                group_by = f'gdn({self.SELF_DICT["Order Date"]})'

            case 'month':
                do = f'gmn({self.SELF_DICT["Order Date"]}) as Month'
                group_by = f'gmn({self.SELF_DICT["Order Date"]})'

            # case'year':
                # do = f'get_year({self.SELF_DICT["Order Date"]}) as Year'
                # group_by = f'get_year({self.SELF_DICT["Order Date"]})'

            case 'size':
                do = f'gzn({self.SELF_DICT["Size"]}) as Size'
                group_by = f'gzn({self.SELF_DICT["Size"]})'

            case 'category':
                do = f'{self.SELF_DICT["Category"]} as Category'
                group_by = f'{self.SELF_DICT["Category"]}'

        revenue = f'sum({self.SELF_DICT["Price"]})/1000 as Revenue'
        quire = f'SELECT {do}, {revenue} FROM {self.table} GROUP BY {group_by} {self.filter};'
        print(quire)

        df = self.get_quire_result(quire)

        return df
    
    def quantity_summary(self, based_on: str) -> pd.DataFrame:
        """(str, str) -> list[str, float]
        Return a quantity summary based on an attribute

        based_on: str
        Define over what calculate the revenue
        'day' -> get the daily quantity summary
        'month' -> get the monthly quantity summary
        'year' -> get the yearly quantity summary # not implement yet
        'size' -> get the quantity summary based on size
        'category' -> get the quantity summary based on category
        """

        do = ''
        group_by = ''

        match based_on.lower():
            case 'day':
                do = f'gdn({self.SELF_DICT["Order Date"]}) as Day'
                group_by = f'gdn({self.SELF_DICT["Order Date"]})'

            case 'month':
                do = f'gmn({self.SELF_DICT["Order Date"]}) as Month'
                group_by = f'gmn({self.SELF_DICT["Order Date"]})'

            # case'year':
                # do = f'get_year({self.SELF_DICT["Order Date"]}) as Year'
                # group_by = f'get_year({self.SELF_DICT["Order Date"]})'

            case 'size':
                do = f'gzn({self.SELF_DICT["Size"]}) as Size'
                group_by = f'gzn({self.SELF_DICT["Size"]})'

            case 'category':
                do = f'{self.SELF_DICT["Category"]} as Category'
                group_by = f'{self.SELF_DICT["Category"]}'

        quantity = f'sum({self.SELF_DICT["Price"]})/1000 as Quantity'
        quire = f'SELECT {do}, {quantity} FROM {self.table} GROUP BY {group_by} {self.filter};'

        df = self.get_quire_result(quire)

        return df

