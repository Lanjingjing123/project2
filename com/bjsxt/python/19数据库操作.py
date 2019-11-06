from pymysql import  *
conn = connect("localhost","ljj","ljj","pythonDb",3306)
cur=conn.cursor()
# 查询
count = cur.execute("select * from user")
print(count)
result = cur.fetchall()
for i in result:
    print(i)
    pass
# conn.close()

# # 添加记录
# count = cur.execute("insert into user values(2,'lisi') ")
# print(count)
# #
# sql注入，记得在 %s外面增加''
count=cur.execute("insert into user values(%d,'%s') "%(123,'ads'))
# print(count)

conn.commit()
conn.close()