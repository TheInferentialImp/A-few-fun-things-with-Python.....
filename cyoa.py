"""A sorry adventure."""
__author__ = "730622857"
from random import randint


RED_FLAG: str = "\U0001F6A9"
RAINBOW: str = "\U0001F7E5" + "\U0001F7E6" + "\U0001F7E7" + "\U0001F7EA" + "\U0001F7E8" + "\U0001F7E9"
WINK_TONGUE: str = "\U0001F61B" 
COWBOY_HAT: str = "\U0001F920"
points: int = 0
player: str = ""
i: int = 0


def main() -> None:
    """Call greet and game functions to bring everything together."""
    global i
    if i != 1:
        greet()
        i += 1
    playing: bool = True
    while playing:
        global points
        print(f"You currently have {points} Adventure Points!")
        x: str = input("Choose from the following two games or exit.\n(A) Life Choices \n(B) Pick a number \n(C) Exit. \nEnter your choice: ")
        while x != "A" and x != "B" and x != "C":
            x = input("You must enter either A, B, or C!\nEnter your choice: ")
        if x == "A":
            points += 10
            doors()
        elif x == "B":
            points += 10
            points = compare(points)
        elif x == "C":
            print(RAINBOW)
            print(f"Thanks for playing, have a great day! You scored {points} points!")
            exit()
        

def greet() -> None:
    """Greets the player and assigns inputted name to global variable 'player'."""
    global player
    player = input(f"Well how'dy {COWBOY_HAT}{COWBOY_HAT}{COWBOY_HAT}. And what might your name be? ")
    print(f"Nice to meet you, {player}!")
    print(RAINBOW)
    return None


def compare(points: int) -> int:
    """Begins a number guessing game from 1 to 20. The player has 5 guesses. Returns an integer to main."""
    print("In this game, a random number from 1 to 20 will be selected. You have a 5 guesses to get the correct number. \nYour points will be recorded in attempts.")       
    i: int = 1
    y: int = randint(1, 20)
    while i <= 5:
        x: int = (int(input("What is your guess? ")))
        while x == '':
            x = (int(input("Your guess must be a number between 1 and 20!\nEnter a guess: ")))
        if x < 1:
            x = (int(input("Your guess must be a number between 1 and 20!\nEnter a guess: ")))
        if x > 20:
            x = (int(input("Your guess must be a number between 1 and 20!\nEnter a guess: ")))
        if int(x) == int(y):
            print(f"Whohoo, {player}! You got it in {i} tries!")
            if i == 1:
                points += 100
            if i == 2:
                points += 80
            if i == 3:
                points += 60
            if i == 4:
                points += 40
            if i == 5:
                points += 20
            return points
        else:
            print("Maybe next time! +10 Adventure Points")
            points += 10
            i += 1
    return points


def doors() -> None:
    """Prompts the user with a series of questions. Points are given based on responses."""
    global points
    global player
    door_1: str = input("There's a porcupine! (A) Leave it or (B) kick it? \nEnter a choice: ")
    while door_1 == "":
        door_1 = print(input("You must choose either (A) or (B).\nEnter a choice: "))
    if door_1 == "A":
        points = points + 10
        print("Aw, that was nice of you.")
    if door_1 == "B":
        points = points + -10
        print(f"Really {player}, I'm calling the PETA. " + RED_FLAG + RED_FLAG + RED_FLAG)
    door_2: str = input("Are (A) cakes or (B) cupcakes better? ")
    if door_2 == "A":
        points = points + 10
        print("Red Velvet is the best!")
    if door_2 == "B":
        print("More the merrier!" + WINK_TONGUE)
        points = points - 10
    door_3 = input("COMP110 is being taught by Kris Jordan in the Spring. \nWill you enroll? If yes, enter (A) If no, enter (B): ")
    if door_3 == "A":
        points = points + 50
        print(f"Great choice, {player}!")
    if door_3 == "B":
        print("Your loss!")
        points = points - 30


if __name__ == "__main__":
    main()