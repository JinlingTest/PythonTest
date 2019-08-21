#pure Function  返回值依赖于参数 相同的参数 执行任意遍 返回值相同
def fun1(arg):
    return arg*2

def fun2(arg1,arg2):
    return (arg1*2+arg2-10)/(arg1+3)*(arg2-2)

print(fun1(10))
print(fun1(10))
print(fun1(10))
print(fun1(10))

print(fun2(20,30))
print(fun2(20,30))
print(fun2(20,30))
print(fun2(20,30))
