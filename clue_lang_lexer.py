from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('NEWLINE', r'\n')
        self.lexer.add('BEGIN_CLUE', r'There has been a murder at Tudor Mansion')
        self.lexer.add('END_CLUE', r'is arrested for murder')
        self.lexer.add('SUSPECT', r'Miss Scarlett|Colonel Mustard|Doctor Orchid|Reverend Green|Mrs. Peacock|Professor Plum')
        self.lexer.add('WEAPON', r'Candlestick|Dagger|Lead Pipe|Revolver|Rope|Wrench')
        self.lexer.add('LOCATION', r'Ballroom|Billiard Room|Conservatory|Dining Room|Hall|Kitchen|Library|Lounge|Study')
        self.lexer.add('CHOOSE_SUSPECT', 'is')
        self.lexer.add('DEFINE_CRIME_SUSPECT', r'The murder was done by')
        self.lexer.add('DEFINE_CRIME_WEAPON', r'The crime weapon is a')
        self.lexer.add('DEFINE_CRIME_LOCATION', r'The crime location is the')
        self.lexer.add('ACCUSATION_SUSPECT', 'accuses')
        self.lexer.add('ACCUSATION_LOCATION', 'in the')
        self.lexer.add('ACCUSATION_WEAPON', 'with a')
        self.lexer.add('INVESTIGATION', r'While the crime is not solved')
        self.lexer.add('SOLVED', r'The crime has been solved')
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer.ignore(r'[ \t]+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
