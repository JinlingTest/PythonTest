v1=[70,71,80,53,90,65]
v1=[10,11,10,13,10,25]
v2=[10,21,'30',43,50,'65']
v3=['fail','pass','good','excellent']
"""
if all(i>=60   for i in v1):
    print('全部都及格')
else:
    print('有不及格学生')

if any(i>=60   for i in v2):
    print('有及格的')
else:
    print('居然都不及格 ')
"""
"""
print(v3[2])
['fail','pass','good','excellent']
0,fail
1,pass
2,good
3,excellent
"""
for i in enumerate(v3):
    print(i)

for i in enumerate(v3,3):
    print(i)

for i in enumerate(v3,1):
    print(i)






    

