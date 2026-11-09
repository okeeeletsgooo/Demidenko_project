"""Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1)."""

while True:
    try:
        N = int(input("Введите N: "))
        if N > 1:
            break
        else:
            print("Ошибка! N должно быть больше 1.")
    except ValueError:
        print("Ошибка! Введите целое число.")

S = 0
F = 1

for I in range(1, N + 1):
    F = F * I
    S = S + F

print("Сумма факториалов:", S)