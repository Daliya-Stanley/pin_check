#Passwords and PINs are normally hidden as you type. Add the functionality to hide the characters typed. Use the getpass.getpass module to help.

import sys
import getpass



correct_pin = "1234"
attempts = 0
attempts_allowed = 3
supplied_pin = None

while attempts < attempts_allowed:
        print("Attempt #", attempts + 1)
        supplied_pin = getpass.getpass(prompt = "Enter your PIN:", stream=None)

        if supplied_pin == correct_pin:
                print("Correct PIN entered. Welcome to your account.")
                break
        else:
                print("Incorrect PIN entered. Please try again.")
                attempts += 1
                if attempts == attempts_allowed:
                        print("Incorrect PIN entered too many times. Access denied. Please contact customer services.")
