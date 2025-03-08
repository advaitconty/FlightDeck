import sys
from files import handler
from colorama import Fore, Style
import colorama
import file_path
import timer.pomodoro
import vault
import random
import string
import weather
import api_key

WORDS = ["apple", "tiger", "ocean", "planet", "rocket", "guitar", "silver", "forest", "sunset", "mountain"]

def create_password(characters=14, lowercase=True, uppercase=True, numbers=True, symbols=True, readable=False):
    if readable:
        num_words = max(2, characters // 6)  # Adjust number of words based on length
        password = "-".join(random.choices(WORDS, k=num_words)).capitalize()
        if numbers:
            password += str(random.randint(10, 99))

        print(password)
    else:
        pool = ""
        if lowercase:
            pool += string.ascii_lowercase
        if uppercase:
            pool += string.ascii_uppercase
        if numbers:
            pool += string.digits
        if symbols:
            pool += "!@#$%^&*()_-+=<>?/"

        print("".join(random.choices(pool, k=characters)))

def convert_text_to_bool(text):
    if text.lower() == "true":
        return True
    elif text.lower() == "false":
        return False
    else:
        raise ValueError("Invalid input.")

colorama.init(autoreset=True)

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "help":
        with open("help.txt") as f:
            print(f.read())
    
    # Files
    elif command == "open" and len(sys.argv) > 2:
        print("Reading file...")
        handler.read_file(file_path.get_full_path(sys.argv[2]))
    elif command == "open" and len(sys.argv) < 2:
        print(Fore.RED + "⚠ Error: No file provided")
        print("Usage: flightdeck open [file]")

    # Solstice
    elif command == "solstice":
        try:
            if len(sys.argv) > 2:
                if sys.argv[2].isdigit():
                    timer.pomodoro.start_timer(work_time=int(sys.argv[2]))
                elif sys.argv[2] == "help":
                    print("Usage: flightdeck solstice [work_time] [break_time]")
            elif len(sys.argv) > 3:
                timer.pomodoro.start_timer(work_time=int(sys.argv[2]), break_time=int(sys.argv[3]))
            elif len(sys.argv) > 1:
                timer.pomodoro.start_timer()
        except:
            print(Fore.RED + "⚠ Error: Invalid arguments" + Style.RESET_ALL)
            print("Usage: flightdeck solstice [work_time] [break_time]")

    # FlightDeck Vault
    elif command == "secure-vault":
        vault.main_loop()

    elif command.startswith("password"):
        if len(sys.argv) == 2 and sys.argv[1] == "help":
            print("Usage: flightdeck password [characters] [lowercase] [uppercase] [numbers] [symbols]")
            print("Default: flightdeck password 16 true true true true false")
        # try:
        if len(sys.argv) == 2:
            create_password()
        elif len(sys.argv) == 3:
            create_password(int(sys.argv[2]))
        elif len(sys.argv) == 4:
            create_password(int(sys.argv[2]), convert_text_to_bool(sys.argv[3]))
        elif len(sys.argv) == 5:
            create_password(int(sys.argv[2]), convert_text_to_bool(sys.argv[3]), convert_text_to_bool(sys.argv[4]))
        elif len(sys.argv) == 6:
            create_password(int(sys.argv[2]), convert_text_to_bool(sys.argv[3]), convert_text_to_bool(sys.argv[4]), convert_text_to_bool(sys.argv[5]))
        elif len(sys.argv) == 7:
            create_password(int(sys.argv[2]), convert_text_to_bool(sys.argv[3]), convert_text_to_bool(sys.argv[4]), convert_text_to_bool(sys.argv[5]), convert_text_to_bool(sys.argv[6]))
        elif len(sys.argv) == 8:
            create_password(int(sys.argv[2]), convert_text_to_bool(sys.argv[3]), convert_text_to_bool(sys.argv[4]), convert_text_to_bool(sys.argv[5]), convert_text_to_bool(sys.argv[6]), convert_text_to_bool(sys.argv[7]))
        else:
            print("Usage: flightdeck password [characters] [lowercase] [uppercase] [numbers] [symbols]")
        # except:
        #     print("Invalid input. Please give a valid input")
    elif command.startswith("weather"):
        if len(sys.argv) > 2:
            weather.get_weather(api_key.WEATHER_API_KEY, sys.argv[2])
        else:
            print("Usage: flightdeck weather [location]")

    else:
        print("Usage: python my_cli.py <command> [arguments]")