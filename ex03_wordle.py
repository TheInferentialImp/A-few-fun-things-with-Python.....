"""EXO3 - Worldle: my first program using a function."""

__author__ = "730622857"

def contains_char(guess: str, letter: str) -> bool:
    """Indexes the guess for a specified character and returns a boolean value."""
    assert len(letter) == 1
    i: int = 0
    while i < len(guess):
        if guess[i] == letter:
            return True
        else: i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Color codifies characters based on appearance and position in the secret word."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    status: str = ""
    i: int = 0
    while i < len(guess): 
        if guess[i] == secret[i]:
             # if the secret contains a character in the right place, a green box is concatonated
            status = status + GREEN_BOX
        elif contains_char(secret, guess[i]): 
            # if the secret contains a character in any of its indices, it will concatonate a yellow box, otherwise () a white box.
            status = status + YELLOW_BOX
        else: 
            status = status + WHITE_BOX
        i += 1 # increments i to close loop
    return status


def input_guess(expected_length: int) -> str: 
    """It's purpose is given an length of a word, it will prompt the user for a guess and continue prompting them until they provide a guess of the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ") 
    # prompts user for a guess
    while len(guess) != expected_length: 
        # loop ensures guess is proper length
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None: 
    # beginning of game, calls functions together
    """Entrypoint of the program and main game loop."""
    turn: int = 1
    playing: bool = True
    secret: str = "codes"
    while playing is True and turn <= 6: # player hasn't guessed correctly and is has less than/equal to 6 guesses left
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess,secret)) # calls emojified and compares arguments from secret and inputted guesses
        if guess == secret: # ends game by changing playing to False and exiting
            print(f"You won in {turn}/6 turns!")
            playing is False
            return None
        turn += 1
    if turn > 6: 
        # if player reaches maximum amount of tries, it prints and exits.
        print("X/6 - Sorry, try again tomorrow!")
        return None


if __name__ == "__main__": 
    # allows module to be ran from zsh
    main()