import sys
from .files import handler
from colorama import Fore, Style
import colorama
import flightdeck.file_path as file_path
from .timer import pomodoro
import flightdeck.vault as vault
import random
import string
import flightdeck.weather as weather
import flightdeck.apikey as apikey
from flightdeck.passwords import create_password

WORDS = ["apple", "tiger", "ocean", "planet", "rocket", "guitar", "silver", "forest", "sunset", "mountain"]

help = """flightdeck v1.0-testing {}
✈ usage: flightdeck [commands] [options | file (if command requires)] ...

flightdeck is a versatile utility that allows you to do many things. it adds
functionality like never before to your terminal. here are the options:

commands:
open [file]        - view an image or markdown file using the commandline.
solstice           - open Solstice for the commandline, a pomodoro tracker
weather [location] - get weather forecast for your country, country in ISO 3166 alpha 2 format
secure-vault       - enter the secure vault and view your notes and other secret stuff...
password [options] - manage your password stuff
"""

def convert_text_to_bool(text):
    if text.lower() == "true":
        return True
    elif text.lower() == "false":
        return False
    else:
        raise ValueError("Invalid input.")

def main_loop():
    colorama.init(autoreset=True)

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "help":
            print(help)
        
        # Files
        elif command == "open" and len(sys.argv) > 2:
            print("Reading file...")
            handler.read_file(file_path.get_full_path(sys.argv[2]))
        elif command == "open" and len(sys.argv) < 2:
            print(Fore.RED + "⚠ Error: No file provided")
            print("Usage: flightdeck open [file]")

        # Solstice
        elif command == "solstice":
            print("Opening Solstice...")
            try:
                if len(sys.argv) == 3:
                    if sys.argv[2].isdigit():
                        pomodoro.start_timer(work_time=int(sys.argv[2]))
                    elif sys.argv[2] == "help":
                        print("Usage: flightdeck solstice [work_time] [break_time]")
                elif len(sys.argv) == 4:
                    pomodoro.start_timer(work_time=int(sys.argv[2]), break_time=int(sys.argv[3]))
                elif len(sys.argv) == 2:
                    pomodoro.start_timer()
            except:
                print(Fore.RED + "Error: Failed to launch Solstice" + Style.RESET_ALL)
                print("Usage: flightdeck solstice [work_time] [break_time]")
                if sys.platform == "win32":
                    print("HINT: Check if windows-curses is installed")

        # FlightDeck Vault
        elif command == "secure-vault":
            vault.main_loop()

        elif command.startswith("password"):
            if len(sys.argv) == 2 and sys.argv[1] == "help":
                print("Usage: flightdeck password [characters] [lowercase] [uppercase] [numbers] [symbols]")
                print("Default: flightdeck password 16 true true true true false")
            try:
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
            except:
                print("Invalid input. Please give a valid input")
        elif command.startswith("weather"):
            if len(sys.argv) > 2:
                weather.get_weather(apikey.WEATHER_API_KEY, sys.argv[2])
            else:
                print("Usage: flightdeck weather [location]")

        else:
            print("Invalid command!")
            print("Usage: python my_cli.py <command> [arguments]")
            print("Check flightdeck help for more info")

    else:
        print("FlightDeck v1.0.0")
        print("Please add a command to test")