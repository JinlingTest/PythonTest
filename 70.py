try:
    print(1)
    print(1/0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)


#open('f1.txt','w').write('eee')

try:
    v1=open('f01.txt','r')
    print(v1.read())
finally:
     v1.close()

with open('f01.txt','r') as f:
      print(f.readlines())

try:
    print(1)
    assert 1==2
except AssertionError:
    print(2)
except:
    print(3)

    

















      
      
