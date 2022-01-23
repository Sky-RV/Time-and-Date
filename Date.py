import imp
from tkinter import font
import colorama
from os import system
from colorama import init, Fore, Style
from pyfiglet import Figlet

################################################## MAIN ##################################################

def main():
    print(Style.RESET_ALL)
    
    main_input = input(Fore.BLUE + ">> " + Fore.WHITE)

    if main_input == "1":
        pass
    elif main_input == "2":
        pass
    elif main_input == "3":
        pass
    elif main_input == "4":
        pass
    elif main_input == "5":
        pass
    elif main_input == "6":
        pass
    else:
        print(Fore.RED + ' Please enter a valid number...')
        main()

################################################## BODY ##################################################

def body():
    system('cls') # clear the cmd screen

    banner = Figlet(font="banner3")
    print(Fore.GREEN + banner.renderText(" Date Time") + Fore.WHITE)

    print("\n")

    print(" What do you want to use?")
    print(
        "  1. Persian Monthly Calendar\n" +
        "  2. English Monthly Calendar\n" +
        "  3. Timer\n" +
        "  4. Cornometer\n" +
        "  5. Convert Persian Calendar to English\n" +
        "  6. Convert English Calendar to Persian"
    )

body()
main()