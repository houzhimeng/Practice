from queue import Queue
import pymysql
from pymysql.cursors import DictCursor
import threading


class ConnectionPool:
    def __init__(self, size, *args, **kwargs):
        self._pool = Queue(size)
        self.args = args
        self.kwargs = kwargs
        for x in range(size):
            self._pool.put(self._connect())
        self.local = threading.local()

    def _connect(self):
        return pymysql.connect(*self.args, **self.kwargs)

    def _close(self, conn):
        conn.close()

    def __enter__(self):
        try:
            return self.local.cursor
        except AttributeError:
            self.local.idx, self.local.cursor = self._get().cursor()
            return self.local.cursor

    def __exit__(self, *args):
        self.local.cursor.connection.commit()
        self._return_resource(self.local.idx)
        self.local.cursor.close()
        del self.local.cursor
        del self.local.idx

    def get(self):
        return self._pool.get()

    def return_resource(self, conn):
        self._pool.put(conn)


if __name__ == '__main__':
    cp = ConnectionPool(10, host='192.168.1.109',
                          port=3306,
                          user='root',
                          password='123..com',
                          database='demo',
                          cursorclass=DictCursor)

    conn = cp.get()
    with conn as cur:
        with cur:
            cur.execute('''SELECT 1 ''')






