import datetime
from datetime import datetime
from email.utils import localtime
import sys
import pytz
from tkinter import font
from persiantools.jdatetime import JalaliDate
import colorama
from os import system
from colorama import init, Fore, Style
from pyfiglet import Figlet
import time
import calendar

DAYS = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
DAYS_INT = [0, 1, 2, 3, 4, 5, 6]
DAYS_small = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
PER_DAYS = ['Shanbe', '1 Shanbe', '2 Shanbe', '3 Shanbe', '4 Shanbe', '5 Shanbe', 'Jomae']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
PER_MONTHS = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Day', 'Bahman', 'Esfand']
MONTHS_small = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', "Aug", 'Sep', 'Oct', 'Nov', 'Dec']

SEASOND = ['Spring', 'Summer', 'Fall', 'Winter']
PER_SEASONS = ['Bahar', 'Tabestan', 'Paiz', 'Zemestan']

################################################## MAIN ##################################################

def main():
    print(Style.RESET_ALL)
    
    main_input = input(Fore.BLUE + " >> " + Fore.WHITE)

    if main_input == "1":
        Persian_Monthly_Calendar()
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
    elif main_input == '7':
        Today_Time()
    elif main_input == '8':
        Today_Date()
    else:
        print(Fore.RED + ' Please enter a valid number...')
        main() # if you want in input more and more in one screen
        # body() # if you want to reset the code and enter new input in new screen

################################################## PERSIAN MONTHLY CALENDAR ##################################################

def Persian_Monthly_Calendar():
    system('cls')
    print(Fore.YELLOW + " Persian Monthly Calendar\n\n")

    print(Fore.WHITE + ' Enter Month (1-12) :')
    per_month_input = input(Fore.BLUE + " >> ")

    now = JalaliDate.today()
    this_year = JalaliDate.today().year
    this_month = JalaliDate.today().month
    this_day = JalaliDate.today().day
    this_season = ""
    this_month_v = ""
    this_day_v = ""

    if this_month == 1 or this_month == 2 or this_month == 3:
        this_season = 'Bahar'
    elif this_month == 4 or this_month == 5 or this_month == 6:
        this_season = 'Tabestan'
    elif this_month == 7 or this_month == 8 or this_month == 9:
        this_season = 'Paiz'
    else:
        this_season = 'Zemestan'
    
    en_day = time.strftime("%A")
    for i in DAYS_INT:
        if en_day in DAYS[i]:
            this_day_v = PER_DAYS[i]

    for j in range(1, 13):
        if this_month == j:
            this_month_v = PER_MONTHS[j]

    print('\n')
    print(Fore.LIGHTYELLOW_EX + ' Today : ' + str(this_year) + ' / ' + str(this_month) + ' / ' + str(this_day))
    print(Fore.LIGHTYELLOW_EX + ' Today : ' + str(this_season) + ' - ' + str(this_month_v) + ' - ' + str(this_day_v) + '\n')

    # Show input's month

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
    this_day_v = time.strftime('%A')
    this_season = ""
    
    if this_month_num == 1 or this_month_num == 2 or this_month_num == 3:
        this_season = 'Spring'
    elif this_month_num == 4 or this_month_num == 5 or this_month_num == 6:
        this_season = 'Summer'
    elif this_month_num == 7 or this_month_num == 8 or this_month_num == 9:
        this_season = 'Fall'
    else:
        this_season = 'Winter'

    print('\n')

    print(Fore.LIGHTYELLOW_EX + ' Today : ' + this_month_num + ' / ' + this_day + ' / ' + this_year)
    print(Fore.LIGHTYELLOW_EX + ' Today : ' + this_day_v + ' - ' + this_month_voc + ' - ' + this_season + '\n')

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

    print(Fore.WHITE + " Press S to start...\n" +
                        " Press E to stop...\n" + 
                        " Press Enter for each lap...")
    start_time = time.time()
    end_time = start_time
    lap = 1
    value = ""

    while value.lower() != "e":
        value = input(Fore.BLUE + " >> ")

        lap_time = round((time.time() - end_time), 2)
        total_time = round((time.time() - start_time), 2)

        # Here, should be counter time

        print(Fore.YELLOW + " Lap No. " + str(lap))
        print(Fore.YELLOW + ' Total Time : ' + str(total_time))
        print(Fore.YELLOW + " Lap Time : " + str(lap_time))

        end_time = time.time()
        lap += 1

    print()  
    print(Fore.RED + '\n Timer Finished')

    if value == 'E' or value == 'e':
        print(Fore.WHITE + " Do you want to continue ? (y/n/home)")
        answer_timer = input(Fore.BLUE + " >> ")
        
        if answer_timer == 'y':
            Timer()
        elif answer_timer == 'home':
            main()
        else:
            pass

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

