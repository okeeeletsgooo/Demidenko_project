"""Вариант 9.
1. Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N"""

while True:
    try:
        N = int(input("Введите N: "))
        if N > 0:
            break
        else:
            print("Ошибка! N должно быть больше 0.")
    except ValueError:
        print("Ошибка! Введите целое число.")

S = 0
I = 1

while I <= N:
    S += 1 / I
    I += 1

print("Сумма:", S)