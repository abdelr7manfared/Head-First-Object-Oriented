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
                  model: str,type: Type,backWood: Wood,topWood: Wood) -> None:
        guitarSpec = GuitarSpec(builder,model,type,backWood,topWood)
        guitar = Guitar(serialNumber,price,guitarSpec)
        self._guitars.append(guitar)
            
    def getGuitar(self,serialNumber: str) -> Guitar:
        for guitar in self._guitars:
            if guitar.serialNumber == serialNumber:
                return guitar
        return None
    
    def Search(self,searchGuitar: Guitar) -> List[Guitar]:
        matchingGuitars = []
        for guitar in self._guitars:
         
            if (guitar.model is not None and
                    guitar.model.lower() != searchGuitar.model.lower()
                        and guitar.model):
                continue
            if guitar.builder != searchGuitar.builder:
                continue
            if  guitar.type != searchGuitar.type:
                continue
            if  guitar.backWood != searchGuitar.backWood:
                continue
            if  guitar.topWood != searchGuitar.topWood:
                continue
            matchingGuitars.append(guitar)
        return matchingGuitars
            