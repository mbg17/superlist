from gevent import monkey
monkey.patch_all()
import requests
import gevent


def get_url(url):
    ret = requests.get(url)
    content = ret.content.decode('utf-8')
    return url, len(content)


url_list = [
    'http://www.baidu.com',
    'http://www.taobao.com',
    'http://www.hao123.com',
    'http://www.sohu.com',
    'http://www.cnblogs.com',
]
g_list = []
for i in url_list:
    g = gevent.spawn(get_url, i)
    g_list.append(g)
gevent.joinall(g_list)
print([g.value for g in g_list])