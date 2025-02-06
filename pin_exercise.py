password = "1234"
# The correct PIN code is stored as a string in the variable password.

max_attempts = 3
attempt = 1

# The input function prompts the user to give a password and stores it as a string in the supplied_pin variable
supplied_pin = input("Enter your PIN: ")

# Use a while loop to prompt the user for input while the number of attempts is less than or equal to 3
while attempt <= max_attempts:
    if supplied_pin == password:
        print("Correct password!")
        break  # Exit loop if correct PIN is entered

    # If incorrect PIN and attempts are remaining
    if max_attempts>attempt:
        print(f"Wrong password. Please try again.")
        print(f"Attempt {attempt} out of {max_attempts}")
        attempt += 1
        supplied_pin = input("Enter your PIN: ")
    else:
        print(f"Attempt {attempt} out of {max_attempts}. You are locked out!")
        break

