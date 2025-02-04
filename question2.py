import getpass

#HARDCODED PIN
correct_PIN = '4567'

max_attempts = 3
attempts = 0

#loop for the pin
#while the attempts is less than 3, users can input their pin
while attempts < max_attempts:
    supplied_pin = getpass.getpass(prompt="Please enter your PIN: ")
    if supplied_pin == correct_PIN:
      print(f"Correct PIN in {attempts + 1} attempt")
      break

    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left")

#
if attempts == max_attempts:
    print("ACCESS DENIED")

