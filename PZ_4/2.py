"""Ввести 4 числа. Найти и вывести на экран количество четных чисел."""

K = 0

for I in range(4):
    while True:
        try:
            A = int(input("Введите число: "))
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    if A % 2 == 0:
        K = K + 1

print("Количество четных чисел:", K)