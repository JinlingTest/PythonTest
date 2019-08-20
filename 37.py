def myadd(n1,n2):
    return str(n1+n2)
def mysub(n1,n2):
    return str(n1-n2)
def mymul(n1,n2):
    return str(n1*n2)
def mydiv(n1,n2):
    return str(n1/n2)
while True:
    print('=====这是一个加减乘除四则运算的脚本，请按提示输入所需的运算符号和运算数字======')
    print('如果你需要加法,请输入+')
    print('如果你需要减法,请输入-')
    print('如果你需要乘法,请输入*')
    print('如果你需要除法,请输入/')
    print('如果退出，输入Q或q')
    v1=input('在此输入运算符号: ')

    if v1=='Q' or v1=='q':
        break
    elif v1=='+':
        n1=int(input('Enter First Num: ')) 
        n2= int(input('Enter Second Num: ')) 
        print('你的答案是：'+myadd(n1,n2))
    elif v1=='-':
        n1=int(input('Enter First Num: '))
        n2=int(input('Enter Second Num: '))
        print('你的答案是：'+mysub(n1,n2))
    elif v1=='*':
        n1=int(input('Enter First Num: '))
        n2=int(input('Enter Second Num: '))
        print('你的答案是：'+mymul(n1,n2))
    elif v1=='/':
        n1=int(input('Enter First Num: '))
        n2=int(input('Enter Second Num: '))
        print('你的答案是：'+mydiv(n1,n2))
