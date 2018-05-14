import random

clear = "\n" * 100
def randomizeWord():
    global guessingword = random.choice(WORDS)
    print(clear)

def customizeWord():
    guessingword = input("Enter your custom word: ")
    print(clear)

guessingword = ""
quitGame = ""
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

STAGE0 = "┏━━┓\n┃\n┃\n┃\n┻━\n"
STAGE1 = "┏━━┓\n┃  O\n┃\n┃\n┻━\n"
STAGE2 = "┏━━┓\n┃  O\n┃  |\n┃\n┻━\n"
STAGE3 = "┏━━┓\n┃  O\n┃ /|\n┃\n┻━\n"
STAGE4 = "┏━━┓\n┃  O\n┃ /|\\\n┃\n┻━\n"
STAGE5 = "┏━━┓\n┃  O\n┃ /|\\\n┃ /\n┻━\n"
STAGE6 = "┏━━┓\n┃  O\n┃ /|\\\n┃ / \\n┻━\n"

def openingmenu():
    answer = 0
    while answer != 1 or answer != 2:
        answer = input("Welcome to Hangman!\n"
                       "[1] random word\n"
                       "[2] custom word\n")
    if answer == 1:
        randomizeWord()
    elif answer == 2:
        customizeWord()

def game():

while quitGame != 'y':
    openingmenu()




