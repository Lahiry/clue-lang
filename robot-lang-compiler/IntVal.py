from Node import Node

class IntVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symbolTable = None):
        return ("Int", self.value)