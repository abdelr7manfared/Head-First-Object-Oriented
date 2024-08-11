from Type import Type
from Wood import Wood
from Builder import Builder
class GuitarSpec:
    def __init__(self,builder: Builder,model: str,type: Type,
                 backWood: Wood,topWood: Wood) -> None:
        self._builder = builder
        self._model = model
        self._type = type
        self._backWood =  backWood
        self._topWood = topWood

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
