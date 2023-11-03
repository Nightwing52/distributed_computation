from models import Request, Response, SimulationState
import numpy as np

def simulate(request : Request) -> Response:
    states : list[SimulationState] = [SimulationState(request)] # carries current state and state before that
    output : Response = Response([])
    
    states.append(first_step(states[0]))

    for i in range(2, request.get_T()):
        F : np.matrix = calculate_force(states[-1])

        # TODO: update state and append new density to output
        


        

    return Response([])

# performs first step of Verlet integration
def first_step(initialState : SimulationState) -> SimulationState:
    return initialState

# calculates force given state and puts result in [N, 2] matrix of the form [Fx, Fy]
def calculate_force(state : SimulationState) -> np.matrix:
    # TODO: implement
    F : np.matrix = np.matrix(np.zeros([len(state.get_xList()), 2]))

    return F

# calculates density given state
def calculate_density(state : SimulationState) -> np.matrix:
    # TODO: implement
    return np.matrix(np.zeros([2, 2]))