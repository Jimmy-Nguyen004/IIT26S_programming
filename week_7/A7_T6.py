# setup
import random
random.seed(1234)

Choices = ("rock", "paper", "scissors")

# ASCII art
# use multiline string """........"""
arts = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

class PLAYER:
    name = ""
    wins = 0
    losses = 0
    draws = 0

def showMenu() -> None:
    print()
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    return None

def showChoice(PPlayer: PLAYER, PChoice: int) -> None:
    print("{} chose {}.".format(PPlayer.name, Choices[PChoice - 1]))
    print(arts[PChoice - 1])
    print("#" * 25)
    return None

def play(PUser: PLAYER, PBot: PLAYER, PUserChoice: int) -> None:
    BotChoice = random.randint(1, 3)
    print("Rock! Paper! Scissors!")
    showChoice(PUser, PUserChoice)
    showChoice(PBot, BotChoice)
    print()
    if PUserChoice == BotChoice:
        print("Draw! Both players chose {}.".format(Choices[PUserChoice - 1]))
        PUser.draws += 1
        PBot.draws += 1
        return None
    if (PUserChoice == 1 and BotChoice == 3) or (PUserChoice == 2 and BotChoice == 1) or (PUserChoice == 3 and BotChoice == 2):
        print("{} {} beats {} {}".format(PUser.name, Choices[PUserChoice - 1], PBot.name, BotChoice))
        PUser.wins += 1
        PBot.losses += 1
    else:
        print("{} {} beats {} {}".format(PBot.name, BotChoice, PUser.name, Choices[PUserChoice - 1]))
        PUser.losses += 1
        PBot.wins += 1
    return None

def showResults(PUser: PLAYER, PBot: PLAYER) -> None:
    print()
    print("Results:")
    print("{} - wins ({}) - losses ({}) - draws ({})".format(PUser.name, PUser.wins, PUser.losses, PUser.draws))
    print("{} - wins ({}) - losses ({}) - draws ({})".format(PBot.name, PBot.wins, PBot.losses, PBot.draws))
    print()

def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    User = PLAYER()
    User.name = input("Insert player name: ")
    Bot = PLAYER()
    Bot.name = "RPS-3PO"
    print("Welcome!\nYour opponent is {}.\nGame starts...".format(User.name, Bot.name))
    while True:
        showMenu()
        choice = input("Your choice: ")
        if choice == "1" or choice == "2" or choice == "3":
            play(User, Bot, int(choice))
        elif choice == "0":
            break
        else:
            print("Unknown option.")
    showResults(User, Bot)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()