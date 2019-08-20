try:
    print(1)
    raise NameError("This Is Invalide name！！")
    print(2)
except NameError:
    print(3333)
