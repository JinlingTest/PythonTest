
def fib(arg):
    if arg==1 or arg==2:
        return 1
    else:
        return fib(arg-2)+fib(arg-1)

print(fib(6))



"""
斐波那契数列
1,1,2,3,5,8,13,21
1--1
2--1
3--2
4--3
......
8--21
"""
