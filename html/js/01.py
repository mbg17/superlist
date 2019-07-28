a=('a','b')
b=('c','d')
f=lambda x,y: [{k:v} for k,v in zip(x,y)]
print(f(a,b))