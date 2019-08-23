class A:
    def __add__(self,obj):
        print('This is Class A 左加 __add__')
    def __radd__(self,obj):
        print('This is Class A 的右加__radd__')
    def __iadd__(self,obj):
        print( 100000000)
    
class B:
    pass

a=A()
b=B()
b+a
a+=b



#a.v1=10
#b.v1=20
#print(a.v1+b.v1)
#
#+ (__add__)

    



