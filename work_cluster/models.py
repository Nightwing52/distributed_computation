import numpy as np

class Request:
    def __init__(self, xList : list[float], yList : list[float], 
                 vxList : list[float], vyList : list[float], mList : list[float], 
                 G : float, T : int):
        self.__xList__ = xList
        self.__yList__ = yList
        self.__vxList__ = vxList
        self.__vyList__ = vyList
        self.__mList__ = mList
        self.__G__ = G
        self.__T__ = T
    
    def validate(self) -> bool:
        # within unit square
        for x in self.__xList__:
            if(x < 0.0 or x > 1.0):
                return False
        for y in self.__yList__:
            if(y < 0.0 or y > 1.0):
                return False
        
        if(self.__G__ <= 0.0 or self.__T__ <= 0):
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

class SimulationState(Request):
    def __init__(self, request : Request):
        Request.__init__(self, request.get_xList(), request.get_yList(), request.get_vxList(), request.get_vyList(),
              request.get_mList(), request.get_G(), request.get_T())

class Response:
    def __init__(self, binMatrix : list[np.matrix]):
        # there is a bin list for every step in time
        self.__binMatrix__ = binMatrix