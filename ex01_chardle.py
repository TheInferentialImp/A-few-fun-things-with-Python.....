"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730622857"
count = 0
word_of_the_day: str = input("Enter a 5-character word: ")
if len(word_of_the_day) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    desired_letter: str = input("Enter a single character: ")
    if len(desired_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + desired_letter + " in " + word_of_the_day)
        if desired_letter == word_of_the_day[0]:
            print((desired_letter) + " found at index 0")
            count = count + 1
        if desired_letter == word_of_the_day[1]:
            print((desired_letter) + " found at index 1")
            count = count + 1
        if desired_letter == word_of_the_day[2]:
            print((desired_letter) + " found at index 2")
            count = count + 1
        if desired_letter == word_of_the_day[3]:
            print((desired_letter) + " found at index 3")
            count = count + 1
        if desired_letter == word_of_the_day[4]:
            print((desired_letter) + " found at index 4")
            count = count + 1
        if count == 1:
            print("1 instance of " + (desired_letter) + " found in " + (word_of_the_day))
        if count == 2:
            print("2 instances of " + (desired_letter) + " found in " + (word_of_the_day))
        if count == 3:
            print("3 instances of " + (desired_letter) + " found in " + (word_of_the_day))
        if count == 4:
            print("4 instances of " + (desired_letter) + " found in " + (word_of_the_day))
        if count == 5:
            print("5 instances of " + (desired_letter) + " found in " + (word_of_the_day))
        if count == 0:
                print("No instances of " + (desired_letter) + " found in " + (word_of_the_day))