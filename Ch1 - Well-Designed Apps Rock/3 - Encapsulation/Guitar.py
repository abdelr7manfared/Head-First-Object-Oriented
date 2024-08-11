from Type import Type
from Wood import Wood
from Builder import Builder
from GuitarSpec import GuitarSpec
class Guitar:
    def __init__(self,serialNumber: str,price: float,builder: Builder,
                 model: str,type: Type,backWood: Wood,topWood: Wood) -> None:
        self._serialNumber = serialNumber
        self._price = price
        self._guitarSpec = GuitarSpec(builder,model,type,backWood,topWood)
        
        
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self,price: float):
        self._price = price
        
    @property
    def serialNumber(self) -> str:
        return self._serialNumber

    @property
    def guitarSpec(self) -> GuitarSpec:
        return self._guitarSpec


            