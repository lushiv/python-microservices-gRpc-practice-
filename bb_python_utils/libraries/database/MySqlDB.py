import mysql.connector.pooling
from bb_python_utils.libraries.database.BaseDB import BaseDatabase


class MysqlDatabase(BaseDatabase):
    __instance = None
    __connected = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.name = 'Mysql Database Singleton'
        return cls.__instance

    def __init__(self, **kwargs):
        """
        :param kwargs:
        """
        self.__cnx_pool = None
        self.pool_name = kwargs.get('mysql_pool_name', 'bb_python_mysql_pool')
        self.pool_size = kwargs.get('mysql_pool_size', 10)
        self.host = kwargs.get('mysql_host', 'localhost')
        self.port = kwargs.get('mysql_port', 3306)
        self.user = kwargs.get('mysql_user', 'root')
        self.password = kwargs.get('mysql_password', 'Mobile@97701')
        self.auth_plugin= kwargs.get('auth_plugin', 'mysql_native_password')
        self.database = kwargs.get('database_name', '')
        super(MysqlDatabase, self).__init__()

    def connect(self):
        """
        :return:
        """
        try:
            self.__cnx_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name=self.pool_name, pool_size=self.pool_size,
                host=self.host, port=self.port,
                user=self.user, passwd=self.password,
                database=self.database,auth_plugin= self.auth_plugin,autocommit=True
            )
            self.__connected = True
        except Exception as e:
            raise e

    def get_connection(self):
        """
        :return:
        """
        try:
            if not self.__connected:
                self.connect()
            return self.__cnx_pool.get_connection()
        except Exception as e:
            raise e

    def commit(self):
        """
        :return:
        """
        try:
            if not self.__connected:
                raise Exception('database is not connected, commit operation cannot be done')
            self.__cnx_pool.commit()
        except Exception as e:
            raise e

    def get_cursor(self):
        """
        :return:
        """
        try:
            if not self.__connected:
                self.connect()
            return self.__cnx_pool.get_connection().cursor(buffered=True) 
        except Exception as e:
            raise e


    def insert_data(self,sql,val):
        try:
            if not self.__connected:
                self.connect()

            connection_object = self.__cnx_pool.get_connection()
            cursor = connection_object.cursor()
            cursor.execute(sql,val)
            cursor.close()
            return cursor.lastrowid

        except Exception as e:
            raise e


    def get_fetch_data(self,query):
            try:
                if not self.__connected:
                    self.connect()

                connection_object = self.__cnx_pool.get_connection()
                cursor = connection_object.cursor()
                cursor.execute(query)
                data = cursor.fetchall()
                return data

            except Exception as e:
                raise e



