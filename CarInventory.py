#CarInventory.py

from Car import *
from CarInventoryNode import *

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root:
            myNode = CarInventoryNode(car)
            self._add(myNode,self.root)
        else:
            self.root = CarInventoryNode(car)
        
    def _add(self, myNode, currentRoot):
        if myNode == currentRoot:
            currentRoot.cars.append(myNode.cars[0])
        elif myNode < currentRoot:
            if currentRoot.getLeft():
                self._add(myNode,currentRoot.getLeft())
            else:
                currentRoot.setLeft(myNode)
                myNode.setParent(currentRoot)
        else:
            if currentRoot.getRight():
                self._add(myNode,currentRoot.getRight())
            else:
                currentRoot.setRight(myNode)
                myNode.setParent(currentRoot)

    def _doesCarExist(self, car, currentNode):
        newNode = CarInventoryNode(car)
        if not currentNode:
            return None
        elif newNode == currentNode:
            return currentNode
        elif newNode < currentNode:
            return self._doesCarExist(car, currentNode.getLeft())
        else:
            return self._doesCarExist(car, currentNode.getRight())

    def doesCarExist(self, car):
        if self.root:
            res = self._doesCarExist(car,self.root)
            if res:
                for i in res.cars:
                    if i == car:
                        return True
        return False

    def _get(self,car,currentNode):
        Car = CarInventoryNode(car)
        if not currentNode:
            return False
        elif currentNode == Car:
            return currentNode
        elif car < currentNode:
            return self._get(car,currentNode.getLeft())
        else:
            return self._get(car,currentNode.getRight())

    def _inOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += self._inOrder(currentNode.getLeft())
            ret += str(currentNode)
            ret += self._inOrder(currentNode.getRight())
        return ret

    def inOrder(self):
        return self._inOrder(self.root)

    def _preOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += str(currentNode)
            ret += self._preOrder(currentNode.getLeft())
            ret += self._preOrder(currentNode.getRight())
        return ret

    def preOrder(self):
        return self._preOrder(self.root)

    def _postOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += self._inOrder(currentNode.getLeft())
            ret += self._inOrder(currentNode.getRight())
            ret += str(currentNode)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)

    def getBestCar(self, make, model):
        car = Car(make, model)

        if self.root:
            res = self._doesCarExist(car,self.root)
            if res:
                if len(res.cars) == 1:
                    return res.cars[0]
                else:
                    max = res.cars[0]
                    for i in res.cars:
                        if i > max:
                            max = i
                    return max
        return None

    def getWorstCar(self, make, model):
        car = Car(make, model)

        if self.root:
            res = self._doesCarExist(car,self.root)
            if res:
                if len(res.cars) == 1:
                    return res.cars[0]
                else:
                    least = res.cars[0]
                    for i in res.cars:
                        if i < least:
                            least = i
                    return least
        return None

    def _getTotalInventoryPrice(self, currentNode):
        total = 0
        if currentNode:
            for i in currentNode.cars:
                total = total + i.price
            total += self._getTotalInventoryPrice(currentNode.getLeft())
            total += self._getTotalInventoryPrice(currentNode.getRight())
        return total

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)

    def getSuccessor(self, make, model):
        ObjectCar = Car(make, model, 0, 0)
        node = CarInventoryNode(ObjectCar)
        temp = self._get(node, self.root)
        #print(temp.getParent())
        succ = None
        if self.root:
            # case 1
            if temp is None: # if node doesn't exist
                # print("case1")
                return None
           
            elif temp.getRight(): #case 2
                #findMin function
                succ = temp.getRight()
                while succ.getLeft(): #right child's left child exists
                    if succ.getLeft() < succ:
                        succ = succ.left
                return succ
                
            else:  #case 3, no right child
                current = temp.getParent()
                while current:
                    if current > temp:
                        # print("case3, while loop")
                        return current
                    current = current.getParent()
                return current
        else:
            return None 

    """def findMin(self, currentNode):
        current = currentNode
        while current.getLeft():
            if current.getLeft() < current:
                current = current.left
        return current"""

    def spliceOut(self, node):
        if not (node.right and node.left):
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

        elif (node.left or node.right):
            if node.right:
                if node.parent.left == node:
                    node.parent.left = node.right
            else:
                node.parent.right = node.right
            node.right.parent = node.parent

    
    def removeCar(self, make, model, year, price):
        car = Car(make, model, year, price)
        if self.root:
            currentNode = self._get(car, self.root)
            if not currentNode: # does it exist
                return False
            for i in range(len(currentNode.cars)):
                if currentNode.cars[i] == car:
                    currentNode.cars.remove(i)
                    break
            
            if len(currentNode.cars) == 0: # If the list is empty after removing the Car, remove the CarInventoryNode from the BST entirely
                return True
            else:
# Case 1: Node to remove is leaf
                if currentNode.isLeaf():
                    if not currentNode.getParent():
                        self.root = None
                    elif currentNode == currentNode.parent.getLeft():
                        currentNode.parent.setLeft(None)
                    else:
                        currentNode.parent.setRight(None)

# Case 3: Node to remove has both children
                elif currentNode.getLeft() and currentNode.getRight():
                    # Need to find the successor, remove successor, and replace
                    # currentNode with successor's data
                    succ = currentNode.getSuccessor(make, model)
                    self.spliceOut(succ)
                    
                    currentNode.make = succ.make
                    currentNode.model = succ.model
                    currentNode.cars = succ.cars

# Case 2: Node to remove has one child
                else:
                    # Node has leftChild
                    if currentNode.left():
                        if currentNode.isLeftChild():
                            currentNode.left.setParent(currentNode.getParent())
                            currentNode.parent.setLeft(currentNode.getLeft())
                        elif currentNode.isRightChild():
                            currentNode.left.setParent(currentNode.getParent())
                            currentNode.parent.setRight(currentNode.getLeft())
                        else:
                            currentNode.make = currentNode.left.make
                            currentNode.model = currentNode.left.model
                            currentNode.cars = currentNode.left.cars
                            currentNode.setLeft(currentNode.left)
                            currentNode.setRight(currentNode.right)

                            if currentNode.getLeft():
                                currentNode.left.setParent(currentNode)
                            if currentNode.getRight():
                                currentNode.right.setParent(currentNode)
    
                    # Node has rightChild
                    else:
                        if currentNode.isLeftChild():
                            currentNode.right.setParent(currentNode.getParent())
                            currentNode.parent.setLeft(currentNode.getLeft())
                        elif currentNode.isRightChild():
                            currentNode.right.setParent(currentNode.getParent())
                            currentNode.parent.setLeft(currentNode.getLeft())
                        else:
                            currentNode.make = currentNode.left.make
                            currentNode.model = currentNode.left.model
                            currentNode.cars = currentNode.left.cars
                            currentNode.setLeft(currentNode.left)
                            currentNode.setRight(currentNode.right)

                            if currentNode.getLeft():
                                currentNode.left.setParent(currentNode)
                            if currentNode.getRight():
                                currentNode.right.setParent(currentNode)
        else:
            return False
                  
    

"""bst = CarInventory()

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

bst.removeCar("BMW", "X5", 2020, 58000)
bst.removeCar("Mazda", "CX-5", 0,0)
print(bst.inOrder())

"""

