from ActionTable import ActionTable
from Node import Node

class ActionDec(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, symbolTable = None):
        ActionTable.Create(self.children[0].value, self)