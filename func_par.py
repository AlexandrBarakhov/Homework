def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5)
print_params(1.5, 2.5)
print_params(True, False, 'hello')

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [False, 'bye', 10]
values_dict = {'a': 5.5, 'b': 'bye', 'c': 1}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["10", 5]

print_params(*values_list_2, 42)