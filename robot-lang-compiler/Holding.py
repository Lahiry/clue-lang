from Node import Node

class Holding(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, symbolTable = None):
        if self.children[0] == "!":
            return not symbolTable.Check(self.children[1])
        else:
            return symbolTable.Check(self.children[1])