from Guitar import Guitar
from typing import List
class Inventory:
    def __init__(self) -> None:
        self._guitars = []
    
    def addGuitar(self,serialNumber: str,price: float,builder: str,
                  model: str,type: str,backWood: str,topWood: str) -> None:
        guitar = Guitar(serialNumber,price,builder,model,type,backWood,topWood)
        self._guitars.append(guitar)
            
    def getGuitar(self,serialNumber: str) -> Guitar:
        for guitar in self._guitars:
            if guitar.serialNumber == serialNumber:
                return guitar
        return None
    
    def Search(self,searchGuitar: Guitar) -> List[Guitar]:
        for guitar in self._guitars:
            if (guitar.builder is not None and 
                    guitar.builder != searchGuitar.builder and 
                        guitar.builder):
                continue
            if (guitar.model is not None and 
                    guitar.model != searchGuitar.model and
                        guitar.model):
                continue
            if (guitar.type is not None and
                    guitar.type != searchGuitar.type and
                        guitar.type):
                continue
            if (guitar.backWood is not None and
                    guitar.backWood != searchGuitar.backWood and
                        guitar.backWood):
                continue
            if (guitar.topWood is not None and
                    guitar.topWood != searchGuitar.topWood and
                        guitar.topWood):
                continue
            return guitar
        return None
            