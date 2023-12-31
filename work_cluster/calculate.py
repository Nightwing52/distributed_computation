from models import Request, Response, SimulationState
import numpy as np

NUM_BINS = 50

def simulate(request : Request) -> Response:
    states : list[SimulationState] = [request.create_state()] # carries current state and state before that
    output : Response = Response([calculate_density(states[0], NUM_BINS)])
    
    states.append(first_step(states[0]))
    output.add(calculate_density(states[1], NUM_BINS))

    for i in range(2, request.get_T()):
        F : np.matrix = calculate_force(states[-1])
        new_x = 2.0*states[-1].get_xList()-states[-2].get_xList()+F[:,0]/states[-1].get_mList()*states[-1].get_delta()**2
        new_y = 2.0*states[-1].get_yList()-states[-2].get_yList()+F[:,1]/states[-1].get_mList()*states[-1].get_delta()**2

        # TODO: update state and append new density to output
        new_state : SimulationState = SimulationState(new_x, new_y, [0], [0], states[-1].get_mList(), states[-1].get_G(),
                                                      states[-1].get_T(), states[-1].get_delta())
        states[-2] = states[-1]
        states[-1] = new_state
        output.add(calculate_density(states[-1], NUM_BINS))

    return output

# performs first step of Verlet integration
def first_step(initialState : SimulationState) -> SimulationState:
    F = calculate_force(initialState)
    new_x = initialState.get_xList()+initialState.get_vxList()*initialState.get_delta()+0.5*F[0:,0]*initialState.get_delta()**2
    new_y = initialState.get_yList()+initialState.get_yList()*initialState.get_delta()+0.5*F[0:,1]*initialState.get_delta()**2
    return SimulationState(new_x, new_y, initialState.get_vxList(), initialState.get_vyList(), initialState.get_mList(),
                           initialState.get_G(), initialState.get_T(), initialState.get_delta())

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