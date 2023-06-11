from Node import Node

class Drop(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symbolTable = None):
        symbolTable.Delete(self.value.value)
        print("Droping " + self.value.value)