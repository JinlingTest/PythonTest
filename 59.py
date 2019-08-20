try:
    color={'red':[255,0,0],'green':[0,255,0],'blue':[0,0,255]}
    print(color['red'])
    print(color['green'])
    print(color['blue'])
    print(color['yellow'])
except KeyError:
    print('所取键yellow有误 开始添加')
    if 'yellow' not in color:
        color['yellow']=[0,255,255]
