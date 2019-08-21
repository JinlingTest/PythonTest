v1=[1,2,3,4,5,6]
v2=[4,5,6,7,8,9,10]
v3=[1,3,5,7,9]
v4=[1,3,5,9]
#generator
def fun1():
    i=1
    while i<=6:
        yield i
        i+=1
print(list(fun1()))

def fun2():
    i=4
    while i<=10:
        yield i
        i+=1
print(list(fun2()))

def fun3():
    i=1
    while i<=9:
        if i%2==1:
            yield i
        i+=1
print(list(fun3()))

def fun4():
    i=1
    while i<=9:
        if i%2==1:
            if i!=7:
              yield i
        i+=1
print(list(fun4()))







"""
def fun2():
    return 10

print(fun2())
"""
