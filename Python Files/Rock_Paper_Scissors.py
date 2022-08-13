import random
import sys

choices = ["Rock", "Paper", "Scissors"]

b = random.choice(choices)
retry = input("Do You Want To Play?:")


if retry == "no":
    print("ok")
    sys.exit(0)

x = 0
e = 0
Retry = True

while Retry:

    a = input("\nChoose your fighter:")
    b = random.choice(choices)
    uppera = a[0].upper()+ a[1::]
    if uppera == b:
        print("Draw")
        print(f'bot chooses {b}')
        print("Bot " + str(e) + " " + "You " + str(x))

    elif a == "Rock" or a == 'r' or a == 'R' or a == 'rock' and b == "Scissors":
        print("Bot Chooses Scissors")
        print("you Win!")
        x = x + 1
        print("Bot " + str(e) + " " + "You " + str(x))

    elif a == "Scissors" or a == 's' or a == 'S' or a == 'scissors' and b == "Rock":
        print("Bot Chooses Rock")
        print("You Lose!")
        e = e + 1
        print("Bot " + str(e) + " " + "You " + str(x))

    elif a == "Paper" or a == 'P' or a == 'p' or a == 'paper' and b == "Scissors":
        print("Bot Chooses Scissors")
        print("You Lose!")
        e = e + 1
        print("Bot " + str(e) + " " + "You " + str(x))

    elif a == "Scissors" or a == 's' or a == 'S' or a == 'scissors' and b == "Paper":
        print("Bot Chooses Paper")
        print("You Win!")
        x = x + 1
        print("Bot " + str(e) + " " + "You " + str(x))

    elif a == "Rock" or a == 'r' or a == 'R' or a == 'rock' and b == "Paper":
        print("Bot Chooses Paper")
        print("You Lose!")
        e = e + 1
        print("Bot " + str(e) + " " + "You " + str(x))

    elif a == "Paper" or a == 'P' or a == 'p' or a == 'paper'  and b == "Rock":
        print("Bot Chooses Rock")
        print("You Win")
        x = x + 1
        print("Bot " + str(e) + " " + "You " + str(x))

    if x == 3 or e == 3:
        x = x - x
        e = e - e
        print("Good Job")
        retry = input("Wanna Play Again?:")
        if retry == "yes" or retry == 'y' or retry == 'Y' or retry == 'Yes':
            pass
        else:
            Retry = False
            print("ok")
            
