import pymysql
#创建连接配置
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123123',db='sqlexample',charset='utf8')

#创建游标
cursor = conn.cursor()

#修改数据
inp = input('请输入:')
r = cursor.execute('insert into student(gendel,class_id,name) values (%s,%s,%s)', inp)
print(r)

#提交
conn.commit()

#游标关闭
cursor.close()

#连接实例关闭
conn.close()