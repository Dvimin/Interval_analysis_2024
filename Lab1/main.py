
import math
import numpy as np
from interval import Interval
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

# Установка точности Decimal
getcontext().prec = 50

def determinant_with_interval(matrix, alpha):
    """
    Вычисляет детерминант матрицы, используя интервалы.
    """
    i1 = Interval(Decimal(matrix[0][0]) - alpha, Decimal(matrix[0][0]) + alpha)
    i2 = Interval(Decimal(matrix[0][1]) - alpha, Decimal(matrix[0][1]) + alpha)
    i3 = Interval(Decimal(matrix[1][0]) - alpha, Decimal(matrix[1][0]) + alpha)
    i4 = Interval(Decimal(matrix[1][1]) - alpha, Decimal(matrix[1][1]) + alpha)
    return i1 * i4 - i2 * i3

def find_upper_limit(matrix):
    """
    Находит верхнюю границу alpha, для которой det(matrix, alpha) не содержит 0.
    """
    alpha = Decimal(1)
    while 0 not in determinant_with_interval(matrix, alpha):
        alpha *= Decimal(2)  # Ускоренный рост alpha
    return alpha

def find_alpha(matrix, tolerance=1e-18):
    """
    Использует метод половинного деления для поиска alpha.
    """
    a = Decimal(0)
    b = find_upper_limit(matrix)
    iterations = 0

    alpha_values = []
    determinants = []

    while b - a > tolerance:
        mid = (a + b) / 2
        alpha_values.append(mid)
        determinants.append(determinant_with_interval(matrix, mid))

        if 0 in determinant_with_interval(matrix, mid):
            b = mid
        else:
            a = mid

        iterations += 1

    alpha = (a + b) / 2
    alpha_values.append(alpha)
    determinants.append(determinant_with_interval(matrix, alpha))

    return alpha_values, determinants

if __name__ == '__main__':
    # Исходная матрица
    mid_matrix = np.array([
        [Decimal('1.05'), Decimal('0.95')],
        [Decimal('1.0'), Decimal('1.0')],
    ])

    # Поиск alpha
    alphas, dets = find_alpha(mid_matrix, 1e-5)

    # Печать результатов
    print("Число итераций:", len(alphas))
    print("Последнее значение alpha:", alphas[-1])

    # Теоретическое значение alpha
    theoretical_alpha = Decimal('0.025')

    # Построение графиков
    iterations = np.arange(len(alphas))
    alphas = np.array(alphas, dtype=float)

    # Относительная погрешность
    deltas = np.abs(alphas - float(theoretical_alpha)) / float(theoretical_alpha)
    exp_decay = np.exp(-iterations)

    # График изменения alpha
    plt.plot(iterations, alphas, label="alpha")
    plt.xlabel('Итерации')
    plt.ylabel('alpha')
    plt.title('Изменение alpha')
    plt.grid()
    plt.show()

    # График погрешности
    plt.semilogy(iterations, deltas, label='Относительная погрешность')
    plt.semilogy(iterations, exp_decay, label='exp(-k)')
    plt.xlabel('Итерации')
    plt.ylabel('Ошибка')
    plt.legend()
    plt.grid()
    plt.show()
