'''Program to make a game named ROCK  PAPER  SCISSOR which follows the following general rules:
1 - Rock can destroy the Scissor
2- Scissor can cut the Paper
3- Paper can wrap the Rock'''

#<<<Importing the relevant libraries
import time
import random

#Printing the first user display
print("\t\t\t\tWelcome to the Rock Paper Scissor game")
print("\t\t\t\t------------------------------------------------------------------")
print("\t\t\t\t\tMenu")
print("\t\t\tPress play if you want to play Rock Paper Scissor ")
#Starting time when game starts
start_time = time.time()
#Demanding choice from user to start game
choice_for_game = input("Enter choice to play: ").lower()
if choice_for_game == "play":
    
    # Initializing value if user wants to try again i.e. Sentinel loop
    ch = "Y"
    while ch == "Y":
        
        
        
        #Input from program and user through random and own choice respectively
        program_input = random.randrange(0, 3)
        user_input = int(input("Press 0 for rock, 1 for scissors, and 2 for paper: "))
        
        #Condition if both values are same
        if user_input == program_input:
            print(f"You choose {user_input} Computer choose {program_input} but Match is drawn! Better luck next time :|")
        
        #All conditions for user to win game
        elif (user_input == 0 and program_input == 1) or (user_input == 1 and program_input == 2) or (user_input == 2 and program_input == 0):
            print(f"You choose {user_input} Computer choose {program_input} but Awesome! You won :)")
            
        #Condition if user enters choice out or range
        elif (user_input < 0) or (user_input > 2):
            print("Invalid choice! Please choose between 0 -- 2")
            
        #All conditions regardless of mentioned above user will loose
        else:
            print(f"You choose {user_input} Computer choose {program_input} but Oh no! Computer won :(")
        #Asking user if he/she wants to continue or exit
        ch = input("If you want to try again press Y or press any other key to exit: ").upper()        
        
            
        
else:
    print("Invalid Choice")
#Ending time out of loop tom calculate time for whole game not for single iteration
end_time = time.time()
endtime = int(end_time - start_time)


print(f"You took {endtime} seconds")
print("Game Ends! See you soon ;)")
#Game Ends >>>