v1=input('PLS Input a NUm: ')

if int(v1)>0:
    print(v1+"大于零")
    if int(v1)>100:
        print(v1+"大于一百")
else:
    if int(v1)<0:
        print(v1+"小于零")
    else:
        print(v1+"等于零")  

print('判断完毕')        
