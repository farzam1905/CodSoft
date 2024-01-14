from random import *
import string

users_choice = "Y"
while users_choice == "Y":
    print("\t\t\t\t \t    Welcome to the Password Generator")
    # Promting user to enter deisred length of password
    user_input = input("Enter the length of password:\n")
    
    #Checking if user has entered correct length or not
    if user_input.isdigit():
        # Concatenating Random Characters
        characters = string.digits + string.ascii_letters + string.punctuation

        # Including numbers in password
        final_pass = str(randrange(1, 1001))

        # Applying loop to check that length of randomly generated password is less than or equal to user input or not
        while len(final_pass) < int(user_input):
            final_pass += choice(characters)  # Adding random characters to final pass until it meets desired length

        # Printing the final pasword generated
        print(f'Your Password is {final_pass}')
        
    #Program will show error if user input is incorrect
    else:
        print("ERROR! Enter the length correctly")
    
    users_choice = input("Do you want to try again? Press Y , else press any key to exit:\n").upper()
print("\t\t\t\t\t\t\t\t\t\t\t  Thanks for using this program :)")

