from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(['NEWLINE', 'WALK', 'STEPS', 'TURN', 'DEGREES', 'ORIENTATION', 'PICK', 'DROP', 'REPEAT', 'TIMES', 'TWO_DOTS', 
                                   'COMMA', 'IF', 'ELSE', 'HOLDING', 'NOT', 'ACTION', 'DO', 'STOP', 'OPENING_BRACKET', 'CLOSING_BRACKET', 'IDENTIFIER',
                                   'NUMBER'])

    def parse(self):
        @self.pg.production('instructions : tasks')
        def instructions(p):
            pass

        @self.pg.production('tasks : task')
        @self.pg.production('tasks : task tasks')
        def tasks(p):
            pass

        @self.pg.production('task : walk')
        @self.pg.production('task : turn')
        @self.pg.production('task : pick')
        @self.pg.production('task : drop')
        @self.pg.production('task : repeat')
        @self.pg.production('task : if_op')
        @self.pg.production('task : action')
        @self.pg.production('task : do')
        @self.pg.production('task : NEWLINE')
        def task(p):
            pass

        @self.pg.production('walk : WALK NUMBER STEPS NEWLINE')
        @self.pg.production('walk : WALK IDENTIFIER STEPS NEWLINE')
        def walk(p):
            pass

        @self.pg.production('turn : TURN NUMBER DEGREES ORIENTATION NEWLINE')
        @self.pg.production('turn : TURN IDENTIFIER DEGREES ORIENTATION NEWLINE')
        def turn(p):
            pass

        @self.pg.production('pick : PICK IDENTIFIER NEWLINE')
        def pick(p):
            pass

        @self.pg.production('drop : DROP IDENTIFIER NEWLINE')
        def drop(p):
            pass

        @self.pg.production('repeat : REPEAT NUMBER TIMES TWO_DOTS NEWLINE instructions STOP NEWLINE')
        @self.pg.production('repeat : REPEAT IDENTIFIER TIMES TWO_DOTS NEWLINE instructions STOP NEWLINE')
        def repeat(p):
            pass

        @self.pg.production('if_op : IF conditional TWO_DOTS NEWLINE instructions STOP NEWLINE')
        @self.pg.production('if_op : IF conditional TWO_DOTS NEWLINE instructions ELSE TWO_DOTS NEWLINE instructions STOP NEWLINE')
        def if_op(p):
            pass

        @self.pg.production('action : ACTION IDENTIFIER OPENING_BRACKET parameters CLOSING_BRACKET TWO_DOTS NEWLINE instructions STOP NEWLINE')
        def action(p):
            pass

        @self.pg.production('do : DO IDENTIFIER OPENING_BRACKET numbers CLOSING_BRACKET NEWLINE')
        def do(p):
            pass

        @self.pg.production('conditional : HOLDING IDENTIFIER')
        @self.pg.production('conditional : NOT HOLDING IDENTIFIER')
        def conditional(p):
            pass

        @self.pg.production('parameters : ')
        @self.pg.production('parameters : IDENTIFIER')
        @self.pg.production('parameters : IDENTIFIER COMMA parameters')
        def parameters(p):
            pass

        @self.pg.production('numbers : ')
        @self.pg.production('numbers : NUMBER')
        @self.pg.production('numbers : NUMBER COMMA numbers')
        def numbers(p):
            pass
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
