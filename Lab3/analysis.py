from matplotlib import pyplot as plt

from data_processing import get_transformed_values
from visualization import save_plot
import os

CONFIG = {
    'images_dir': './images',
    'data_files': {
        'x': './-0.205_lvl_side_a_fast_data.bin',
        'y': './0.225_lvl_side_a_fast_data.bin'
    }
}


def main():
    X, Y = get_transformed_values(
        CONFIG['data_files']['x'], CONFIG['data_files']['y']
    )
    print("Data transformed successfully.")

    def example_plot():
        plt.plot(X, Y)

    save_plot(example_plot, CONFIG['images_dir'], 'scatter.png')

if __name__ == '__main__':
    main()
