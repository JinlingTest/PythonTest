class Person:
    def __init__(self,name,sex,age):  #self代表 调用该method的instance
        self.name=name
        self.sex=sex  
        self.age=age

    def greeting(self):
         #print('hi 你好 i am ')
        return 'hi 你好 我是  '+self.name

u01=Person('alice','F',18)
u02=Person('bob','M',19)
print(u01.name,u01.sex,u01.age)
#print(u01.greeting()+u01.name)     
print(u01.greeting())
