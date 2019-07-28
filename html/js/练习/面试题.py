def fun(m):
    for k, v in m.items():
        m[k + 2] = v + 2


m = {1: 2, 3: 4}
l = m
l[9] = 10
# fun(m)
m[7] = 8
# l {3:4,5:6,11:12}
# m {1:2,3:4,7:8}
print(l, m)
