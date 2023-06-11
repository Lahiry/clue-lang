from Walk import Walk
from Turn import Turn
from Pick import Pick
from Drop import Drop
from Repeat import Repeat
from Holding import Holding
from VarDec import VarDec
from Instructions import Instructions
from ActionCall import ActionCall
from ActionDec import ActionDec
from Identifier import Identifier
from IfOp import IfOp
from NoOp import NoOp
from IntVal import IntVal
from Tokenizer import Tokenizer

class Parser:
    
    @staticmethod
    def parseInstructions():
        tasks = []
        while Parser.tokenizer.next.type != "EOF":
            tasks.append(Parser.parseTask())
        result = Instructions(tasks)
        return result

    @staticmethod
    def parseTask(inside_action = False):
        result = None
        
        if Parser.tokenizer.next.type == "WALK":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "INT":
                steps = IntVal(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "STEPS":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "ENDLINE":
                        result = Walk(steps)
                        Parser.tokenizer.selectNext()
                    else:
                        raise Exception("Expected endline")
                else:
                    raise Exception("Expected 'steps'")
            elif Parser.tokenizer.next.type == "IDENTIFIER":
                steps = Identifier(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "STEPS":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "ENDLINE":
                        result = Walk(steps)
                        Parser.tokenizer.selectNext()
                    else:
                        raise Exception("Expected endline")
                else:
                    raise Exception("Expected 'steps'")
            else:
                raise Exception("Expected an integer or an identifier")
            
        elif Parser.tokenizer.next.type == "TURN":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "INT":
                degrees = IntVal(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "DEGREES":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "TO":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "THE":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "ORIENTATION":
                                orientation = Parser.tokenizer.next.value
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "ENDLINE":
                                    result = Turn([degrees, orientation])
                                    Parser.tokenizer.selectNext()
                                else:
                                    raise Exception("Expected endline")
                            else:
                                raise Exception("Expected 'left' or 'right'")
                        else:
                            raise Exception("Expected 'the'")
                    else:
                        raise Exception("Expected 'to'")
                else:
                    raise Exception("Expected 'degrees to the'")
            elif Parser.tokenizer.next.type == "IDENTIFIER":
                degrees = Identifier(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "DEGREES":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "TO":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "THE":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next == "ORIENTATION":
                                orientation = Parser.tokenizer.next.value
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "ENDLINE":
                                    result = Turn([degrees, orientation])
                                    Parser.tokenizer.selectNext()
                                else:
                                    raise Exception("Expected endline")
                            else:
                                raise Exception("Expected 'left' or 'right'")
                        else:
                            raise Exception("Expected 'the'")
                    else:
                        raise Exception("Expected 'to'")
                else:
                    raise Exception("Expected 'degrees to the'")
                
        elif Parser.tokenizer.next.type == "PICK":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                item = Identifier(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "ENDLINE":
                    result = Pick(item)
                    Parser.tokenizer.selectNext()
                else:
                    raise Exception("Expected endline")
            else:
                raise Exception("Expected an identifier")
            
        elif Parser.tokenizer.next.type == "DROP":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                item = Identifier(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "ENDLINE":
                    result = Drop(item)
                    Parser.tokenizer.selectNext()
                else:
                    raise Exception("Expected endline")
            else:
                raise Exception("Expected an identifier")
            
        elif Parser.tokenizer.next.type == "REPEAT":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "INT":
                times = IntVal(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "TIMES":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "TWO_DOTS":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "ENDLINE":
                            Parser.tokenizer.selectNext()
                            tasks = []
                            while Parser.tokenizer.next.type != "STOP":
                                tasks.append(Parser.parseTask())
                            result = Repeat([times, Instructions(tasks)])
                            if Parser.tokenizer.next.type == "STOP":
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "ENDLINE":
                                    Parser.tokenizer.selectNext()
                                else:
                                    raise Exception("Expected endline")
                            else:
                                raise Exception("Expected stop")
                        else:
                            raise Exception("Expected endline")
                    else:
                        raise Exception("Expected ':'")
                else:
                    raise Exception("Expected 'times'")
                
            elif Parser.tokenizer.next.type == "IDENTIFIER":
                times = Identifier(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "TIMES":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "TWO_DOTS":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "ENDLINE":
                            Parser.tokenizer.selectNext()
                            tasks = []
                            while Parser.tokenizer.next.type != "STOP":
                                tasks.append(Parser.parseTask())
                            result = Repeat([times, Instructions(tasks)])
                            if Parser.tokenizer.next.type == "STOP":
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "ENDLINE":
                                    Parser.tokenizer.selectNext()
                                else:
                                    raise Exception("Expected endline")
                            else:
                                raise Exception("Expected stop")
                        else:
                            raise Exception("Expected endline")
                    else:
                        raise Exception("Expected ':'")
                else:
                    raise Exception("Expected 'times'")
                
        elif Parser.tokenizer.next.type == "IF":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "HOLDING":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "IDENTIFIER":
                    condition = Holding([None, Parser.tokenizer.next.value])
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "TWO_DOTS":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "ENDLINE":
                            Parser.tokenizer.selectNext()
                            tasks_if = []
                            while Parser.tokenizer.next.type != "STOP" and Parser.tokenizer.next.type != "ELSE":
                                tasks_if.append(Parser.parseTask())
                            result = IfOp([condition, Instructions(tasks_if)])
                            if Parser.tokenizer.next.type == "ELSE":
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "TWO_DOTS":
                                    Parser.tokenizer.selectNext()
                                    if Parser.tokenizer.next.type == "ENDLINE":
                                        Parser.tokenizer.selectNext()
                                        tasks_else = []
                                        while Parser.tokenizer.next.type != "STOP":
                                            tasks_else.append(Parser.parseTask())
                                        result = IfOp([condition, Instructions(tasks_if), Instructions(tasks_else)])
                                        if Parser.tokenizer.next.type == "STOP":
                                            Parser.tokenizer.selectNext()
                                            if Parser.tokenizer.next.type == "ENDLINE":
                                                Parser.tokenizer.selectNext()
                                            else:
                                                raise Exception("Expected endline")
                                        else:
                                            raise Exception("Expected stop")
                                    else:
                                        raise Exception("Expected endline")
                                else:
                                    raise Exception("Expected ':'")
                            else:
                                raise Exception("Expected else")
                        else:
                            raise Exception("Expected endline")
                    else:
                        raise Exception("Expected ':'")
                    
            elif Parser.tokenizer.next.type == "NOT":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "HOLDING":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "IDENTIFIER":
                        condition = Holding(["!", Parser.tokenizer.next.value])
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "TWO_DOTS":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "ENDLINE":
                                Parser.tokenizer.selectNext()
                                tasks_if = []
                                while Parser.tokenizer.next.type != "STOP" and Parser.tokenizer.next.type != "ELSE":
                                    tasks_if.append(Parser.parseTask())
                                result = IfOp([condition, Instructions(tasks_if)])
                                if Parser.tokenizer.next.type == "ELSE":
                                    Parser.tokenizer.selectNext()
                                    if Parser.tokenizer.next.type == "TWO_DOTS":
                                        Parser.tokenizer.selectNext()
                                        if Parser.tokenizer.next.type == "ENDLINE":
                                            Parser.tokenizer.selectNext()
                                            tasks_else = []
                                            while Parser.tokenizer.next.type != "STOP":
                                                tasks_else.append(Parser.parseTask())
                                            result = IfOp([condition, Instructions(tasks_if), Instructions(tasks_else)])
                                            if Parser.tokenizer.next.type == "STOP":
                                                Parser.tokenizer.selectNext()
                                                if Parser.tokenizer.next.type == "ENDLINE":
                                                    Parser.tokenizer.selectNext()
                                                else:
                                                    raise Exception("Expected endline")
                                            else:
                                                raise Exception("Expected stop")
                                        else:
                                            raise Exception("Expected endline")
                                    else:
                                        raise Exception("Expected ':'")
                                else:
                                    raise Exception("Expected else")
                            else:
                                raise Exception("Expected endline")
                        else:
                            raise Exception("Expected ':'")
                        
        elif Parser.tokenizer.next.type == "ACTION":
            if inside_action == True:
                raise Exception("Cannot declare an action inside another action")
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                action = Identifier(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "OPENING_BRACKET":
                    Parser.tokenizer.selectNext()
                    arguments = []
                    if Parser.tokenizer.next.type != "CLOSING_BRACKET":
                        if Parser.tokenizer.next.type == "IDENTIFIER":
                            arguments.append(VarDec(Parser.tokenizer.next.value))
                            Parser.tokenizer.selectNext()
                        else:
                            raise Exception("Expected an identifier")
                        while Parser.tokenizer.next.type == "COMMA":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "IDENTIFIER":
                                arguments.append(VarDec(Parser.tokenizer.next.value))
                                Parser.tokenizer.selectNext()
                            else:
                                raise Exception("Expected an identifier")
                        if Parser.tokenizer.next.type != "CLOSING_BRACKET":
                            raise Exception("Expected ')'")
                        
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "TWO_DOTS":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "ENDLINE":
                            Parser.tokenizer.selectNext()
                            tasks = []
                            while Parser.tokenizer.next.type != "STOP":
                                tasks.append(Parser.parseTask(inside_action = True))
                            result = ActionDec([action, arguments, Instructions(tasks)])
                            if Parser.tokenizer.next.type == "STOP":
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "ENDLINE":
                                    Parser.tokenizer.selectNext()
                                else:
                                    raise Exception("Expected endline")
                            else:
                                raise Exception("Expected stop")
                        else:
                            raise Exception("Expected endline")
                    else:
                        raise Exception("Expected ':'")
                else:
                    raise Exception("Expected '('")
            else:
                raise Exception("Expected an identifier")
            
        elif Parser.tokenizer.next.type == "DO":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                action = Identifier(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "OPENING_BRACKET":
                    Parser.tokenizer.selectNext()
                    arguments = []
                    if Parser.tokenizer.next.type != "CLOSING_BRACKET":
                        if Parser.tokenizer.next.type == "INT":
                            arguments.append(IntVal(Parser.tokenizer.next.value))
                            Parser.tokenizer.selectNext()
                        else:
                            raise Exception("Expected an integer")
                        while Parser.tokenizer.next.type == "COMMA":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "INT":
                                arguments.append(IntVal(Parser.tokenizer.next.value))
                                Parser.tokenizer.selectNext()
                            else:
                                raise Exception("Expected an integer")
                        if Parser.tokenizer.next.type == "CLOSING_BRACKET":
                            result = ActionCall(action, arguments)
                            Parser.tokenizer.selectNext()
                        else:
                            raise Exception("Expected ')'")
                        
                    else:                 
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "ENDLINE":
                            Parser.tokenizer.selectNext()
                            result = ActionCall(action, arguments)
                        else:
                            raise Exception("Expected endline")
                else:
                    raise Exception("Expected '('")


        elif Parser.tokenizer.next.type == "ENDLINE":
            result = NoOp()
            Parser.tokenizer.selectNext()

        
        return result

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.position = 0
        Parser.tokenizer.selectNext()

        result = Parser.parseInstructions()
            
        return result


