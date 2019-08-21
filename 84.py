v1=[5000,6000,5500,8000,12000,20000,5200]
"""
def fun20(arg):
    return arg*1.2

print(list(map(fun20,v1)))
"""
print(list(map(lambda x: x*1.2,v1)))
