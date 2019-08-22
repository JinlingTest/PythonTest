from itertools import count,cycle,repeat,accumulate,takewhile,product,permutations
#print(list(accumulate([1,20,3,5,5,16,7,28])))
#print(list(accumulate(range(1,20,2))))

list1=[1,2,3,4,5,6,7,8]
list2=[8,10,6,1,2,3,4,5,6,7,8]
#print(list(takewhile(lambda x: x<=5,list2)))
#print(list(takewhile(lambda x: x>=5,list2)))
#print(list(takewhile(lambda x: x%2==0,list2)))
#product_list=['Apple','CellPhone','TV','Computer']
#city=['Nanjing','Shanghai','Hangzhou']
#print(list(product(pproduct,permutationsroduct_list,city)))
#组合
num_list=['a','b','c','d','e','f','g']
print(list(permutations(num_list)))






"""
for i in repeat(20):
    print(i)
"""

"""
for i in cycle([1,2,100]):
    print(i)
"""

"""
for i in count(10):
    print(i)
    if i==20:
      break
"""
