def test():
    a, b = 4, 5
    print(a, b)


def test2(a=1, b=False, c='Hello'):
    print(a, b, c)


test()
test2()
test2(2, True, 'Bye')