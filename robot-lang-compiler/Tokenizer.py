import re
from Token import Token

class Tokenizer:
    def __init__(self, source: str):
        self.source = source
        self.position: int = None
        self.next: Token = Token(None, None)
        
    def selectNext(self):       
        pattern = r'\b\w+\b|\|\||:|[^\s\w()+\-*/"]|(?<=\d)[-+*/](?=\d)|\n|"[^"\n]*"|\'[^\n\']*\'|[^\w\s]'

        arguments = re.findall(pattern, self.source)
        arguments.append("EOF")

        allowed_variables = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')
        reserved_words = ['walk', 'steps', 'turn', 'degrees', 'to', 'the', 'left', 'right', 'pick', 'drop', 'repeat', 'times', 'if', 'else', 'holding', 'action',
                          'do', 'stop', ':', ',', '!', '(', ')', 'EOF']
                
        if arguments[self.position].isdigit():
            self.next.type = "INT"
        elif arguments[self.position] == "walk":
            self.next.type = "WALK"
        elif arguments[self.position] == "steps":
            self.next.type = "STEPS"
        elif arguments[self.position] == "turn":
            self.next.type = "TURN"
        elif arguments[self.position] == "degrees":
            self.next.type = "DEGREES"
        elif arguments[self.position] == "to":
            self.next.type = "TO"
        elif arguments[self.position] == "the":
            self.next.type = "THE"
        elif arguments[self.position] == "left" or arguments[self.position] == "right":
            self.next.type = "ORIENTATION"
        elif arguments[self.position] == "pick":
            self.next.type = "PICK"
        elif arguments[self.position] == "drop":
            self.next.type = "DROP"
        elif arguments[self.position] == "repeat":
            self.next.type = "REPEAT"
        elif arguments[self.position] == "times":
            self.next.type = "TIMES"
        elif arguments[self.position] == "if":
            self.next.type = "IF"
        elif arguments[self.position] == "else":
            self.next.type = "ELSE"
        elif arguments[self.position] == "holding":
            self.next.type = "HOLDING"
        elif arguments[self.position] == "action":
            self.next.type = "ACTION"
        elif arguments[self.position] == "do":
            self.next.type = "DO"
        elif arguments[self.position] == "stop":
            self.next.type = "STOP"
        elif arguments[self.position] == ":":
            self.next.type = "TWO_DOTS"
        elif arguments[self.position] == "!":
            self.next.type = "NOT"
        elif arguments[self.position] == ",":
            self.next.type = "COMMA"
        elif arguments[self.position] == "(":
            self.next.type = "OPENING_BRACKET"
        elif arguments[self.position] == ")":
            self.next.type = "CLOSING_BRACKET"
        elif allowed_variables.match(arguments[self.position]) and arguments[self.position] not in reserved_words:
            self.next.type = "IDENTIFIER"
        elif arguments[self.position] == "\n":
            self.next.type = "ENDLINE"
        elif arguments[self.position] == "EOF":
            self.next.type = "EOF"
        
        self.next.value = arguments[self.position]
        self.next = Token(self.next.type, self.next.value)
        self.position += 1