class Guitar:
    def __init__(self,serialNumber: str,price: float,builder: str,
                 model: str,type: str,backWood: str,topWood: str) -> None:
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
    def builder(self) -> str:
        return self._builder
    
    @property
    def model(self) -> str:
        return self._model

    @property
    def backWood(self) -> str:
        return self._backWood

    @property
    def topWood(self) -> str:
        return self._topWood
    @property
    def type(self) -> str:
        return self._type


            