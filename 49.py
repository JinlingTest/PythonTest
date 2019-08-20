try:
  v1=open('f02.txt','w')
  message1='hello python'

  #assert v1.write(message1)==message1
  #assert v1.write(message1)==True

# assert v1.write(message1)==len(message1)
 #print (1)

finally:
    v1.close()
