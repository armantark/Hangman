import random

clear = "\n" * 100


def randomizeWord():
    global guessingword
    guessingword = random.choice(WORDS)
    print(clear)


def customizeWord():
    global guessingword
    guessingword = input("Enter your custom word: ")
    print(clear)


guessingword = ""
quitGame = ""
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

STAGES = ["┏━━┓\n┃\n┃\n┃\n┻━\n",
          "┏━━┓\n┃  O\n┃\n┃\n┻━\n",
          "┏━━┓\n┃  O\n┃  |\n┃\n┻━\n",
          "┏━━┓\n┃  O\n┃ /|\n┃\n┻━\n",
          "┏━━┓\n┃  O\n┃ /|\\\n┃\n┻━\n",
          "┏━━┓\n┃  O\n┃ /|\\\n┃ /\n┻━\n",
          "┏━━┓\n┃  O\n┃ /|\\\n┃ / \\\n┻━\n"]


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
    win = False
    currstage = 0
    currguess = ""
    for _ in range(len(guessingword)):
        currguess.join("_")
    while not win:
        print(STAGES[currstage])

        currstage += 1
        if currstage > 5:
            print("Game over\n")
            break



while quitGame != 'y':
    openingmenu()
    game()
    quitGame = input("Play again? [y] or [n]\n")
