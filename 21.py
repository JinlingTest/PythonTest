while True:
    print('Please Input your choose')
    print('如果你需要加法,请输入+')
    print('如果你需要减法,请输入-')
    print('如果你需要乘法,请输入*')
    print('如果你需要除法,请输入/')
    print('如果退出，输入Q')
    v1=input('Your Choose: ')

    if v1=='Q':
        break
    elif v1=='+':
        n1=input('Enter First Num: ')
        n2=input('Enter Second Num: ')
        print('你的答案是：'+str(int(n1)+int(n2)))
    elif v1=='-':
        n1=input('Enter First Num: ')
        n2=input('Enter Second Num: ')
        print('你的答案是：'+str(int(n1)-int(n2)))
    elif v1=='*':
        n1=input('Enter First Num: ')
        n2=input('Enter Second Num: ')
        print('你的答案是：'+str(int(n1)*int(n2)))
    elif v1=='/':
        n1=input('Enter First Num: ')
        n2=input('Enter Second Num: ')
        print('你的答案是：'+str(int(n1)/int(n2)))
    else:
        continue
