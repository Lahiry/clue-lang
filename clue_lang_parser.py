from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(['NEWLINE', 'BEGIN_CLUE', 'END_CLUE', 'SUSPECT', 'WEAPON', 'LOCATION', 'CHOOSE_SUSPECT',
                                   'DEFINE_CRIME_SUSPECT', 'DEFINE_CRIME_WEAPON', 'DEFINE_CRIME_LOCATION', 'ACCUSATION_SUSPECT',
                                   'ACCUSATION_LOCATION', 'ACCUSATION_WEAPON', 'INVESTIGATION', 'SOLVED', 'IDENTIFIER'])

    def parse(self):
        @self.pg.production('clue : BEGIN_CLUE NEWLINE define_players define_crime investigation SUSPECT END_CLUE')
        def clue(p):
            return p

        @self.pg.production('define_players : IDENTIFIER CHOOSE_SUSPECT SUSPECT NEWLINE define_players')
        @self.pg.production('define_players : IDENTIFIER CHOOSE_SUSPECT SUSPECT NEWLINE')
        def define_players(p):
            return p

        @self.pg.production('define_crime : DEFINE_CRIME_SUSPECT SUSPECT NEWLINE DEFINE_CRIME_WEAPON WEAPON NEWLINE DEFINE_CRIME_LOCATION LOCATION NEWLINE')
        def define_crime(p):
            return p

        @self.pg.production('investigation : INVESTIGATION NEWLINE accusation SOLVED NEWLINE')
        def investigation(p):
            return p
            
        @self.pg.production('accusation : IDENTIFIER ACCUSATION_SUSPECT SUSPECT ACCUSATION_LOCATION LOCATION ACCUSATION_WEAPON WEAPON NEWLINE accusation')
        @self.pg.production('accusation : IDENTIFIER ACCUSATION_SUSPECT SUSPECT ACCUSATION_LOCATION LOCATION ACCUSATION_WEAPON WEAPON NEWLINE')
        def accusation(p):
            return p
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
