# Define the correct PIN as a hardcoded value
correct_pin = "2468"  # This is the correct PIN to be put by the user

# Set the maximum number of attempts allowed
max_attempts = 3

# Initialize the attempt counter
attempts = 0

# Loop to allow the user to enter the PIN, as long as it is less than the maximum number of attempts
while attempts < max_attempts:
    supplied_pin = input("Enter your pin: ")

    # Check if the entered PIN matches the correct PIN
    if supplied_pin == correct_pin:   #set the conditional statement
        # If the PIN is correct, print a success message
        print(f"Access granted! You entered the correct PIN in {attempts + 1} attempt(s).")
        break  # Exit the loop since the user succeeded
    else:
        # If the PIN entered is incorrect, increase the attempt counter
        attempts += 1
        remaining_attempts = max_attempts - attempts

        # If there are attempts left, inform the user
        if remaining_attempts > 0:
            print(f"Incorrect PIN. You have {remaining_attempts} attempt(s) remaining.")
        else:
            # If no attempts are left, print a failure message
            print("Oops! You have entered the wrong PIN too many times. Access denied.")
