import json
from datetime import datetime

from dbutils.pooled_db import PooledDB

import pymysql
from pymysql.cursors import DictCursor





class BasePymysqlPool(object):
    def __init__(self):
        self.DB_HOST = "127.0.0.1"
        self.DB_PORT = 3306
        self.DB_DATABASE = 'plant'
        self.DB_USER = "root"
        self.DB_PASSWORD = "123123"
        self.CHARSET = 'utf8'

        self.DB_MIN_CACHED = 3
        self.DB_MAX_CACHED = 5

        self.DB_MAX_CONNECYIONS = 10
        self.DB_BLOCKING = True
        #单个连接重用的最大次数
        self.DB_MAX_USAGE = 3
        self.DB_SET_SESSION = None
        self.DB_CREATOR = pymysql


class dbapi(BasePymysqlPool):
    """
    MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现获取连接对象：conn = Mysql.getConn()
            释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    __pool = None

    def __init__(self):

        super(dbapi, self).__init__()

 #从连接池中提取一个连接
    def __getConn(self):
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        if dbapi.__pool is None:
            __pool = PooledDB(creator=self.DB_CREATOR,
                              mincached=self.DB_MIN_CACHED,
                              maxcached=self.DB_MAX_CACHED,
                              host=self.DB_HOST,
                              port=self.DB_PORT,
                              user=self.DB_USER,
                              passwd=self.DB_PASSWORD,
                              db=self.DB_DATABASE,
                              use_unicode=False,
                              charset=self.CHARSET,
                              cursorclass=DictCursor)
        return __pool.connection()


    def login_authentication(self, username, password):
                conn=self.__getConn()
                cur=conn.cursor()

                sql = "SELECT * FROM user WHERE username = %s AND password = %s"

                cur.execute(sql, (username, password))

                row_count = cur.rowcount
                print(row_count)

                if row_count == 0:
                    cur.close()
                    conn.close()
                    return False
                else:

                    result = list(cur.fetchall())[0]

                    for key,value in result.items():
                        if isinstance(value,bytes):
                            result[key] = value.decode('utf-8')

                    return  result

    def getalldata(self):
        conn = self.__getConn()
        cur = conn.cursor()

        sql = "SELECT * FROM air_quality_data  order by id desc limit 15"

        cur.execute(sql)
        data = cur.fetchall()
        result = {
            'pm1': [int(item['pm1']) for item in data][-7:],
            'pm25': [int(item['pm25']) for item in data][-7:],
            'pm10': [int(item['pm10']) for item in data][-7:],
            'temperature': [float(item['temperature']) for item in data][-7:],
            'humidity': [float(item['humidity']) for item in data][-7:],
            'time': [item['time'].strftime('%Y-%m-%d %H:%M:%S') for item in data][-7:]
        }
        return result

    def insertairqualitydate(self,data_dict):
         conn = self.__getConn()
         cur = conn.cursor()
         data_dict['time']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         columns = ', '.join(data_dict.keys())  # 获取字典的键作为列名
         values = ', '.join(['%s'] * len(data_dict))  # 每个值用占位符'%s'代替

         # 构建 INSERT SQL 语句
         sql = f"INSERT INTO air_quality_data ({columns}) VALUES ({values})"

         # 执行插入操作
         try:
             cur.execute(sql, tuple(data_dict.values()))  # 使用字典的值进行插入
             conn.commit()  # 提交事务
             print("Data inserted successfully.")
         except Exception as e:
             conn.rollback()  # 如果出错则回滚
             print(f"Error inserting data: {e}")
         finally:
             cur.close()
             conn.close()


db=dbapi()


if __name__ == '__main__':
    db.getalldata()