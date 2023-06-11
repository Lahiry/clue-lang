from Node import Node

class Identifier(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symbolTable = None):
        return symbolTable.Get(self.value)