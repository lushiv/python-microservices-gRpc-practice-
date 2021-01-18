from bb_python_utils.libraries.database.BaseDB import BaseDatabase


class MongoDatabase(BaseDatabase):
    __instance = None
    __connected = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.name = 'Mongo Database Singleton'
        return cls.__instance

    def __init__(self):
        super(MongoDatabase, self).__init__()
        print('mongo db class')
        pass
