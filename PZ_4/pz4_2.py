"""2. Дано число A (> 1). Вывести наименьшее из целых чисел K, для которых сумма 1 +
1/2 + ... + 1/K будет больше A, и саму эту сумму."""

while True:
    try:
        A = float(input("Введите A: "))
        if A > 1:
            break
        else:
            print("Ошибка! A должно быть больше 1.")
    except ValueError:
        print("Ошибка! Введите число.")

S = 0
K = 0

while S <= A:
    K += 1
    S += 1 / K

print("K =", K)
print("Сумма:", S)