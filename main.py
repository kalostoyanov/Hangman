tries = 10
letter = ""
word = ""


def generate_word():
    global word
    import random
    with open("words.txt") as words_file:
        lines = words_file.read().splitlines()
    word = random.choice(lines)


def user_input():
    global letter
    letter = input("Please enter a letter: ").lower()
    while True:
        if letter.isalpha() and (len(letter) == 1):  # is this pythonic?
            break
        print("That's not one letter.")
        letter = input("Please try again: ").lower()


def check_letter():
    global tries
    global blank_word
    blank_word_list = []
    if letter in word:
        blank_word_list = list(blank_word)
        temporary_index = 0
        for i in word:
            if letter == i:
                blank_word_list[temporary_index] = letter
            temporary_index += 1
        blank_word = "".join(blank_word_list)
        print(f"This is your current progress: {blank_word}")
    else:
        tries -= 1
        print(f"I'm sorry, that's wrong. You still have {tries} tries left.")


generate_word()

# Generated blank
blank_word = "_" * len(word)

print(f"You start with {tries} tries.")
print("The lenght of the words is {0} characters.".format(len(blank_word)))

while tries != 0: # I could add a game over message
    user_input()
    check_letter()
    if "_" not in blank_word:
        print("Actually... When I think about it, this is it! You won!!!")  # Note: probably could be more elegant
        break