import colorama
from colorama import Fore, Back, Style
import getpass
import socket

hostname = socket.gethostname()
username = getpass.getuser()

colorama.init(autoreset=True)

vault_entry = True
unlocked = False

if vault_entry:
    print("✈ Welcome to the FlightDeck Vault!")
    print("Commands: help, exit, add, list, path")

while vault_entry:
    command = input(f"{Fore.BLUE}{"🔒" if not unlocked else "🔑"} FlightDeck Vault{Fore.RESET} {Fore.GREEN}{username} at {hostname} {Fore.BLUE}✈{Fore.RESET}  ")
    if command == "exit":
        vault_entry = False
        print("🔒 Vault will be automatically locked as you leave. See you soon!")