print('программа определяет вид треугольника')
print('введите длины сторон')
a = float(input('сторона a:'))
b = float(input('сторона b:'))
c = float(input('сторона c:'))
print('введены длины:', a, b, c)

if not (a + b <= c or b + c <= a or c + a <= b):  # проверка на треугольность

    if a == b or b == c or c == a:
        print('треугольник равнобедренный')
        if a == b == c:
            print('треугольник равносторонний')

    if a != b != c:
        print('треугольник разносторонний')
        if a*a == b*b + c*c or b*b == c*c + a*a or c*c == a*a + b*b:
            print('треугольник прямоугольный')

else:
    print('это не треугольник')
