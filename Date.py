import imp
from tkinter import font
import colorama
from os import system
from colorama import init, Fore, Style
from pyfiglet import Figlet

################################################## BODY ##################################################

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

choose_input = input(Fore.BLUE + ">> " + Fore.WHITE)

