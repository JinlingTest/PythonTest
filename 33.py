def fun01(v1,v2):
    return v1+v2
def fun02(v1,v2):
    return v1-v2
def fun03(v1,v2):
    return v1*v2
def fun04(v1,v2):
    return v1/v2
"""
print(fun01(1000,200))
print(fun02(1000,200))
print(fun03(1000,200))
print(fun04(1000,200))
"""
def fun7(v01,v02,v03):
     #return v01+v02
     #return fun6(v01,v02)
     return v03(v01,v02)
print(fun7(1000,2000,fun01))
print(fun7(1000,2000,fun02))
print(fun7(1000,2000,fun03))
print(fun7(1000,2000,fun04))



