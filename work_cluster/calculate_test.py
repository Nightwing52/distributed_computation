from models import Request, SimulationState
from calculate import calculate_force, calculate_density
import numpy as np

THRESHOLD = 10**(-9)

# returns if two ndarrays are numerically close
def is_close_ndarray(a, b):
    return np.linalg.norm(a-b) < THRESHOLD

def test_calculate_force_x():
    m1 : float = 2.0
    m2 : float = 1.0
    x : list[float] = [0.0, 1.0]
    G : float = 3.0
    request = Request(x, [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [m1, m2], G, 500)
    initialState = SimulationState(request)
    force = calculate_force(initialState)
    rij = np.array([x[1], 0.0])-np.array([x[0], 0.0])
    Fij = G*m1*m2*rij/np.linalg.norm(rij)**3
    print(Fij)
    assert(is_close_ndarray(force, np.array([Fij, -Fij])))

def test_multi_force():
    request = Request([0.5, 1.0, 1.0], [0.5, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 1.0], 1.0, 500)
    initialState = SimulationState(request)
    force = calculate_force(initialState)
    assert(is_close_ndarray(force[0, 0:2], 2**(5.0/2.0)*0.5*np.matrix([1.0, 0.0])))

def test_density():
    m : float = 3.0
    N : int = 2
    request = Request([0.1], [0.1], [0.0], [0.0], [m], 1.0, 500)
    state = SimulationState(request)
    assert(is_close_ndarray(calculate_density(state, N), np.matrix([[m/(1/N**2), 0.0], [0.0, 0.0]])))