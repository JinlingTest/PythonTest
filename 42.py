#print(open('f01.txt','r').read())
try:
 v1=open('f01.txt','r')
 print(v1.read())
except:
    print(1)
finally:
  v1.close()
