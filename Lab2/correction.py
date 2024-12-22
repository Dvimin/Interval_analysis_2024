import copy
import intvalpy as ip
from tabulate import tabulate
from emptiness import emptinessTol

# Функция для коррекции вектора b
def b_correction(b, step=5):
    mid = ip.mid(b)
    new_rad = ip.rad(b) + step
    new_b = [[mid[i] - new_rad[i], mid[i] + new_rad[i]] for i in range(len(mid))]
    return ip.Interval(new_b)

# Функция для коррекции матрицы A
def A_correction(A, b):
    max_tol = ip.linear.Tol.maximize(A, b)
    lower_bound = abs(max_tol[1]) / (abs(max_tol[0][0]) + abs(max_tol[0][1]))
    rad_A = ip.rad(A)
    upper_bound = min(min(row) for row in rad_A)
    e = (lower_bound + upper_bound) / 2

    corrected_A = [
        [[str(A[i][j]._a + e), str(A[i][j]._b - e)] for j in range(len(A[0]))]
        for i in range(len(A))
    ]

    headers = ["Параметр", "Значение"]
    table = [
        ["Пустое множество?", False],
        ["Точка максимума (x)", str(max_tol[0])],
        ["Максимальное Tol", str(max_tol[1])],
    ]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    return ip.Interval(corrected_A)

# Функция для коррекции как матрицы A, так и вектора b
def Ab_correction(A, b):
    emptiness, max_x, max_Tol = emptinessTol(A, b)
    new_A, new_b = copy.deepcopy(A), copy.deepcopy(b)

    while emptiness:
        new_A = A_correction(new_A, new_b)
        emptiness, max_x, max_Tol = emptinessTol(new_A, new_b)
        if not emptiness:
            break
        new_b = b_correction(new_b, step=1)
        emptiness, max_x, max_Tol = emptinessTol(new_A, new_b)

    headers = ["Параметр", "Значение"]
    table = [
        ["Пустое множество?", emptiness],
        ["Точка максимума (x)", ", ".join(map(str, max_x))],
        ["Максимальное Tol", f"{max_Tol:.6f}"],
    ]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    return new_A, new_b
