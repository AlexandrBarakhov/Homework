'''
Написать программу для подсчёта суммы всех чисел и длин всех строк
Что должно быть подсчитано:
1. Все числа (не важно, являются они ключами или значениям или ещё чем-то).
2. Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.
'''

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
    {'ab': [1, 3, 5], 'cd': (2, 4, 6)}
]

count = 0


# isinstance(obj, int)  # True or False
# isinstance(5, int)  # --> True
# isinstance('5', int)  # --> False

def func(param):
    global count
    if isinstance(param, int):
        count += param
    elif isinstance(param, str):
        count += len(param)
    elif isinstance(param, dict):
        for key, value in param.items():
            func(key)
            func(value)
    elif isinstance(param, (list, tuple, set)):
        for k in param:
            func(k)


for i in data_structure:
    func(i)

print(count)