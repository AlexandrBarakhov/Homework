'''
На числовой прямой даны два отрезка: [𝑎1; 𝑏1] и [𝑎2; 𝑏2].
Напишите программу, которая находит их пересечение.
Гарантируется, что 𝑎1 < 𝑏1 и 𝑎2 < 𝑏2.
Пересечением двух отрезков может быть:
•отрезок;
•точка;
•пустое множество.

a, b, c, d = 1, 3, 2, 4  result — > 2 3

a, b, c, d = 1, 2, 3, 4  result — > пустое множество

'''

a1, b1, a2, b2 = map(int, input('введите интервалы через пробел').split())
# a1, b1 = int(input()), int(input())
# a2, b2 = int(input()), int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
elif a1 == b2:
    print('точка', a1)
elif a2 == b1:
    print('точка', a2)
elif a1 < a2 and b1 < b2:
    print('отрезок', a2, b1)
elif a1 > a2 and b1 > b2:
    print('отрезок', a1, b2)
elif a1 >= a2 and b1 <= b2:
    print('отрезок', a1, b1)
elif a1 <= a2 and b1 >= b2:
    print('отрезок', a2, b2)
