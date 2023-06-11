from ActionTable import ActionTable
from Node import Node
from SymbolTable import SymbolTable

class ActionCall(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbolTable = None):
        action_name = self.value.value
        action = ActionTable.Get(action_name)
        new_symbolTable = SymbolTable()
        for varDec in action.children[1]:
            varDec.Evaluate(new_symbolTable)
        for i, argument in enumerate(self.children):
            variables = list(new_symbolTable.variables.keys())
            new_symbolTable.Set(variables[i], argument.Evaluate(symbolTable))
        return action.children[2].Evaluate(new_symbolTable)