from Node import Node

class Repeat(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, symbolTable = None):
        for i in range(0, int(self.children[0].Evaluate(symbolTable)[1])):
            self.children[1].Evaluate(symbolTable)
        
        
