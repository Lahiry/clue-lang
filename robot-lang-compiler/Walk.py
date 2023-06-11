from Node import Node

class Walk(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symbolTable = None):
        print("Walking " + self.value.Evaluate(symbolTable)[1] + " steps")