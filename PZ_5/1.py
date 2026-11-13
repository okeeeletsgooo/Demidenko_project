"""1. Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры."""

import random

def search_figure(k):
    a = k // 1000
    b = k // 100 % 10
    c = k // 10 % 10
    d = k % 10

    if a == b or a == c or a == d or b == c or b == d or c == d:
        return True
    return False

k = random.randint(1000, 9999)

print("Сгенерированное число:", k)

if search_figure(k):
    print("Есть одинаковые цифры.")
else:
    print("Одинаковых цифр нет.")