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

class Response:
    def __init__(self, binMatrix : list[np.matrix]):
        # there is a bin list for every step in time
        self.__binMatrix__ = binMatrix