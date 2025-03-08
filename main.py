import sys
from files import handler
from colorama import Fore, Style
import colorama
import file_path
import timer.pomodoro
import vault

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


else:
    print("Usage: python my_cli.py <command> [arguments]")