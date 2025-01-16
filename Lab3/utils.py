import numpy as np
import intvalpy as ip

def scalar_to_interval(x, rad):
    return ip.Interval(x - rad, x + rad)

scalar_to_interval_vec = np.vectorize(scalar_to_interval)
