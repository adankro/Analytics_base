
from sqlalchemy import create_engine
import pymysql
import pandas as pd

class MysqlExtractor():
    def __init__(self,host:str, user:str, password:str='', pool_recycle:int=36000):
        self.connection_string = 'mysql+pymysql://{}:{}@{}'.format(user,password,host)
        self.pool_recycle = pool_recycle
    
    def export_table_to_excel(self,table_name:str, fields='*', where:str=None) -> pd.DataFrame:
        query = 'SELECT {} from {} '.format(table_name,fields)
        if where:
            query = query + where
        sqlEngine = create_engine(self.connection_string, pool_recycle=self.pool_recycle)
        dbConnection = sqlEngine.connect()
        frame = pd.read_sql(query, dbConnection)
        frame.to_csv('./data/mysql/' + table_name + '.csv')
        #pd.set_option('display.expand_frame_repr', False)
        dbConnection.close()
        return frame