import getpass

original_pin = 5252
# supplied_pin = input("Enter your PIN: ")
attempts = 3
count = 0

while count < attempts:
    supplied_pin = getpass.getpass(prompt="Enter your PIN: ")
    if original_pin == int(supplied_pin):
        print("Access Granted!")
        break
    else:
        count += 1
        if attempts - count == 0:
            print("Access Denied.")
            break
        print("Incorrect pin entered. You have" + " " + str(attempts - count) + " attempts left.")




