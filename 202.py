class Person:
    weight=50

u01=Person()
u02=Person()
print(u01)
print(type(u01))
u01.name='alice'
u01.sex='F'
u01.age=18
print(u01.name)
print(u01.sex,u01.age)
print(u01.weight)
u02.weight=60
print(u02.weight)

#print(u01.weight)
#AttributeError: 'Person' object has no attribute 'weight'
#
