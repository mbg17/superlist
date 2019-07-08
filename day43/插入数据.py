import pymysql

# 增删改
conn = pymysql.connect(
    host='127.0.0.1',  # 数据库地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='root',  # 密码
    db='host')  # 链接的数据库
cursor = conn.cursor()  # 建立游标执行语句
for i in range(3000000):
    sql = 'insert into userlist(name,email,gender) values (%s,%s,%s)'
    cursor.execute(sql, ['陆远%s' % i, '%s@qq.com' % i, '男'])  # 插入单条
    conn.commit()  # 提交事务
    print('执行%s条' % i)
    #cursor.executemany(sql, (['男', 1, '陆远'], ['男', 1, '哈哈']))  # 插入多条
cursor.close()  # 关闭游标
conn.close()  # 关闭连接