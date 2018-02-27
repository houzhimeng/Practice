import pymysql
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='192.168.1.109', port=3306, user='root', password='123..com')
try:
    with conn as cur:
        # cur.execute('''insert into demo.`author` (name, country) value ("houzhimeng14", "zh")''')

        def get_name(name='hzm'):
            query =  '''SELECT * FROM demo.`author` WHERE `name` = %(name)s'''
            cur.execute(query, {'name': 'hzm'})
            ret = cur.fetchone()
            print(ret)
finally:
    conn.close()




#连接池
