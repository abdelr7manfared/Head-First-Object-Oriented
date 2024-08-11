from Type import Type
from Wood import Wood
from Builder import Builder
class Guitar:
    def __init__(self,serialNumber: str,price: float,builder: Builder,
                 model: str,type: Type,backWood: Wood,topWood: Wood) -> None:
        self._serialNumber = serialNumber
        self._builder = builder
        self._model = model
        self._type = type
        self._backWood =  backWood
        self._topWood = topWood
        self._price = price
        
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
    def builder(self) -> Builder:
        return self._builder.value
    
    @property
    def model(self) -> str:
        return self._model

    @property
    def backWood(self) -> Wood:
        return self._backWood.value

    @property
    def topWood(self) -> Wood:
        return self._topWood.value
    @property
    def type(self) -> Type:
        return self._type.value


            