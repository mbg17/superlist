from multiprocessing import Pool
import requests


def get(url):
    ret = requests.get(url)
    if ret.status_code == 200:
        return url, len(ret.content.decode('utf-8'))


def call_back(args):
    url, length = args
    print(url, length)


if __name__ == '__main__':
    p = Pool(5)
    url_list = [
        'http://www.baidu.com', 'http://www.souhu.com', 'http://www.qq.com',
        'http://www.sogou.com'
    ]
    for url in url_list:
        p.apply_async(get, args=(url, ), callback=call_back)
    p.close()
    p.join()
