import intvalpy as ip
from tabulate import tabulate


# Функция для проверки пустоты множества Tol и вычисления максимального Tol
def emptinessTol(A, b):
    # Вычисляем максимальное Tol с помощью функции maximize из библиотеки intvalpy
    maxTol = ip.linear.Tol.maximize(A, b)

    # Проверяем, является ли множество пустым
    emptiness = maxTol[1] < 0

    # Подготавливаем данные для вывода таблицы
    headers = ["Параметр", "Значение"]
    table = [
        ["Пустое множество?", emptiness],
        ["Точка максимума (x)", ", ".join(map(str, maxTol[0]))],
        ["Максимальное Tol", f"{maxTol[1]:.6f}"],
    ]

    # Выводим таблицу с результатами
    print(tabulate(table, headers=headers, tablefmt="grid"))

    # Возвращаем результаты
    return emptiness, maxTol[0], maxTol[1]
