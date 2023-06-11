import sys
from Parser import Parser
from PrePro import PrePro
from SymbolTable import SymbolTable

def robot_lang():
    arguments = PrePro.filter_comments((" ").join(open(sys.argv[1], 'r')))
    parser = Parser()
    symbolTable = SymbolTable()
    parser.run(arguments).Evaluate(symbolTable)

robot_lang()