def fun1(arg1):
    def fun01():
        arg1()
    return fun01()

def fun2():
    print('AAAAAA')

def fun3():
    print('BBBBBBB')

fun1(fun3)
fun1(fun2)

@fun1
def fun4():
    print('CCCCC')


@fun1
def fun4():
    print('CCCCC')




