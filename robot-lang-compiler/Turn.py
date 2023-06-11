from Node import Node

class Turn(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, symbolTable = None):
        print("Turning " + self.children[0].Evaluate(symbolTable)[1] + " degrees to the " + self.children[1])