# Displays time since birth
import time
import datetime
import os


def clear():
    # clears the console
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


MONTHS = {
    "january": "Jan",
    "february": "Feb",
    "march": "Mar",
    "april": "Apr",
    "may": "May",
    "june": "Jun",
    "july": "Jul",
    "august": "Aug",
    "september": "Sep",
    "october": "Oct",
    "november": "Nov",
    "december": "Dec",
}


def user_input():
    while True:
        try:
            birth_day, birth_month, birth_year = input(
                "Enter birth day, month, year (space separated) (01 January 1970): "
            ).split()
            birth_day = int(birth_day)
            birth_month = birth_month.lower()
            if birth_month in MONTHS:
                birth_month = MONTHS[birth_month]
            elif len(birth_month) == 3 and birth_month.title() in MONTHS.values():
                birth_month = birth_month.title()
            else:
                print("Invaild input. Try again.")
            birth_year = int(birth_year)
        except KeyboardInterrupt:
            exit()
        except:
            print("Invalid input or input format. Try again.")
            continue

        if (1 < birth_day > 31) or (len(str(birth_year)) > 4):
            print("Invalid input. Try again.")
            continue
        return birth_day, birth_month, birth_year


birth_day, birth_month, birth_year = user_input()
bday = datetime.date(birth_year, time.strptime(birth_month, "%b").tm_mon, birth_day)
today = datetime.date.today()

then_timestamp = time.mktime(bday.timetuple())

while True:
    time.sleep(1)
    clear()
    now_timestamp = time.time()
    diff = now_timestamp - then_timestamp
    now_year = time.struct_time(datetime.date.today().timetuple()).tm_year
    print(
        f"Years: {now_year-birth_year}\nDays: {int(diff/86400)}\nHours: {int(diff/3600)}\nSeconds: {int(diff)}"
    )
