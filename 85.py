#filter 针对列表进行迭代的高阶函数 当函数(用于判断的函数 T  F)
v1=[5000,6000,5500,8000,12000,20000,5200]

def fun1(arg):
    return arg>=8000

print(list(filter(fun1,v1)))

print(list(filter(lambda arg: arg>=8000,v1)))
