try:
    print(1)
    #1+'1'
    raise TypeError
    print(2)
except   ZeroDivisionError:
    print(3)

