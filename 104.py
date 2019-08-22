def fun1(x,y):
    if y==0:
        return 1
    else:
        return x*fun1(x,y-1)
#x^y
print(fun1(5,0))    #1
print(fun1(5,1))    #5
print(fun1(5,2))    #5*5
print(fun1(5,3))   #5*5*5
print(fun1(5,4))   #5*5*5*5
