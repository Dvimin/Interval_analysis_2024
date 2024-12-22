import numpy as np
import matplotlib.pyplot as plt
import intvalpy as ip

# Отключаем расширенную точность в библиотеке intvalpy для повышения производительности
ip.precision.extendedPrecisionQ = False

# Функция для отрисовки поверхности Tol
def draw_Tol(A, b, max_x, max_Tol, axis):
    # Создаем сетку для отрисовки поверхности
    x_1_, x_2_ = np.mgrid[max_x[0] - 2:max_x[0] + 2:100j, max_x[1] - 2:max_x[1] + 2:100j]

    # Создаем массивы значений для осей x1 и x2
    list_x_1 = np.linspace(max_x[0] - 2, max_x[0] + 2, 100)
    list_x_2 = np.linspace(max_x[1] - 2, max_x[1] + 2, 100)

    list_tol = []
    # Рассчитываем значение Tol для каждого сочетания x1 и x2
    for x_1 in list_x_1:
        mas_tol = []
        for x_2 in list_x_2:
            x = [x_1, x_2]
            tol = []
            for i in range(len(b)):
                sum_ = sum([A[i][j] * x[j] for j in range(len(x))])
                tol.append(ip.rad(b[i]) - ip.mag(ip.mid(b[i]) - sum_))

            mas_tol.append(min(tol))

        list_tol.append(np.array(mas_tol))

    # Отрисовываем поверхность Tol
    surface = axis.plot_surface(x_1_, x_2_, np.array(list_tol), cmap='viridis', edgecolor='none', alpha=0.8)

    # Отрисовываем точку максимума
    label_text = f"Максимум: ({max_x[0] :.2f}, {max_x[1] :.2f})"
    axis.scatter(max_x[0], max_x[1], max_Tol, color='red', s=50, zorder=5, label=label_text)

    # Настраиваем подписи осей
    axis.set_xlabel('x₁', fontsize=12)
    axis.set_ylabel('x₂', fontsize=12)
    axis.set_zlabel('Tol', fontsize=12)

    # Добавляем легенду
    axis.legend()
