from Guitar import Guitar
from Type import Type
from Wood import Wood
from Builder import Builder
from typing import List,Union
from GuitarSpec import GuitarSpec

class Inventory:
    def __init__(self) -> None:
        self._guitars = []
    
    def addGuitar(self,serialNumber: str,price: float,builder: Builder,
                  model: str,type: Type,backWood: Wood,topWood: Wood,numString: int)->None:
        guitarSpec = GuitarSpec(builder,model,type,backWood,topWood,numString)
        guitar = Guitar(serialNumber,price,guitarSpec)
        self._guitars.append(guitar)
            
    def getGuitar(self,serialNumber: str) -> Guitar:
        for guitar in self._guitars:
            if guitar.serialNumber == serialNumber:
                return guitar
        return None
    
    def Search(self,searchSpec:GuitarSpec) -> List[Guitar]:
        matchingGuitars = []
        for guitar in self._guitars:
            if guitar.guitarSpec.match(searchSpec):        
                matchingGuitars.append(guitar)
        return matchingGuitars
            