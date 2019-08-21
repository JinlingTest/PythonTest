v1=['a','b','c']
v2='abc'
"""
print(v1[1])
print(v2[1])
"""
def fun1():
   v1='哈哈哈哈哈哈'
   x=''
   for i in v1:
       x+=i
       yield x 
print(list(fun1()))
