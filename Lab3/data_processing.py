import numpy as np
import struct
from utils import scalar_to_interval_vec

def read_bin_file_with_numpy(file_path):
    """
    Reads binary data files and parses frame information.
    """
    with open(file_path, 'rb') as f:
        header_data = f.read(256)
        side, mode_, frame_count = struct.unpack('<BBH', header_data[:4])

        frames = []
        point_dtype = np.dtype('<8H')

        for _ in range(frame_count):
            frame_header_data = f.read(16)
            stop_point, timestamp = struct.unpack('<HL', frame_header_data[:6])
            frame_data = np.frombuffer(f.read(1024 * 16), dtype=point_dtype)
            frames.append(frame_data)

        return np.array(frames)

def get_transformed_values(x_file, y_file):
    """
    Converts raw data to voltage and interval representations.
    """
    x_data = read_bin_file_with_numpy(x_file)
    y_data = read_bin_file_with_numpy(y_file)

    x_voltage = x_data / 16384.0 - 0.5
    y_voltage = y_data / 16384.0 - 0.5

    X = scalar_to_interval_vec(x_voltage, 2 ** -14).flatten()
    Y = scalar_to_interval_vec(y_voltage, 2 ** -14).flatten()

    return X, Y
