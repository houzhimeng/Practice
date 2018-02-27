import pymysql
import queue
from pymysql.cursors import  DictCursor

class ConnectionPool:
    def __init__(self, **kwargs):
        self.size = kwargs.pop('size', 10)
        self.idle = kwargs.pop('idle', 3)
        self.kwargs = kwargs
        self.length = 0
        self.connections = queue.Queue(maxsize=self.idle)


    def _connect(self):
        if not self.connections.full():
            conn = pymysql.connect(**self.kwargs)
            self.connections.put(conn)
            self.length += 1
        else:
            raise RuntimeError('erro')

    def _close(self, conn):
        conn.close()
        self.length -= 1


    def get(self, timeout=None):
        if self.connections.empty() and self.length < self.size:
            self._connect()
        return self.connections.get(timeout=timeout)

    def return_resource(self, conn):
        if self.connections.full():
            self._close(conn)
            return
        self.connections.put(conn)


if __name__ == '__main__':
    pool = ConnectionPool(host='192.168.1.109',
                          port=3306,
                          user='root',
                          password='123..com',
                          database='demo',
                          cursorclass=DictCursor)

    conn = pool.get()
    try:
        with conn as cur:
            cur.execute('''SELECT * FROM demo.`author`''')
            for res in cur.fetchall():
                print(res)
    finally:
        pool.return_resource(conn)
