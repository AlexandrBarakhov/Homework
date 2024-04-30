print('программа определяет среднее из трех чисел')
print('введите три числа')
a1 = float(input('число 1:'))
a2 = float(input('число 2:'))
a3 = float(input('число 3:'))
print('введены числа:', a1, a2, a3)

if not (a1 == a2 or a2 == a3 or a3 == a1):

    if ((a1 > a2) and (a1 < a3)) or ((a1 < a2) and (a1 > a3)):
        print('среднее число:', a1)

    elif ((a2 > a1) and (a2 < a3)) or ((a2 < a1) and (a2 > a3)):
        print('среднее число:', a2)

    else:
        print('среднее число:', a3)

else:
    print('ошибка, все числа должны быть разные')
