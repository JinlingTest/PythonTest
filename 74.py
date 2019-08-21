def myadd1(arg1,arg2):
    return arg1+arg2
def mymul1(arg21,arg22):
    return arg21*arg22
def mymul2(arg1):
    return arg1*2
def myfun1(func,arg1):
    return func(func(arg1))

v1=100
v2=mymul2
print(mymul2(10))
print(v2(10))
print(myfun1(mymul2,100))
print(myfun1(v2,v1))



"""
v1=10
v2=20
print(myadd1(v1,v2))

v3=30
v4=40
print(mymul1(v3,v4))
"""
