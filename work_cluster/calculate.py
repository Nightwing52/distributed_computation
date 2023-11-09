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
    #new_x = initialState.get_xList()+(initialState.get_xList()+initialState.get_yList())*initialState.get_delta()+0.5*calculate_force(initialState)/initialState.get_mList()*initialState.get_delta()**2
    return initialState

# calculates force given state and puts result in [N, 2] matrix of the form [Fx, Fy]
def calculate_force(state : SimulationState) -> np.matrix:
    G : float = state.get_G()
    F : np.matrix = np.matrix(np.zeros([len(state.get_xList()), 2]))
    for i in range(len(state.get_xList())):
        ri = np.array([state.get_xList()[i], state.get_yList()[i]])
        mi = np.array(state.get_mList()[i])
        for j in range(len(state.get_xList())):
            if(i != j):
                rj = np.array([state.get_xList()[j], state.get_yList()[j]])
                mj = state.get_mList()[j]
                rij_norm = np.linalg.norm(ri-rj)
                Fij = 1.0*G*mi*mj*(rj-ri)/rij_norm**3
                F[i, 0:2] += Fij
                
    return F

# calculates density given state
def calculate_density(state : SimulationState, numBins : int) -> np.matrix:
    dl : float = 1.0/numBins
    dA : float = 1.0/numBins**2
    M : np.matrix = np.matrix(np.zeros([numBins, numBins]))
    for i in range(len(state.get_xList())):
        M[int(state.get_xList()[i]/dl), int(state.get_yList()[i]/dl)] += state.get_mList()[i]
    return M/dA