import colorama
from colorama import Fore, Back, Style
import getpass
import socket
import os
import pyAesCrypt
import platform
from pathlib import Path
from getpass import getpass

BUFFER_SIZE = 64 * 1024

hostname = socket.gethostname()
username = getpass.getuser()

vault_entry = True
unlocked = False

def vault_location(os):
    if os == "Windows":
        path = f"C:/Users/{username}/Documents/FlightDeckVault"
    elif os == "Linux":
        path = f"/home/{username}/Documents/FlightDeckVault"
    elif os == "Darwin":
        path = f"/Users/{username}/Documents/FlightDeckVault"
    return path

# Enccryption/Decryption
def encrypt_file(file_path, password):
    encrypted_path = file_path + ".fdei"
    pyAesCrypt.encryptFile(file_path, encrypted_path, password, BUFFER_SIZE)
    os.remove(file_path)

def encrypt_folder(folder_path, password):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, password)
    print(f"Folder '{folder_path}' encrypted successfully.")

class DecryptionError(Exception):
    pass

def decrypt_file(encrypted_file_path, password):
    original_file_path = encrypted_file_path[:-5] 
    try:
        pyAesCrypt.decryptFile(encrypted_file_path, original_file_path, password, BUFFER_SIZE)
        os.remove(encrypted_file_path)
        print(f"Decrypted: {original_file_path}")
    except Exception:
        raise DecryptionError(f"Failed to decrypt {encrypted_file_path}: Wrong password or corrupted file.")

def decrypt_folder(folder_path, password):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".fdei"): 
                encrypted_file_path = os.path.join(root, file)
                decrypt_file(encrypted_file_path, password) 
    print(f"Decryption process completed for '{folder_path}'.")


# New guy setup
def first_entry():
    global unlocked
    print("✈ Welcome to the FlightDeck Vault!")
    print("Since this is your first time, we'll need to set up your vault.")
    os = platform.system()
    if os == "Windows":
        path = Path(f"C:/Users/{username}/Documents/FlightDeckVault")
        path.mkdir(parents=True, exist_ok=True)
    elif os == "Linux":
        path = Path(f"/home/{username}/Documents/FlightDeckVault")
        path.mkdir(parents=True, exist_ok=True)
    elif os == "Darwin":
        path = Path(f"/Users/{username}/Documents/FlightDeckVault")
        path.mkdir(parents=True, exist_ok=True)

    print(f"Vault created at {path}!")
    print("In case you ever forget this, you can use the 'path' command to see where your vault is located.")

    unlocked = True

def main_loop():
    colorama.init(autoreset=True)

    if vault_entry:
        print("✈ Welcome to the FlightDeck Vault!")
        print("Please start by unencrypting your vault.")

        verifying_password = True
        first_attempt = True
        new_vault = False
        while verifying_password:
            password = getpass("Enter your password: ")

            if not first_attempt and password == "HELP IT MOVED":
                print("Let's get a new vault")
                new_vault = True
                break

            path = vault_location(platform.system())
            try:
                decrypt_folder(path, password)
                unlocked = True
                verifying_password = False
                print("Vault unlocked!")
            except DecryptionError:
                print("Failed to decrypt. Please enter a valid password or ensure that your vault has not been moved/deleted. If it has moved/deleted, enter the \"HELP IT MOVED\" in the next prompt to create a new one")
            
            first_attempt = False

        if new_vault:
            first_entry()

        print("Commands: help, exit, add, list, path")

        help = f"""Welcome to the FlightDeck Secure Vault!
        Current vault status: {"🔒" if not unlocked else "🔑"}

        Commands:
        help   - show this help message
        exit   - exit the vault
        add    - add a new note to your vault
        list   - list all notes in your vault
        path   - show the current path to your vault
        rm     - remove a note from your vault
        """

        while vault_entry:
            command = input(f"{Fore.BLUE}{"🔒" if not unlocked else "🔑"} FlightDeck Vault{Fore.RESET} {Fore.GREEN}{username} at {hostname} {Fore.BLUE}✈{Fore.RESET}  ")
            if command == "exit":
                vault_entry = False
                print("🔒 Lock your vault before you go!")
                verifying_password = True
                while verifying_password:
                    password = getpass("Enter a password:")
                    confirm_password = getpass("Enter again to confirm")
                    if password == confirm_password:
                        verifying_password = False
                    else:
                        print("Passwords do not match. Try again.")

                path = vault_location(platform.system())
                encrypt_folder(path, password)
                print("Vault locked. Do not forget your password else you will lose access to your vault!")
                print("See you soon!")
            
            elif command == "help":
                print(help)
            
            else:
                print("Invalid command. Type 'help' to see available commands.")