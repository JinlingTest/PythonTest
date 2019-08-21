v1='Hello World'
print(v1.replace('World','Python'))
print(v1)

#join使用一个字符串 作为分隔符 来连接一个字符列表
v1=['hello','world','python','java']
v2=','
v3=v2.join(v1)
print(v3)

print(','.join(['a','b','c']))
print('\t'.join(['a','b','c']))
print('$$$$$'.join(['a','b','c']))
print(''.join(['a','b','c']))

print('a,b,c'.split(','))
print('a$$$$$b$$$$$c'.split('$$$$$'))

