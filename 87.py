v1=[1,2,3,4,5,6]
v2=[3,4,5,6,7,8,9,10]

def fun1(m,n):
    i=m
    while i<=n:
        yield i
        i+=1
print(list(fun1(3,10)))


def fun1(m,n):
    for i in range(m,n+1):
        yield i

print(list(fun1(7,15)))        
    
