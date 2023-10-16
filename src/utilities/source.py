"""
This module have DataSource object that help handel data the right way
"""
import sqlite3
from dataclasses import dataclass

@dataclass
class DataSource:
    """
    DataSource object help handel data the right way
    """
    _cursor: sqlite3.Cursor

    def doit(self):
        pass  
