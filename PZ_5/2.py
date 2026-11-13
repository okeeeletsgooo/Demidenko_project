"""Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y (X и Y —
вещественные параметры, являющиеся одновременно входными и выходными). С
ее помощью для данных переменных A, B, C, D последовательно поменять
содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C,
D."""

def Swap(X, Y):
    X, Y = Y, X
    return X, Y

A = float(input("Введи A: "))
B = float(input("Введи B: "))
C = float(input("Введи C: "))
D = float(input("Введи D: "))

A, B = Swap(A, B)
C, D = Swap(C, D)
B, C = Swap(B, C)

print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)