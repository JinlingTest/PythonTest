v1='Hello World'
print(v1.replace('World','Python'))
print(v1)
print(v1.upper())
print(v1.lower())
print(v1)

print(v1.startswith('AAA'))
print(v1.startswith('He'))
print(v1.endswith('ld'))

#list
#join使用一个字符串 作为分隔符 来连接一个字符列表
v1=['hello','world','python','java']
v2=','
v3=v2.join(v1)
print(v3)

print('\t'.join(['A','B','C']))
print('\n'.join(['A','B','C']))
print(','.join(['A','B','C']))
print(' '.join(['A','B','C']))



