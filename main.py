def generate_word():
    global word
    global blank_word
    import random
    with open("words.txt") as words_file:
        lines = words_file.read().splitlines()
    word = random.choice(lines)
    blank_word = "_" * len(word)


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
                blank_word_list[temporary_index] = letter  # too much denting, it's not pythonic
            temporary_index += 1
        blank_word = "".join(blank_word_list)
    else:
        tries -= 1
        print(f"I'm sorry, that's wrong.")
        if tries != 0:
            print(f"You still have {tries} tries left.")
        else:
            print("This was your last try...")
   


generate_word()
tries = 10

print(f"You start with {tries} tries.")
print("The length of the words is {0} characters.".format(len(blank_word)))

while tries != 0:
    user_input()
    check_letter()
    if ("_" in blank_word) and (tries != 0):
        print(f"This is your current progress: {blank_word}")
    elif "_" not in blank_word:
        print(f"Congrats! You won! You guessed correctly \"{word}\".")
        break
else:
    print("GAME OVER!")