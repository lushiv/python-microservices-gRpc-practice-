class BaseDatabase:
    def __init__(self):
        pass

    def connect(self):
        raise NotImplemented

    def get_connection(self):
        raise NotImplemented

    def close(self):
        raise NotImplemented

    def destroy(self):
        raise NotImplemented

    def execute_query(self):
        raise NotImplemented

    def execute_transaction(self):
        raise NotImplemented

    def commit(self):
        raise NotImplemented

    def get_cursor(self):
        raise NotImplemented
