v1=[0,1,2,3,4,5,6,7]
print(v1)
v2=[i                      for i in range(10)]
print(v2)
v3=[i*2                   for i in range(11)]
print(v3)

v4=[i    for i in range(11)         if i%2==0]
print(v4)

print("列表 0-20之间的3的倍数的值 ")
v5=[i  for i in range(1,20)  if i%3==0]
print(v5)

v6=[i*20 for i in range(1000000)]
print(v6)

