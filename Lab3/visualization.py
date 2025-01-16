import os
import matplotlib.pyplot as plt

def save_plot(plot_func, save_dir, filename):
    """
    Saves a plot to the specified directory.
    """
    os.makedirs(save_dir, exist_ok=True)
    plot_func()
    plt.savefig(os.path.join(save_dir, filename))
    plt.close()
