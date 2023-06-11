from Node import Node

class Pick(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symbolTable = None):
        symbolTable.Create(self.value.value, "Item", "Holding")
        print("Picking " + self.value.value)