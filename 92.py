def pbanner(arg):
    def wrap():
        print('================')
        arg()
        print('================')
    return wrap()

def fun01():
    print('AAAAAAAAAA')
    print('BBBBBBBBBBBB')
    print('CCCCCCCCCCC')

def fun02():
    print('XXAAAAAAAAAA')
    print('YYBBBBBBBBBBBB')
    print('ZZCCCCCCCCCCC')


pbanner(fun02)



