class Animal:                                  #superclass
        legs=4
        def __init__(self,name,color):
           self.name=name
           self.color=color
        def action(self):
             return 'running'
class Brid(Animal):
    legs=2
    def voice(self):
        return '啾啾啾'
    def action(self): #子类Method设置的覆盖超类Method
        return 'flying '+super().action() #super()调用超类
class Dog(Animal):     #subclass
     def voice(self):
        return '汪汪汪'
class Cat(Animal):
    def voice(self):
        return '喵喵喵'
    def action(self,arg1):
            return '静悄悄的走'+arg1
class Butterfly(Animal):
    legs=6      #子类Attribute设置的覆盖超类Attribute
    def voice(self):
        return '-----'
    def action(self,): #子类Method设置的覆盖超类Method
        return 'flying'

cat1=Cat('tom','deepBlue')
print(cat1.name,cat1.legs,cat1.voice(),cat1.action('YYYY'))
butterfly1=Butterfly('alice','White')
print(butterfly1.name,butterfly1.action())
brid1=Brid('wanda','red')
print(brid1.name,brid1.color,brid1.legs,brid1.action())
cat1.name
    
