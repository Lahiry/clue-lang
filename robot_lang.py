import sys
from robot_lang_lexer import Lexer
from robot_lang_parser import Parser

lexer = Lexer().get_lexer()
tokens = lexer.lex((" ").join(open(sys.argv[1], 'r')))

pg = Parser()
pg.parse()
parser = pg.get_parser()

try:
    result = parser.parse(tokens)
    print("Success!")
except Exception as e:
    print("Fail:")
    print("Exception:", e)