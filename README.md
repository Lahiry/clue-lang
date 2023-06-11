# Robot Lang 🤖

## EBNF

```python
 INSTRUCTIONS = { TASK } 
 
 TASK = { WALK | TURN | PICK | DROP | REPEAT | (IF | IF, ELSE) | ACTION | DO } 
  
 WALK = "walk", ({ DIGIT } | IDENTIFIER), "steps", "\n"
 
 TURN = "turn", ({ DIGIT } | IDENTIFIER), "degrees to the", { ORIENTATION }, "\n"
 
 ORIENTATION = "left" | "right"
 
 PICK = "pick", IDENTIFIER, "\n"
 
 DROP = "drop", IDENTIFIER, "\n"
 
 REPEAT = "repeat", ({ DIGIT } | IDENTIFIER), "times:", "\n", INSTRUCTIONS, STOP, "\n"
 
 IF = "if", CONDITIONAL, ":", "\n", INSTRUCTIONS, STOP, "\n"
 
 ELSE = "else", ":", "\n", INSTRUCTIONS, STOP, "\n"
 
 CONDITIONAL = ("holding" | NOT, "holding"), IDENTIFIER
 
 ACTION = "action", IDENTIFIER, "(", PARAMETERS, ")", ":", "\n", INSTRUCTIONS, STOP, "\n"
  
 PARAMETERS = [ identifier { ",", identifier } ]
 
 DO = "do", IDENTIFIER, "\n"
 
 STOP = "stop"
 
 NOT = "!"

LETTER = ("a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z")

DIGIT = ("0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9")

IDENTIFIER = { LETTER | DIGIT }
```

## Exemplo de uso

```lua
walk 3 steps
turn 90 degrees to the left
walk 2 steps
pick box

repeat 3 times:
  turn 90 degrees to the right
  walk 2 steps
  turn 90 degrees to the right
  walk 5 steps
stop

if !holding box:
  pick box
else:
  drop box
stop

action square(x, y):
  repeat x times:
    walk y steps
    turn 90 degrees to the left
   stop
  stop
 
do square(3, 2)
```
