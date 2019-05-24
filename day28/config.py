# logging
# logging.DEBUG 显示debug以上的日志
# http://www.cnblogs.com/Eva-J/articles/7228075.html#_label13
import logging
import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9',
    'ForwardX11': 'yes'
}

config['bitbucket.org'] = {'User': 'hg'}

config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}

with open('example.ini', 'w') as configfile:

    config.write(configfile)

import configparser

config = configparser.ConfigParser()

#---------------------------查找文件内容,基于字典的形式

print(config.sections())  #  []

config.read('example.ini')

print(config.sections())  #   ['bitbucket.org', 'topsecret.server.com']

print('bytebong.com' in config)  # False
print('bitbucket.org' in config)  # True

print(config['bitbucket.org']["user"])  # hg

print(config['DEFAULT']['Compression'])  #yes

print(config['topsecret.server.com']['ForwardX11'])  #no

print(config['bitbucket.org'])  #<Section: bitbucket.org>

for key in config['bitbucket.org']:  # 注意,有default会默认default的键
    print(key)

print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键

print(config.items('bitbucket.org'))  #找到'bitbucket.org'下所有键值对

print(config.get('bitbucket.org',
                 'compression'))  # yes       get方法Section下的key对应的value

import configparser

config = configparser.ConfigParser()

config.read('example.ini')

config.add_section('yuan')

config.remove_section('bitbucket.org')
config.remove_option('topsecret.server.com', "forwardx11")

config.set('topsecret.server.com', 'k1', '11111')
config.set('yuan', 'k2', '22222')

config.write(open('new2.ini', "w"))

# logging
# 扩展性强 写法复杂
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置等级
fh = logging.FileHandler('test.log', encoding='utf-8')  # 写入文件
sh = logging.StreamHandler()  # 控制台输出
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s - %(lineno)d 行 - %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(sh)

logger.debug("test %(key)s" % {'key': '1'})
logger.warning("test")
logger.error("test")

# 简单配置 缺点不能输出中文 可定制差
# import logging
logging.basicConfig(
    level=logging.DEBUG,
    format=
    '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='test.log',
    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
