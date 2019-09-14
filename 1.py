s = "a,b"
d = [{'key': 'a'}, {'key': 'b'}, {'key': 'c'}]

for i in d:
    if list(i.values())[0] in [x for x in s.split(",")]:
        i['flag'] = '1'
    else:
        i['flag'] = '0'
print(d)