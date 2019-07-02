import pymysql
# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',  # 数据库地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='root',  # 密码
    db='db1')  # 链接的数据库
consur = conn.cursor()  # 建立游标执行语句
sql = "select * from student where sid =%(sid)s or sname =%(sname)s"
consur.execute(sql, {'sid': 1, 'sname': '张三'})  # 执行语句
# consur.execute(sql, {'sid': 1, 'sname': '张三'})
ret = consur.fetchone()  # 获取结果
consur.close()  # 关闭游标
conn.close()  # 关闭连接
print(ret)
