class Map2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __sub__(self,other):
        return Map2D(self.x-other.x,self.y-other.y)

first_pos=Map2D(10,4)
second_pos=Map2D(8,8)
L=second_pos-first_pos
print(L.x,L.y)




