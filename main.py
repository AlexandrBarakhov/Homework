import math
a = 1  # переменная типа int
b = 1.5  # переменная типа float
bl = True  # переменная типа bool
print("Hello, World")
print('Hello, World')  # кавычки " "  ' ' равнозначны, применяются чтобы вывести другие кавычки " 'Hello, World' "
print("Hello, \" Sasha \"")  # еще вариант поставить \ перед " чтобы вывести в "  "
print('Hello, \' Tanya \'')  # еще вариант поставить \ перед ' чтобы вывести в '  '
print(a+b)
print(type(a+b))  # вывод типа переменной
print(bl)
del a, b, bl  # удаление переменной
print(2**200)
print(type(2**200))
print(5/2)
print(5//2)  # деление нацело (целочисленное деление)
print(13 % 4)  # остаток от деления
print(math.factorial(7))  # факториал
print(math.trunc(5.85))  # отбросить дробную часть
print(math.sqrt(30))  # квадратный корень
first_str = "Sasha"  # переменная типа str
second_str = "Tanya"
some_str = first_str + second_str  # конкатенация строк
print(some_str)
print("Sasha"+"Tanya")  # или так
print(1 + 1)
print("1" + "1")
print(len(some_str))  # len() длина строки
print(some_str[0])  # первый символ строки (нумерация с 0)
print(some_str[1])  # второй символ строки
print(some_str[:5])  # символы с начала строки до пятого (0, 1, 2, 3, 4)
print(some_str[5:])  # символы с пятого до конца строки (5, 6, 7, 8, 9)
print(some_str[3:8])  # срез строки с четвертого по восьмой символ (3, 4, 5, 6, 7)
print(some_str[-1])  # первый символ с конца строки ( - отсчет с конца, нумерация с 1)
print(some_str[-2])  # второй символ с конца строки
print(some_str[-3:])  # три символа с конца строки
print(some_str[:-3])  # символы с конца строки, начиная с четвертого с конца
name = "Alexandr"
print(name[0:7:2])  # символы с 0 по 7 шагом 2 (0, 2, 4, 6)
print(name[::-2])  # если шаг отрицательный, то элементы выводятся в обратном порядке
print(name.upper())  # upper() - метод для перевода всей строки в верхний регистр
print(name.lower())  # lower() - метод для перевода всей строки в нижний регистр
abra = "Hello, QQQ www EEE rrr TTT yyy UUU iii OOO ppp"
print(abra.upper().lower())  # перевод всей строки сначала в верхний, потом в нижний регистр
print(abra.replace("Hello", "Goodbye"))
print(abra.replace(" ", ""))

print(5 > 3, 3 < 1)  # boolean
print(2/3)
print(int(2/3))  # преобразование типов
print(5/3)
print(int(5/3))
print(float(2))
print(int('234'))
print(float("2.5"))
print(type(str(3.1415)))
print(5 > 3 and 4 == 4 and 7 <= 7 or 3 != 4)
print(bool(5))
print('Hello', 5 > 4, 123)  # здесь вывод разделяется пробелом
print('Hello', 5 > 4, 123, sep="")  # здесь ничем
print('Hello', 5 > 4, 123, sep="|")  # здесь символом |
print(12/11)  # по умолчанию стоит переход на новую строку
print(13/12, end="\n")  # то же самое
print(14/13, end="")  # здесь перехода не будет
print(15/14, end="!\n")
print(16/15, end="!!!!!\n")
print("h\ne\nl\nl\no")
print("h\te\tl\tl\to")  # \t табуляция
print("\\hello\\")  # чтобы вывести сам слеш \ нужно перед ним поставить слеш \
print(min(1, 5, 0, -3, 9))
print(max(1, 5, 0, -3, 9))
print(abs(-3))  # число по модулю
print(pow(3, 2.5))  # возведение в степень ( 3 в степени 2.5 ) то же что и **
print(round(3/2))  # округление как в математике
input()
y = int(input("Введите свой возраст: "))  # функция input с параметром
print("Ваш возраст: ", y)
del y  # удаление переменной
num = 10
num += 2
num -= 5
num *= 7
num /= 3
num //= 4
num %= 6
print(num)
