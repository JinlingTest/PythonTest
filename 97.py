def is_even(x):
    if x==0:
      return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_even(10))
print(is_even(11))
print(is_odd(20))
print(is_odd(21))

"""
！！！if x==0 是递归的底线
"""
