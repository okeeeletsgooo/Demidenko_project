""" Вывести первые N (N≥3) чисел Фибоначчи и посчитать количество четных чисел."""

while True:
    try:
        N = int(input("Введите N: "))
        if N >= 3:
            break
        else:
            print("Ошибка! N должно быть не меньше 3.")
    except ValueError:
        print("Ошибка! Введите целое число.")

A = 0
B = 1
K = 0

for I in range(N):
    print(A)

    if A % 2 == 0:
        K = K + 1

    C = A + B
    A = B
    B = C

print("Количество четных чисел:", K)