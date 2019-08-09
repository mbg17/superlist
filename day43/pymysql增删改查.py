import pymysql

# 增删改
conn = pymysql.connect(
    host='127.0.0.1',  # 数据库地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='root',  # 密码
    db='userinfo', # 链接的数据库
    charset='utf8'
)
cursor = conn.cursor()  # 建立游标执行语句
sql = 'insert into info(name,password) values (%s,%s)'
cursor.execute(sql, ['陆远5','123456'])  # 插入单条
cursor.executemany(sql, (['陆远6','12345678'], ['哈哈2','1234567']))  # 插入多条
conn.commit()  # 提交事务
cursor.close()  # 关闭游标
conn.close()  # 关闭连接

# 查
# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',  # 数据库地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='root',  # 密码
    db='userinfo', # 链接的数据库
    charset='utf8'
)
consur = conn.cursor(pymysql.cursors.DictCursor)  # 建立游标执行语句 以字典格式返回结果
sql = "select * from info where id =%(sid)s or name =%(sname)s"
consur.execute(sql, {'sid': 1, 'sname': '陆远'})  # 执行语句
# consur.execute(sql, {'sid': 1, 'sname': '张三'})
ret = consur.fetchone()  # 获取单条结果
# consur.lastrowid() 获取最后插入数据的自增id
# consur.fetchmany(size) 获取指定行数
# consur.fetchall() 获取所有结果 以元祖形式繁华
consur.close()  # 关闭游标
conn.close()
