import os
import shutil
import matplotlib.pyplot as plt
from correction import Ab_correction, A_correction, b_correction
from emptiness import emptinessTol
from visualization import draw_Tol
import intvalpy as ip

# Определение матриц и векторов
A1 = ip.Interval([
    [[0.65, 1.25], [0.7, 1.3]],
    [[0.75, 1.35], [0.7, 1.3]]
])
b1 = ip.Interval([[2.75, 3.15],
                  [2.85, 3.25]])

A2 = ip.Interval([
    [[0.65, 1.25], [0.70, 1.3]],
    [[0.75, 1.35], [0.70, 1.3]],
    [[0.8, 1.4], [0.70, 1.3]]
])
b2 = ip.Interval([
    [2.75, 3.15],
    [2.85, 3.25],
    [2.90, 3.3]
])
A3 = ip.Interval([
    [[0.65, 1.25], [0.70, 1.3]],
    [[0.75, 1.35], [0.70, 1.3]],
    [[0.8, 1.4], [0.70, 1.3]],
    [[-0.3, 0.3], [0.70, 1.3]]
])
b3 = ip.Interval([
    [2.75, 3.15],
    [2.85, 3.25],
    [2.90, 3.3],
    [1.8, 2.2],
])
As = [A1, A2, A3]
bs = [b1, b2, b3]
names_graphics = ["Матрица 2x2", "Матрица 3x2", "Матрица 4x2"]

# Функция для настройки папок
def setup_folders(base_folder="plots"):
    if os.path.exists(base_folder):
        shutil.rmtree(base_folder)
    os.makedirs(base_folder)
    subfolders = ["A_correction", "b_correction", "Ab_correction", "Without_correction"]
    for subfolder in subfolders:
        os.makedirs(os.path.join(base_folder, subfolder))

# Функция для сохранения графиков
def save_plot(fig, folder, filename):
    filepath = os.path.join(folder, filename)
    fig.savefig(filepath)
    print(f"Сохранено: {filepath}")

# Функция для выполнения коррекции Ab
def run_ab_correction():
    print("____Ab-correction____")
    folder = os.path.join("plots", "Ab_correction")
    fig_Ab = plt.figure(figsize=(15, 6))
    fig_Ab_2D = plt.figure(figsize=(15, 5))
    for i in range(len(As)):
        A_ = As[i]
        b_ = bs[i]
        A_, b_ = Ab_correction(A_, b_)

        emptiness_, maxX, maxTol = emptinessTol(A_, b_)

        ax = fig_Ab_2D.add_subplot(131 + i)
        vertices = ip.IntLinIncR2(A_, b_, consistency='tol', show=False)

        for v in vertices:
            if len(v) > 0:
                x, y = v[:, 0], v[:, 1]
                ax.fill(x, y, linestyle='-', linewidth=1, color='#FFFF00', alpha=0.5)
                ax.scatter(x, y, s=0, color='black', alpha=1)

        # Добавляем точку максимума и легенду с координатами точки максимума
        scatter = ax.scatter(maxX[0], maxX[1], color='red', s=50, zorder=5,
                             label=f"Точка максимума: ({maxX[0]:.2f}, {maxX[1]:.2f})")
        ax.legend()

        # Добавляем сетку на график
        ax.grid(True)

        print(emptiness_, maxX, maxTol)
        print("A_cor = ", A_)
        print("b_cor = ", b_)

        axs = fig_Ab.add_subplot(131 + i, projection='3d')
        axs.set_title(names_graphics[i])
        draw_Tol(A_, b_, maxX, maxTol, axs)

    fig_Ab.tight_layout()
    fig_Ab_2D.tight_layout()
    save_plot(fig_Ab, folder, "3D_plot.png")
    save_plot(fig_Ab_2D, folder, "2D_plot.png")
    plt.show()


