from Type import Type
from Wood import Wood
from Builder import Builder
from typing import Any

class GuitarSpec:
    def __init__(self,builder: Builder,model: str,type: Type,
                 backWood: Wood,topWood: Wood,numString: int) -> None:
        self._builder = builder
        self._model = model
        self._type = type
        self._numString = numString
        self._backWood =  backWood
        self._topWood = topWood

    @property
    def builder(self) -> Builder:
        return self._builder
    
    @property
    def model(self) -> str:
        return self._model

    @property
    def numString(self) -> int:
        return self._numString
    @property
    def backWood(self) -> Wood:
        return self._backWood

    @property
    def topWood(self) -> Wood:
        return self._topWood
    @property
    def type(self) -> Type:
        return self._type

    def match(self,searchSpec: 'GuitarSpec') -> bool: # use Any or 'GuitarSpec'
        if (self.model is not None and 
                self.model.lower() != searchSpec.model.lower() and 
                    self._model):
            return False
        if self.builder != searchSpec.builder:
            return False
        if self.numString != searchSpec.numString:
            return False
        if  self.type != searchSpec.type:
            return False
        if  self.backWood != searchSpec.backWood:
            return False
        if  self.topWood != searchSpec.topWood:
            return False
        return True