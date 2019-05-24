#1,luyuan,23,13020166103,IT
# 定义取数规则
dic={'name':1,'id':0,'age':2,'telephone':3,'job':4}
def read_file(filename):
    with open(filename,encoding='utf-8') as f:
        for i in f:
            view_list=i.split(',')
            yield view_list
# 去除符合条件的所有数据
def filter_detail(detail):
    g = read_file('userinfo')
    if '>' in detail:
        if '=' in detail:
            col, val =detail.strip().split('>=')
            for i in g:
                if int(i[dic[col.strip()]])>=int(val.strip()):
                    yield i
        else:
            col, val = detail.strip().split('>')
            for i in g:
                if int(i[dic[col.strip()]])>int(val.strip()):
                    yield i
    if '<' in detail:
        if '=' in detail:
            col, val =detail.strip().split('<=')
            for i in g:
                if int(i[dic[col.strip()]])<=int(val.strip()):
                    yield i
        else:
            col, val =detail.strip().split('<')
            for i in g:
                if int(i[dic[col.strip()]])>int(val.strip()):
                    yield i
    if '=' in detail:
        col, val = detail.strip().split('=')
        for i in g:
            if int(i[dic[col.strip()]]) == int(val.strip()):
                yield i
# 根据字段提取数据
def views(tj,shuju):
    if tj =='*':
        views=['id','name','age','telephone','job']
    else:
        views = tj.strip().split(',')
    for s in shuju:
        lists = []
        for v in views:
            lists.append(s[dic[v.strip()]].strip())
        print(lists)


ret = 'select id, name, age where age <=19'
result= ret.split('where')
val = result[0].replace('select','').strip()
tiaojian = result[1].strip()
views(val,filter_detail(tiaojian))