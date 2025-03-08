import sys
import files.files
from colorama import Fore, Style
import colorama

colorama.init(autoreset=True)

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "help":
        with open("help.txt") as f:
            print(f.read())
    
    # Files
    elif command == "open" and len(sys.argv) > 2:
        print("Reading file...")
        files.files.read_file(sys.argv[2])
    elif command == "open" and len(sys.argv) < 2:
        print(Fore.RED + "⚠ Error: No file provided")
        print("Usage: flightdeck open [file]")

    # Solstice
    else:
        print(f"Unknown command: {command}")
else:
    print("Usage: python my_cli.py <command> [arguments]")