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
    while answer != '1' and answer != '2':
        answer = input("Welcome to Hangman!\n"
                       "[1] random word\n"
                       "[2] custom word\n")
    if answer == '1':
        randomizeWord()
    elif answer == '2':
        customizeWord()


def game():
    win = False
    currstage = 0
    currguess = ""
    currletter = ""
    for _ in range(len(guessingword)):
        currguess += "_"
    currguess += "\n"
    usedletters = set([])
    while not win:
        print(STAGES[currstage])
        print(currguess)
        print(list(reversed(list(usedletters))))
        while len(currletter) != 1 or not currletter.isalpha():
            currletter = input("What is your letter to guess?\n")
        i = 0
        indices = []
        for letter in guessingword:
            if letter == currletter:
                indices.append(i)
            i += 1
        if len(indices) == 0:
            print("Strike!\n")
            usedletters.add(currletter)
            currstage += 1
            if currstage >= 6:
                print(STAGES[currstage])
                print("Game over\nThe word was " + guessingword + "\n")
                break
        for index in indices:
            liststr = list(currguess)
            liststr[index] = currletter
            currguess = ''.join(liststr)
        currletter = ""
        if "_" not in currguess:
            win = True
            print("You won! The word was " + guessingword + "\n")


while quitGame != 'n':
    openingmenu()
    game()
    quitGame = input("Play again? [y] or [n]\n")
