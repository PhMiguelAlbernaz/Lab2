from typing import Union
from math import sqrt

class Raiz:

    def __init__(self):
        self.x = 0
        self.res = 0

    def executar(self, x:float)->Union[float,str]:

        try:
            self.x = x
            self.res = sqrt(self.x)
        except ValueError:
            return "error:negative number"
        return self.res



