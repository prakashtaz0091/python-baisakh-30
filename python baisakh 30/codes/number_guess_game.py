import random
from os import system

WIN = False
LIFE = 10

secret_number = random.randint(1, 20)

sad_emojis = {
    9: "🙁",
    8: "😟",
    7: "😞",
    6: "😔",
    5: "😕",
    4: "😢",
    3: "☹️",
    2: "😥",
    1: "😿",
    0: "😭",
}

WIN_RESULT_WINDOW = """
    ##############################
    #                            #
    #      Congratulations 🎉    #
    #       you won the game     #
    ##############################

"""
LOSE_RESULT_WINDOW = f"""
    ##############################
    #                            #
    #         Sorry, 🙁          #
    #     You lost the game      #
    #  Secret = {secret_number:^10}  #
    ##############################

"""


while LIFE > 0:
    guess = int(input("Enter a number (1-100)"))

    if guess == secret_number:
        WIN = True
        break
    else:
        system("clear")
        LIFE = LIFE - 1
        print(f"You have {LIFE} lives left {sad_emojis[LIFE]}")

system("clear")

if WIN:
    print(WIN_RESULT_WINDOW)
else:
    print(LOSE_RESULT_WINDOW)
