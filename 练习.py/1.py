list_2 = [
    {
        'name': 'luyuan',
        'hobby': '唱歌'
    },
    {
        'name': 'luyuan',
        'hobby': '看电视'
    },
    {
        'name': 'luyuan',
        'hobby': '读书'
    },
    {
        'name': 'wo',
        'hobby': '鞋子'
    },
    {
        'name': 'wo',
        'hobby': '跳舞'
    },
]
list_4 = []

for i in list_2:
    for item in list_4:
        if i['name'] == item['name']:
            item['hobby_list'].append(i['hobby'])
            break
    else:
        list_4.append({'name': i['name'], 'hobby_list': [i['hobby']]})
print(list_4)
