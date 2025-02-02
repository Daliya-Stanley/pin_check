
# created a variable to define the correct pin
correct_pin = "4567"

# created a variable for maximum attempts which can be changed.
maximum_attempts = 3
# created a variable for the number of attempts
attempt = 0

# created a while loop which will run whilst the condition is true:
# whilst the number of attempts is less than the maximum attempts
# if maximum attempts are reached, this is when the condition is no longer true
# and the loop will stop
while attempt < maximum_attempts:

# input function given to be able to enter PIN
    supplied_pin = input("Please enter your PIN:")

# if statement used: if the supplied pin is equal to the correct PIN
# the console will print 'Correct PIN'.
    if supplied_pin == correct_pin:
        print("Correct PIN")

# a break has been added so that when the Correct Pin is entered
# the while loop will stop even when the number of attempts are less than
# the maximum attempts
        break

# an else statement is added for an incorrect PIN being entered
    else:

# the attempt variable has a value of 0. += will add 1 to the attempt variable.
        attempt += 1

# used an f-string to be able to embed expressions into the string.
# the message will show how many attempts are left by completing
# the subtraction of defined variables in {}
        print(f"Incorrect PIN. You have {maximum_attempts - attempt} attempts left")

# added an if statement for completion of attempts
# if the number of attempts are equal to the maximum attempts, the console will
# print 'ACCESS DENIED'.
if attempt == maximum_attempts:
    print("ACCESS DENIED")