from pymysql import Connection
import json
conn=Connection(
    host='localhost',
    password='20041123zzx.',
    user='root',
    port=3306
)

f=open("d:/123.txt","a",encoding='UTF-8')

#游标
cursor=conn.cursor()

#选择数据库
conn.select_db('py_sql')

cursor.execute("select * from py_sql.orders")
results=cursor.fetchall()
data_dict={}


for i in results:

    data_dict["date"]=str(i[0])
    data_dict["order_id"]=i[1]
    data_dict["money"]=int(i[2])
    data_dict["proxince"]=i[3]
    f.write(json.dumps(data_dict,ensure_ascii=False))

f.close()

conn.close()