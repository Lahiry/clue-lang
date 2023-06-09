from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('NEWLINE', '\n')
        self.lexer.add('ASSIGNMENT', '=')
        self.lexer.add('WALK', 'walk')
        self.lexer.add('STEPS', 'steps')
        self.lexer.add('TURN', 'turn')
        self.lexer.add('DEGREES', 'degrees to the')
        self.lexer.add('ORIENTATION', r'left|right')
        self.lexer.add('PICK', 'pick')
        self.lexer.add('DROP', 'drop')
        self.lexer.add('REPEAT', 'repeat')
        self.lexer.add('TIMES', 'times')
        self.lexer.add('TWO_DOTS', ':')
        self.lexer.add('COMMA', ',')
        self.lexer.add('IF', 'if')
        self.lexer.add('ELSE', 'else')
        self.lexer.add('HOLDING', 'holding')
        self.lexer.add('NOT', '!')
        self.lexer.add('ACTION', 'action')
        self.lexer.add('DO', 'do')
        self.lexer.add('STOP', 'stop')
        self.lexer.add('OPENING_BRACKET', r'\(')
        self.lexer.add('CLOSING_BRACKET', r'\)')
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.ignore(r'[ \t]+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