def run_a_correction():
    print("____A-correction____")
    folder = os.path.join("plots", "A_correction")
    fig_A = plt.figure(figsize=(15, 6))
    fig_A_2D = plt.figure(figsize=(15, 5))
    for i in range(len(As)):
        A_ = As[i]
        b_ = bs[i]
        A_ = A_correction(A_, b_)
        emptiness_, maxX, maxTol = emptinessTol(A_, b_)

        ax = fig_A_2D.add_subplot(131 + i)
        vertices = ip.IntLinIncR2(A_, b_, consistency='tol', show=False)

        for v in vertices:
            if len(v) > 0:
                x, y = v[:, 0], v[:, 1]
                ax.fill(x, y, linestyle='-', linewidth=1, color='#FFFF00', alpha=0.5)
                ax.scatter(x, y, s=0, color='black', alpha=1)

        scatter = ax.scatter(maxX[0], maxX[1], color='red', s=50, zorder=5,
                             label=f"Точка максимума: ({maxX[0]:.2f}, {maxX[1]:.2f})")
        ax.legend()
        ax.grid(True)

        axs = fig_A.add_subplot(131 + i, projection='3d')
        axs.set_title(names_graphics[i])
        draw_Tol(A_, b_, maxX, maxTol, axs)

    fig_A.tight_layout()
    fig_A_2D.tight_layout()
    save_plot(fig_A, folder, "3D_plot.png")
    save_plot(fig_A_2D, folder, "2D_plot.png")
    plt.show()


# Функция для выполнения коррекции b
def run_b_correction():
    print("____b-correction____")
    folder = os.path.join("plots", "b_correction")
    fig_b = plt.figure(figsize=(15, 6))
    fig_b_2D = plt.figure(figsize=(15, 5))
    for i in range(len(As)):
        A_ = As[i]
        b_ = bs[i]
        b_ = b_correction(b_)
        emptiness_, maxX, maxTol = emptinessTol(A_, b_)

        ax = fig_b_2D.add_subplot(131 + i)
        vertices = ip.IntLinIncR2(A_, b_, consistency='tol', show=False)

        for v in vertices:
            if len(v) > 0:
                x, y = v[:, 0], v[:, 1]
                ax.fill(x, y, linestyle='-', linewidth=1, color='#FFFF00', alpha=0.5)
                ax.scatter(x, y, s=0, color='black', alpha=1)

        scatter = ax.scatter(maxX[0], maxX[1], color='red', s=50, zorder=5,
                             label=f"Точка максимума: ({maxX[0]:.2f}, {maxX[1]:.2f})")
        ax.legend()
        ax.grid(True)

        print("b_cor = ", b_)

        axs = fig_b.add_subplot(131 + i, projection='3d')
        axs.set_title(names_graphics[i])
        draw_Tol(A_, b_, maxX, maxTol, axs)

    fig_b.tight_layout()
    fig_b_2D.tight_layout()
    save_plot(fig_b, folder, "3D_plot.png")
    save_plot(fig_b_2D, folder, "2D_plot.png")
    plt.show()


# Функция без коррекции
def run_without_correction():
    print("____Without correction____")
    folder = os.path.join("plots", "Without_correction")
    fig = plt.figure(figsize=(15, 6))
    for i in range(len(As)):
        A_ = As[i]
        b_ = bs[i]
        emptiness_, maxX, maxTol = emptinessTol(A_, b_)
        print(emptiness_, maxX, maxTol)
        axs = fig.add_subplot(131 + i, projection='3d')
        axs.set_title(names_graphics[i])
        draw_Tol(A_, b_, maxX, maxTol, axs)
    fig.tight_layout()
    save_plot(fig, folder, "3D_plot.png")
    plt.show()

# Основная функция для запуска
def run(correction=None):
    if correction == "Ab":
        run_ab_correction()
    elif correction == "A":
        run_a_correction()
    elif correction == "b":
        run_b_correction()
    else:
        run_without_correction()

# Настройка папок и вызов функции run
setup_folders()

run("A")
run("b")
run("Ab")
run()