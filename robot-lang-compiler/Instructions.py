from Node import Node

class Instructions(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, symbolTable = None):

        for child in self.children:
            child.Evaluate(symbolTable)
        
        