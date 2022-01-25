import datetime
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
        Timer()
    elif main_input == "4":
        Chronometer()
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
    this_day = time.strftime('%d')
    this_month_num = time.strftime("%m") # this month in number
    this_month_voc = time.strftime("%B") # this month in words

    print('\n')

    print(Fore.LIGHTYELLOW_EX + ' Today : ' + this_month_num + ' / ' + this_day + ' / ' + this_year + '\n')

    print(Fore.CYAN + " " + calendar.month(int(this_year), int(en_month_input)))
    print(Style.RESET_ALL)

    print(Fore.WHITE + " Back to main ? (y/n)")
    answer = input(Fore.BLUE + ' >> ')
    if answer == 'y':
        main()
    else:
        pass

    # print(Fore.CYAN + "\t " + this_year + " " + this_month_voc)
    # print(Fore.CYAN + " " + " ".join(DAYS_small))
    # print(Style.RESET_ALL)

    # for i in range(1, 13):
        

################################################## TIMER ##################################################

def Timer():
    system('cls')
    print(Fore.YELLOW + " Timer\n\n")

    print(Fore.WHITE + " Enter the time in hour : ")
    timer_hour_input = int(input(Fore.BLUE + " >> "))

    print(Fore.WHITE + " Enter the time in minute : ")
    timer_minute_input = int(input(Fore.BLUE + " >> "))

    print(Fore.WHITE + " Enter the time in second : ")
    timer_second_input = int(input(Fore.BLUE + " >> "))

    print()

    # countdown(int(timer_input)) # input must be by seconds

    CountDown(timer_hour_input, timer_minute_input, timer_second_input)

def CountDown (h, m, s):
    
    total_seconds = (h * 3600) + (m * 60) + s
 
    print(Fore.YELLOW)

    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(" " ,timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print()  
    print(Fore.RED + '\n Timer Finished')

    if total_seconds == 0:
        print(Fore.WHITE + " Do you want to continue ? (y/n/home)")
        answer_timer = input(Fore.BLUE + " >> ")
        
        if answer_timer == 'y':
            Timer()
        elif answer_timer == 'home':
            main()
        else:
            pass

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(Fore.YELLOW + " " + timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print()  
    print(Fore.RED + '\n Timer Finished')

    if t == 0:
        print(Fore.WHITE + " Do you want to continue ? (y/n/home)")
        answer_timer = input(Fore.BLUE + " >> ")
        
        if answer_timer == 'y':
            Timer()
        elif answer_timer == 'home':
            main()
        else:
            pass

################################################## CHORNOMETER ##################################################

def Chronometer():
    system('cls')
    print(Fore.YELLOW + " Chronometer\n\n")

    print(Fore.WHITE + " Press Enter to start...\n")
    start_time = time.time()

    

    #Chronometer_input = input(Fore.WHITE + 'Press 1 to start\n' + Fore.BLUE + ' >> ')

    # if Chronometer_input == '1':
        
    #     # Counting Clock
    #     while True:
    #         localtime = time.localtime()
    #         res = time.strftime('%S', localtime)
    #         print(Fore.YELLOW + " " + res)
    #         time.sleep(1)
    #         system('cls')

def time_chronometer(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    print(Fore.YELLOW + "Time lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


################################################## CONVERT P to E CALENDAR ##################################################

################################################## CONVERT E to P CALENDAR ##################################################

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
    "  4. Chronometer\n" +
    "  5. Convert Persian Calendar to English\n" +
    "  6. Convert English Calendar to Persian"
)

main()