#testFile.py
from Car import *
from CarInventory import *
from CarInventoryNode import *

def test_Car():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    car3 = Car("ur mom", "meow", 2000, 1)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    carNode.cars.append(car3)
    assert str(car1) == "Make: DODGE, Model: DART, Year: 2015, Price: $6000"
    assert str(car2) == "Make: DODGE, Model: DART, Year: 2003, Price: $5000"
    assert str(car3) == "Make: UR MOM, Model: MEOW, Year: 2000, Price: $1"
    assert str(carNode) == \
"Make: DODGE, Model: DART, Year: 2015, Price: $6000\n\
Make: DODGE, Model: DART, Year: 2003, Price: $5000\n\
Make: UR MOM, Model: MEOW, Year: 2000, Price: $1\n"

def test_addCar():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.inOrder() == \
"Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
    assert bst.preOrder() == \
"Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
    assert bst.postOrder() == \
"Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n"

def test_getCar():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Tesla", "Model3", 2010, 50000)
    car7 = Car("Mercedes", "Sprinter", 2013, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4

    car6 = Car("Tesla", "Model3", 2010, 50000)
    car7 = Car("Mercedes", "Sprinter", 2013, 25000)
    bst.addCar(car6)
    bst.addCar(car7)

    assert bst.getWorstCar("Tesla", "Model3") == car6
    assert bst.getWorstCar("Mercedes", "Sprinter") == car7

def test_getTotalInventoryPrice():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getTotalInventoryPrice() == 158000
    car6 = Car("Tesla", "Model3", 2010, 50000)
    car7 = Car("Mercedes", "Sprinter", 2013, 25000)
    bst.addCar(car6)
    bst.addCar(car7)
    assert bst.getTotalInventoryPrice() == 233000

def test_getSuccessor():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.inOrder() == \
"Make: AUDI, Model: A3, Year: 2021, Price: $25000\
Make: BMW, Model: X5, Year: 2022, Price: $60000\
Make: BMW, Model: X5, Year: 2020, Price: $58000\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000"
    
    assert bst.getSuccessor("BMW", "X5") == \
"""Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000"""
    
    assert bst.getSuccessor("Audi", "A3") == \
"Make: BMW, Model: X5, Year: 2020, Price: $58000"

    assert bst.getSuccessor("Mazda", "CX-5") == \
"Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000"

def test_removeCar():
    pass
