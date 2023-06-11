from Node import Node

class IfOp(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, symbolTable = None):
        if self.children[0].Evaluate(symbolTable) == True:
            self.children[1].Evaluate(symbolTable)
        elif len(self.children) == 3:
            self.children[2].Evaluate(symbolTable)