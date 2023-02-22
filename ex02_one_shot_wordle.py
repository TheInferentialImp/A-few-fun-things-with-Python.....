"""EX02 - One Shot Wordle - Loops."""

__author__ = "730622857"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word = str("python")
guess: str = (input(f"What is your {len(secret_word)}-letter guess? "))
letter: str = ""
i: int = 0
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
while i < len(secret_word):
    if guess[i] == secret_word[i]:
        letter = letter + GREEN_BOX
        i = i + 1
    else:
        e: int = 0
        match: bool = False
        while e < len(secret_word) and match is False:
            if guess[i] == secret_word[e]:
                match = True
            e += 1
        if match:
            letter += YELLOW_BOX
        else:
            letter += WHITE_BOX
        i += 1
if letter != GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
print(f"{letter}")