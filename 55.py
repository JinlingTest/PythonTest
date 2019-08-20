try:
    color={'red':[255,0,0],'green':[0,255,0],'blue':[0,0,255]}
    print(color['red'])
    print(color['red'][0])
    print(color['yellow'])
except KeyError:
    print('所取键名有误')
