from Node import Node

class VarDec(Node):
    def __init__(self, value,):
        self.value = value

    def Evaluate(self, symbolTable = None):
            symbolTable.Create(self.value, "Int", 0)
