class Dog:
    legs=4
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def voice(self):
        return '汪汪汪'

class Cat:
    legs=4
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def voice(self):
        return '喵喵喵'

class Goat:
    legs=4
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def voice(self):
        return '咩咩咩'
        
        
dog1=Dog('Pluto','yellow')
dog2=Dog('Hali','Black')
print(dog1.name)
print(dog1.legs)
print(dog2.voice())
