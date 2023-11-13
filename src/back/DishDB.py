import os
import psycopg2 as ps
import pandas as pd
import pymysql
import sqlalchemy

import DishClass

from sqlalchemy import create_engine


class DataBase:
    def __init__(self):
        self._user_name = 'postgres'-m
        self._password = 'SQL_gfccdjhl1'
        self._host = 'localhost'
        self._port = '5432'
        self._db_name = 'test'

        #self.connection = sqlalchemy.engine.Connection
        #self._engine = sqlalchemy.engine

        self._connect_to_db()
        # self.engine = create_engine('postgresql://postgres:SQL_gfccdjhl1@localhost:5432/test')
        # self.connection = engine.connect()

    def _connect_to_db(self):
        self._engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(
            self._user_name, self._password, self._host, self._port, self._db_name))
        print(self._engine)
        self.connection = self._engine.connect()
        print(self.connection)

    def insert_dish_in_db(self,  dish: DishClass, table_name='users'):
        self.connection.execute(sqlalchemy.text(
        '''
        INSERT INTO users (name, age)
        VALUES ('Mike', 22)
        '''
        ))

    def output_table(self, table_name='users'):
        user_table = pd.read_sql(
            '''
            SELECT * FROM users
            ''',
            con=self.connection,
            index_col='id')
        print(user_table)

dish = DishClass
db = DataBase()
db.insert_dish_in_db(dish)
db.output_table()
    # my_query = ''
    # connection.execute(sqlalchemy.text("SELECT * FROM users")).fetchall()
