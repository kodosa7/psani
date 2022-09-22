# this stupid game is based on a program for the commodore 64 computer written
# in commodore basic v2 by my schoolmate in 1990. it persisted on an old cassette-tape
# and this is the python version of it
# simply written as a nostalgic memory of good old days at school

import os, colorama
from colorama import init, Fore, Back, Style


def reset_colors():
    print(Fore.RESET + Back.RESET)

def cls():
    os.system('cls')  # replace 'cls' for 'clear' in *nix

def end():
    cls()
    reset_colors()
    print("\033[15;5H" + "TAK SES BLBEJ.")
    print("")
    print("")
    print("")

def game():
    print("\033[6;25H" + Back.BLUE + "                   ")
    print("\033[7;25H" + Back.BLUE + Fore.WHITE + "     P S A N I     ")
    print("\033[8;25H" + Back.BLUE + "                   ")
    reset_colors()

    text = input("\033[10;25H" + Fore.WHITE + "NAPIS NECO: ")

    cls()
    reset_colors()
    print("\033[6;25H" + Fore.CYAN + "CO TO TAM PISES ?!")
    reset_colors()

    again = input("\033[15;5H" + "CHCES PSAT DAL A/N ")
    if again == "A" or again == "a":
        cls()
        game()
    else:
        end()


if __name__ == "__main__":
    init()
    print(Style.RESET_ALL)
    cls()
    game()
