from models import Request
import numpy as np

THRESHOLD = 10**(-9)
request = Request([0.2, 0.8], [0.2, 0.8], [0.0, 0.0], [0.0, 0.0], [1.0, 1.0], 0.005, 100)

# returns if two ndarrays are numerically close
def is_close_ndarray(a, b):
    return np.linalg.norm(a-b) < THRESHOLD