#Function Programming
#基于函数的函数 高阶函数将一个函数作为另一个函数的参数 或将其作为结果返回
def fun1(arg1,arg2):
    return arg1(arg2)

def fun1(fun,arg):
    return fun(arg)

def fun2(fun,arg):
    return fun(fun(arg))


def fun3(arg1):
    return arg1**2

#print(fun3(10))

print(fun1(fun3,11))

print(fun2(fun3,11))
v01=11
v02=fun3
print(fun2(v02,v01))
