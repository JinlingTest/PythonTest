class Person:
    def __init__(self,name,sex,privateinfo):
        self.name=name
        self.sex=sex
        self.__privateinfo=list(privateinfo)
    def name(self):
        print(self.name)
    def p1(self):
        print('welcome to here')
    def _p2(self):
        print('welcome to nanjing')
    def __p3(self):
        print('welcome to hell')


u01=Person('alice','F',[18,60])
print(u01.name)
print(u01.sex)
print(u01._Person__privateinfo)
u01.p1()
u01._p2()
u01._Person__p3()
