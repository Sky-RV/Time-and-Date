import imp
from tkinter import font
import colorama
from os import system
from colorama import init, Fore, Style
from pyfiglet import Figlet

system('cls') # clear the cmd screen

banner = Figlet(font="banner3")
print(Fore.GREEN + banner.renderText("Date Time") + Fore.WHITE)