#CarInventoryNode.py
from Car import *

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.parent = None
        self.left = None
        self.right = None
        self.cars = [car]

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent
    
    def getLeft(self):
        return self.left
    
    def setLeft(self,left):
        self.left = left
    
    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def isLeaf(self):
        return not (self.right or self.left)

    def isLeftChild(self):
        return self.parent and (self.parent.left is self)

    def isRightChild(self):
        return self.parent and (self.parent.right is self)

    def __str__(self):
        details = ""
        for car in self.cars:
            details += str(car) + "\n"
        return details

    def __gt__(self, rhs):
        if rhs == None:
            return False
        if self.make == rhs.make:
            return self.model > rhs.model
        else:
            return self.make > rhs.make
    
    def __lt__(self, rhs):
        if rhs == None:
            return False
        if self.make == rhs.make:
            return self.model < rhs.model
        else:
            return self.make < rhs.make

    def __eq__(self, rhs):
        if rhs == None:
            return False
        if self.make == rhs.make:
            if self.model == rhs.model:
                return True
            else:
                return False
        else:
            return False


