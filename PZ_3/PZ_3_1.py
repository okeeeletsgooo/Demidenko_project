"""1. Даны два целых числа A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечётное»."""

while True:
    try:
        A = int(input("Введите первое число: "))
        B = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка! Введите целые числа.")

if A % 2 != 0 or B % 2 != 0:
    print(True)
else:
    print(False)