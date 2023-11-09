import numpy as np

class Request:
    def __init__(self, xList, yList, 
                 vxList, vyList, mList, 
                 G : float, T : int, delta : float):
        self.__xList__ = xList
        self.__yList__ = yList
        self.__vxList__ = vxList
        self.__vyList__ = vyList
        self.__mList__ = mList
        self.__G__ = G
        self.__T__ = T
        self.__delta__ = delta
    
    def validate(self) -> bool:
        # within unit square
        for x in self.__xList__:
            if(x < 0.0 or x > 1.0):
                return False
        for y in self.__yList__:
            if(y < 0.0 or y > 1.0):
                return False
        
        if(self.__G__ <= 0.0 or self.__T__ <= 0 or self.__delta__ <= 0.0):
            return False
        
        return True
    
    def get_xList(self):
        return self.__xList__
    
    def get_yList(self):
        return self.__yList__
    
    def get_vxList(self):
        return self.__vxList__
    
    def get_vyList(self):
        return self.__vyList__
    
    def get_mList(self):
        return self.__mList__
    
    def get_G(self):
        return self.__G__
    
    def get_T(self):
        return self.__T__
    
    def get_delta(self):
        return self.__delta__

    def create_state(self): # creates state from request object
        return SimulationState(np.array(self.get_xList()), np.array(self.get_yList()), np.array(self.get_vxList()),
                np.array(self.get_vyList()), np.array(self.get_mList()), self.get_G(), self.get_T(), self.get_delta())

class SimulationState(Request):
    def __init__(self, xList, yList, 
                 vxList, vyList, mList, 
                 G : float, T : int, delta : float):
        Request.__init__(self, xList, yList, vxList, vyList, mList, G, T, delta)

class Response:
    def __init__(self, binMatrix : list[np.matrix]):
        # there is a bin list for every step in time
        self.__binMatrix__ = binMatrix