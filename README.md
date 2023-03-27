# Clue Lang 🕵️

## EBNF

```python
CLUE = "There has been a murder at Tudor Mansion", "\n", { CHOOSE_SUSPECT }, DEFINE_CRIME, INVESTIGATION, SUSPECT, "is arrested for murder"

SUSPECT = "Miss Scarlett" | "Colonel Mustard" | "Doctor Orchid" | "Reverend Green" | "Mrs. Peacock" | "Professor Plum"

WEAPON = "Candlestick" | "Dagger" | "Lead Pipe" | "Revolver" | "Rope" | "Wrench"

LOCATION = "Ballroom" | "Billiard Room" | "Conservatory" | "Dining Room" | "Hall" | "Kitchen" | "Library" | "Lounge" | "Study"

CHOOSE_SUSPECT = IDENTIFIER, "is", SUSPECT, "\n"

DEFINE_CRIME = "The murder was done by", SUSPECT, "with a", WEAPON, "in the", LOCATION, "\n"

ACCUSATION = IDENTIFIER, "accuses", SUSPECT, "in the", LOCATION, "with a", WEAPON, "\n"

INVESTIGATION = "While the crime is not solved", { ACCUSATION }, "The crime has been solved", "\n"

LETTER = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

DIGIT = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

IDENTIFIER = { LETTER | DIGIT }
```

## Exemplo de uso

```lua
There has been a murder at Tudor Mansion

player_1 is Colonel Mustard
player_2 is Reverend Green
player_3 is Miss Scarlett
player_4 is Mrs. Peacock

The murder was done by Reverend Green with a Revolver in the Lounge

While the crime is not solved 
player_1 accuses Miss Scarlet in the Ballroom with a Candlestick
player_2 accuses Reverend Green in the Lounge with a Revolver
The crime has been solved

Reverend Green is arrested for murder
```
