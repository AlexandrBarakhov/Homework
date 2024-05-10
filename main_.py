def test(text, *params, a=5.5):
    print(text, params, a)


test('hello', 1, 2, 3, 4, 5)
test('bye', 5, 4, 3, 2, 1, a=True)


def fact(n):
    if n > 0:  # 0! = 1  и  1! = 1
        return fact(n - 1) * n
    else:
        return 1


n_max = 15
for i in range(n_max + 1):
    print(i, '! =', fact(i))
