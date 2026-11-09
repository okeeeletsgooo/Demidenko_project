"""Ввести N чисел. Найти и вывести их среднее арифметическое."""

while True:
    try:
        N = int(input("Введите количество чисел: "))
        if N > 0:
            break
        else:
            print("Ошибка! N должно быть больше 0.")
    except ValueError:
        print("Ошибка! Введите целое число.")

S = 0

for I in range(N):
    while True:
        try:
            A = float(input("Введите число: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")

    S = S + A

C = S / N

print("Среднее арифметическое:", C)