import imp
from tkinter import font
import colorama
from os import system
from colorama import init, Fore, Style
from pyfiglet import Figlet
import time
import calendar

DAYS = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
DAYS_small = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MONTHS_small = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', "Aug", 'Sep', 'Oct', 'Nov', 'Dec']

################################################## MAIN ##################################################

def main():
    print(Style.RESET_ALL)
    
    main_input = input(Fore.BLUE + " >> " + Fore.WHITE)

    if main_input == "1":
        pass
    elif main_input == "2":
        English_Monthly_Calendar()
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
        main() # if you want in input more and more in one screen
        # body() # if you want to reset the code and enter new input in new screen

################################################## PERSIAN MONTHLY CALENDAR ##################################################

################################################## ENGLISH MONTHLY CALENDAR ##################################################

def English_Monthly_Calendar():
    system('cls')
    print(Fore.YELLOW + " English Monthly Calendar\n\n")

    print(Fore.WHITE + ' Enter Month (1-12) :')
    en_month_input = input(Fore.BLUE + " >> ")

    now = time.ctime()
    this_year = time.strftime('%Y')
    this_month_num = time.strftime("%m") # this month in number
    this_month_voc = time.strftime("%B") # this month in words

    print('\n')

    print(Fore.CYAN + " " + calendar.month(int(this_year), int(en_month_input)))
    print(Style.RESET_ALL)

    print(Fore.WHITE + " Back to main ? (y/n)")
    answer = input(Fore.BLUE + ' >> ')
    if answer == 'y':
        body()
    else:
        pass

    # print(Fore.CYAN + "\t " + this_year + " " + this_month_voc)
    # print(Fore.CYAN + " " + " ".join(DAYS_small))
    # print(Style.RESET_ALL)

    # for i in range(1, 13):
        

################################################## TIMER ##################################################

################################################## CORNOMETER ##################################################

################################################## CONVERT P to E CALENDAR ##################################################

################################################## CONVERT E to P CALENDAR ##################################################

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

    main()

body()
main()