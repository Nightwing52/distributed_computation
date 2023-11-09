from models import Request, SimulationState
from calculate import calculate_force, calculate_density
import numpy as np

THRESHOLD = 10**(-9)
request = Request([0.2, 0.8], [0.2, 0.8], [0.0, 0.0], [0.0, 0.0], [1.0, 1.0], 0.005, 100)

# returns if two ndarrays are numerically close
def is_close_ndarray(a, b):
    return np.linalg.norm(a-b) < THRESHOLD

def test_calculate_force_x():
    request = Request([0.0, 1.0], [0.5, 0.5], [0.0, 0.0], [0.0, 0.0], [2.0, 1.0], 3.0, 500)
    initialState = SimulationState(request)
    force = calculate_force(initialState)
    assert(is_close_ndarray(force, np.matrix([[6, 0], [-6, 0]])))

def test_calculate_force_diag():
    request = Request([0.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0], [1.0, 1.0], 1.0, 500)
    initialState = SimulationState(request)
    force = calculate_force(initialState)
    assert(is_close_ndarray(force, (1.0/(2.0*np.sqrt(2)))*np.matrix([[1.0, 1.0], [-1.0, -1.0]])))

def test_multi_force():
    request = Request([0.5, 1.0, 1.0], [0.5, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 1.0], 1.0, 500)
    initialState = SimulationState(request)
    force = calculate_force(initialState)
    assert(is_close_ndarray(force[0, 0:2], 2**(5.0/2.0)*0.5*np.matrix([1.0, 0.0])))

def test_density():
    request = Request([0.1], [0.1], [0.0], [0.0], [3.0], 1.0, 500)
    state = SimulationState(request)
    assert(is_close_ndarray(calculate_density(state, 2), np.matrix([[12.0, 0.0], [0.0, 0.0]])))