def apply_twice(funx,arg):
    return funx(funx(arg))

def add_ten(arg):
    return arg+10

print(apply_twice(add_ten,10))