################################################## TODAY'S TIME ##################################################

def Today_Time():

    system('cls')
    banner = Figlet(font="banner3")
    print(Fore.YELLOW + banner.renderText(" Time"))

    print(Style.RESET_ALL)

    # Your Time Zone
    e_now = time.ctime()
    e_current_time = time.strftime("%H : %M : %S")

    # America / New York Time Zone
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    NY = datetime_NY.strftime("%H : %M : %S")

    # Iran / Tehran Time Zone
    tz_Tehran = pytz.timezone('Asia/Tehran')
    datetime_Teharan = datetime.now(tz_Tehran)
    IT = datetime_Teharan.strftime("%H : %M : %S")

    print(Fore.CYAN + " Current Your Timezone     = " + e_current_time)
    print(Fore.CYAN + " Current New York Timezone = " + NY)
    print(Fore.CYAN + " Current Tehran Timezone   = " + IT)

    #Count_Time('s')

    print("\n" + Style.RESET_ALL)

    print(Fore.WHITE + " Back to main ? (y/n)")
    answer = input(Fore.BLUE + ' >> ')
    if answer == 'y':
        main()
    else:
        pass

def Count_Time(start):
    while start:
        localtime = time.localtime()
        res = time.strftime(Fore.CYAN + " %H : %M : %S", localtime)
        print(res, end="\r")
        time.sleep(1)

################################################## TODAY'S DATE ##################################################

def Today_Date():
    
    system('cls')
    banner = Figlet(font="banner3")
    print(Fore.YELLOW + banner.renderText(" Date"))

    print(Style.RESET_ALL)

    # Your Date Zone
    now = time.ctime() # Wed Jan 26 23:58:18 2022
    cuttent_time = time.strftime("%d / %m / %Y") # 30 / 10 / 2020
    current_time_w = time.strftime("%A - %B") # sunday - march

    # America / New York Date Zone
    ny_current = time.strftime("%m / %d / %Y") # 1 / 27 / 2022
    ny_current_w = time.strftime("%A %B %d %Y") # sunday march 3 2012

    # Iran / Tehran Date Zone
    this_month = ""
    this_day = ""
    it_now = JalaliDate.today() # 1400-11-7
    it_current = str(it_now.year) + ' / ' + str(it_now.month) + ' / ' + str(it_now.day)

    en_day = time.strftime("%A")
    for i in DAYS_INT:
        if en_day in DAYS[i]:
            this_day = PER_DAYS[i]

    for j in range(1, 13):
        if it_now.month == j:
            this_month = PER_MONTHS[j]

    it_current_w = this_day + " " + this_month + " " + str(it_now.year)

    print(Fore.WHITE + " Current Your Date Zone     : \n " + Fore.CYAN +
                        cuttent_time + '\n ' +
                        current_time_w)

    print(Fore.GREEN + " ----------------------------------------------------------------------------------")

    print(Fore.WHITE + " Current New York Date Zone : \n " + Fore.CYAN +
                        ny_current + '\n ' +
                        ny_current_w)

    print(Fore.GREEN + " ----------------------------------------------------------------------------------")

    print(Fore.WHITE + " Current Tehran Date Zone   : \n " + Fore.CYAN +
                        it_current + '\n ' + 
                        it_current_w)

    print("\n" + Style.RESET_ALL)

    print(Fore.WHITE + " Back to main ? (y/n)")
    answer = input(Fore.BLUE + ' >> ')
    if answer == 'y':
        main()
    else:
        pass

################################################## BODY ##################################################


system('cls') # clear the cmd screen

banner = Figlet(font="banner3")
print(Fore.GREEN + banner.renderText(" Date Time") + Fore.WHITE)

print("\n")

print(" What do you want to use?")
print(
    "  1. Persian Monthly Calendar\n" +
    "  2. English Monthly Calendar\n" + # done
    "  3. Timer\n" + # done
    "  4. Chronometer\n" + # half
    "  5. Convert Persian Calendar to English\n" +
    "  6. Convert English Calendar to Persian\n" +
    "  7. Today's Time\n" +
    "  8. Today's Date"
)

main()