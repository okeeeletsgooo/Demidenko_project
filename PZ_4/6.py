"""Ввести N чисел. Посчитать и вывести количество чисел равных нулю."""

while True:
    try:
        N = int(input("Введите количество чисел: "))
        if N > 0:
            break
        else:
            print("Ошибка! N должно быть больше 0.")
    except ValueError:
        print("Ошибка! Введите целое число.")

K = 0

for I in range(N):
    while True:
        try:
            A = float(input("Введите число: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")

    if A == 0:
        K = K + 1

print("Количество нулей:", K)