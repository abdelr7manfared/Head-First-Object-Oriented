from Guitar import Guitar
from GuitarSpec import GuitarSpec
from Inventory import Inventory
from Type import Type
from Wood import Wood
from Builder import Builder
def FindGuitarTester() -> None:    
    inventory = Inventory()
    initializeInventory(inventory)
    whatErinLikes = GuitarSpec(Builder.FENDER,'Stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER) 
    guitars = inventory.Search(whatErinLikes)
    if guitar:
        print("Erin, you might like these guitars:")
        for guitar in guitars:
            spec = guitar.guitarSpec
            print('We have a',
              spec.builder , ' ', spec.model, ' ',
              spec.type,' spec:\n',
              spec.backWood,' ',' back and sides,\n',
              spec.topWood,' ','top.\nYou can have it for only $',
              guitar.price,'!'
              )
    else:
        print('Sorry, Erin, we have nothing for you.')
def initializeInventory(inventory: Inventory) -> None:
    inventory.addGuitar("11277", 3999.95, Builder.COLLINGS, "CJ", Type.ACOUSTIC,Wood.INDIAN_ROSEWOOD,  Wood.ADIRONDACK)
    inventory.addGuitar("V95693", 1499.95, Builder.FENDER, "Stratocastor", Type.ELECTRIC,Wood.ALDER,  Wood.ALDER)
    inventory.addGuitar("V9512", 1549.95, Builder.FENDER, "Stratocastor", Type.ELECTRIC,Wood.ALDER,  Wood.ALDER)
    inventory.addGuitar("122784", 5495.95, Builder.MARTIN, "D-18", Type.ACOUSTIC,Wood.MAHOGANY,  Wood.ADIRONDACK)
    inventory.addGuitar("76531", 6295.95, Builder.MARTIN, "OM-28", Type.ACOUSTIC,Wood.BRAZILIAN_ROSEWOOD,  Wood.ADIRONDACK)
    inventory.addGuitar("70108276", 2295.95, Builder.GIBSON, "Les Paul", Type.ELECTRIC,Wood.MAHOGANY, Wood.MAPLE)
    inventory.addGuitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue",Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY)
    inventory.addGuitar("77023", 6275.95, Builder.MARTIN, "D-28", Type.ACOUSTIC,Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK)
    inventory.addGuitar("1092", 12995.95, Builder.OLSON, "SJ", Type.ACOUSTIC,Wood.INDIAN_ROSEWOOD, Wood.CEDAR)
    inventory.addGuitar("566-62", 8999.95, Builder.RYAN, "Cathedral", Type.ACOUSTIC,Wood.COCOBOLO, Wood.CEDAR)
    inventory.addGuitar("629584", 2100.95, Builder.PRS, "Dave Navarro Signature",Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE)


if __name__ == '__main__':
    FindGuitarTester()