from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('NEWLINE', r'\n')
        self.lexer.add('WALK', r'walk')
        self.lexer.add('STEPS', r'steps')
        self.lexer.add('TURN', r'turn')
        self.lexer.add('DEGREES', r'degrees to the')
        self.lexer.add('ORIENTATION', r'left|right')
        self.lexer.add('PICK', r'pick')
        self.lexer.add('DROP', r'drop')
        self.lexer.add('REPEAT', r'repeat')
        self.lexer.add('TIMES', r'times')
        self.lexer.add('TWO_DOTS', r':')
        self.lexer.add('COMMA', r',')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('HOLDING', r'holding')
        self.lexer.add('NOT', r'!')
        self.lexer.add('ACTION', r'action')
        self.lexer.add('DO', r'do')
        self.lexer.add('STOP', r'stop')
        self.lexer.add('OPENING_BRACKET', r'\(')
        self.lexer.add('CLOSING_BRACKET', r'\)')
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.ignore(r'[ \t]+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
