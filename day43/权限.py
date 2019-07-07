import pymysql

username = input('>>>输入用户名')
password = input('>>>输入密码')

conn = pymysql.connect(
    host='127.0.0.1',  # 数据库地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='root',  # 密码
    db='host')
cursor = conn.cursor(pymysql.cursors.DictCursor)
# 登录
dl = 'select * from user where username = %s and password = %s'
cursor.execute(dl, [username, password])
ret = cursor.fetchone()
if ret:
    print('登陆成功')
    # 查询权限
    sql = 'select gt.type from g_r left join role on role.rid = g_r.rid LEFT JOIN gt on gt.gid = g_r.gid LEFT join user on user.role_id = role.rid where user.username =%s'
    cursor.execute(sql, username)
    result = cursor.fetchall()
    print(f'当前用户为 {username}')
    print('权限有：', [i['type'] for i in result])
cursor.close()
conn.close()