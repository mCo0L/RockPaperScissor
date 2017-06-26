import random
import time
rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: rock}

player_score = 0
computer_score = 0

def start():
    print("Lets play a game of Rock, Paper, Scissors.")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print()
        player = input("Rock = 1\n   ......   \n  ...  ...  \n ...    ... \n...      ...\n... ROCK ...\n...      ...\n ...    ... \n  ...  ...  \n   ......   \nPaper = 2\n............\n...      ...\n...      ...\n...PAPER ...\n...      ...\n...      ...\n............\nScissors = 3 \n  ...        ... \n ... ...   ... ...\n ... ...   ... ...\n    ..       .. \n     ..     ..  \n       ....   \n     SCISSOR   \n       ....   \n      ..  ..  \n     ..    .. \n    .        .\nMake a move: ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Oops! I didnt understand that. Please Enter 1, 2 or 3.")

def result(player, computer):
    print("Rock...   ......   \n         ...  ...  \n        ...    ... \n       ...      ...\n       ... ROCK ...\n       ...      ...\n        ...    ... \n         ...  ...  \n          ......   ")
    time.sleep(1)
    print("Paper...............\n        ...      ...\n        ...      ...\n       ...PAPER ...\n        ...      ...\n        ...      ...\n        ............\n")
    time.sleep(1)
    print("Scissors...  ...        ... \n            ... ...   ... ...\n            ... ...   ... ...\n               ..       .. \n                ..     ..  \n                  ....   \n                SCISSOR   \n                  ....   \n                 ..  ..  \n                ..    .. \n               .        .")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("Your victory has been assured.")
            player_score += 1
        else:
            print("The computer laughs at you as you realise you have been defeated.")
            computer_score += 1

def play_again():
    answer = input("Would you like to play Again? y/n: ")
    if answer in ("Y", "y"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")

def scores():
    global player_score, computer_score
    print("High Scores")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


start()
