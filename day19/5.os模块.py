# os.getcwd()获取当前的目录
# os.chdir(dirname)改变当前工作目录
# os.makedirs(dirname) 递归生成文件夹
# os.removedirs(dirname) 递归删除文件夹直到不为空
# os.listdir(dirname) 展示目录下的所有文件
# os.stat(dir) 查看文件状态
# os.sep 输入系统的路径分隔符
# os.system(bash) 执行系统中的命令 无返回值
# os.popen(bash).read()  执行系统中的命令 有返回值
# os.path.abspath(path) 返回path规范化的绝对路径
# os.path.split(path) 将path分割成目录和文件名二元组返回
# os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path) 返回path的大小

# 相对路径只能在包最外层使用
# 绝对路径随意调用 不能随意挪动
import sys
print(sys.path)