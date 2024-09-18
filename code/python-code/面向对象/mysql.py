from pymysql import Connection

conn=Connection(
    host='localhost',              #ip
    port=3306,                      #端口
    user='root',                     #账户
    password='20041123zzx.',     #密码
    autocommit=True              #自动提交

)
#获取到游标对象
cursor=conn.cursor()

#选择数据库
conn.select_db('exercise')
"""
#执行sql
cursor.execute('select * from exercise.students')

results=cursor.fetchall()
for i in results:
    print(i)
"""

#执行sql
cursor.execute("insert into exercise.students values(13,'FASD',20,'女')")
# #通过commit确认
# conn.commit()



conn.close()