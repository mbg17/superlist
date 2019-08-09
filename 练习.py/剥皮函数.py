def func(x):
    ret = []
    for i in x:
        if isinstance(i,list):
            for a in func(i):
                ret.append(a)
        else:
            ret.append(i)
    return ret
x=[11,22,33,[1,2,3,[1,23,55]]]
print(func(x))

