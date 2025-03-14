import PyAesCrypt
import os
import getpass
import sys
import string
import pyperclip

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024


WORDS = ["apple", "tiger", "ocean", "planet", "rocket", "guitar", "silver", "forest", "sunset", "mountain"]

def create_password(characters=14, readable=False):
    """Generate a password"""
    if readable:
        num_words = max(2, characters // 6)
        password = "-".join(random.choices(WORDS, k=num_words)).capitalize()
        password += str(random.randint(10, 99))  # Add numbers
    else:
        pool = string.ascii_letters + string.digits + "!@#$%^&*()_-+=<>?/"
        password = "".join(random.choices(pool, k=characters))
    return password

def 