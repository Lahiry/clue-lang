# Robot Lang 🤖

## EBNF

```python
 INSTRUCTIONS = { TASK } 
 
 TASK = { ASSIGNMENT | WALK | TURN | PICK | DROP | REPEAT | IF | ACTION | DO } 
 
 ASSIGNMENT = IDENTIFIER, "=", { DIGIT } 
 
 WALK = "walk", { DIGIT }, "steps", "\n"
 
 TURN = "turn", { DIGIT }, "degrees to the", { ORIENTATION }, "\n"
 
 ORIENTATION = "left" | "right"
 
 PICK = "pick", IDENTIFIER, "\n"
 
 DROP = "drop", IDENTIFIER, "\n"
 
 REPEAT = "repeat", { DIGIT }, "times:", "\n", INSTRUCTIONS, STOP, "\n"
 
 IF = "if", CONDITIONAL, ":", "\n", INSTRUCTIONS, STOP, "\n"
 
 CONDITIONAL = ("holding" | "not holding"), IDENTIFIER
 
 ACTION = "action", IDENTIFIER, "(", PARAMETERS, ")", ":", "\n", INSTRUCTIONS, STOP, "\n"
  
 PARAMETERS = [ identifier { ",", identifier } ]
 
 DO = "do", IDENTIFIER, "\n"
 
 STOP = "stop"

LETTER = ("a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z")

DIGIT = ("0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9")

IDENTIFIER = { LETTER | DIGIT }
```

## Exemplo de uso

```lua
walk 3 steps
turn 90 degrees to the left
walk 2 steps forward

pick box

x = 3

repeat x times:
  turn 90 degrees to the right
  walk 2 steps
  turn 90 degrees to the right
  walk 5 steps
stop

if holding box:
  drop box
stop

action square(x, y):
  repeat x times:
    walk y steps
    turn 90 degrees to the left
   stop
 stop
 
 do square

```
