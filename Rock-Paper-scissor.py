# import random module 
import random 
import os
import time


#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#Rules for the game
print("The Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n") 


time.sleep(5)

#While statement for playing the game till user says to end the game
while True: 
    
	print("Your Choices are: \n 1. Rock \n 2. paper \n 3. scissor \n") 
	
	#If user enters an input other than 1 or 2 or 3 then Invalid input will be printed
	try:
		# take the input from user 
		choice = int(input("What do you choose: ")) 

	except ValueError:
		
		print("Invalid Input")
		continue

	# looping until user enter invalid input 
	while choice > 3 or choice < 1: 
		choice = int(input("Please Enter valid input: ")) 
		

	# initializing value of choice_name variable and corresponding to the choice value 
	if choice == 1: 
		choice_name = 'Rock'
	elif choice == 2: 
		choice_name = 'paper'
	else: 
		choice_name = 'scissor'
		
	# print user choice 
	print("User's choice is: " + choice_name) 
	print("\nNow it's computer's turn.......") 

	# Computer chooses randomly any number among 1 , 2 and 3. Using randint method of random module 
	comp_choice = random.randint(1, 3) 
	
	# looping until comp_choice value is equal to the choice value 
	while comp_choice == choice: 
		comp_choice = random.randint(1, 3) 

	# initializing value of comp_choice_name variable corresponding to the choice value 
	if comp_choice == 1: 
		comp_choice_name = 'Rock'
	elif comp_choice == 2: 
		comp_choice_name = 'paper'
	else: 
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name) 		#Printing computer's choice

	time.sleep(2)

	print(choice_name + " V/s " + comp_choice_name) 		#Printing computer's choice vs user's choice

	# conditions for winning 
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )): 
		print("paper wins => ", end = "") 
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)): 
		print("Rock wins ==>", end = "") 
		result = "Rock"
	else: 
		print("scissor wins ==>", end = "") 
		result = "scissor"

	time.sleep(2)

	# Printing either user or computer wins 
	if result == choice_name: 
		print("You Won! Congractulations...") 
	else: 
		print("Sorry Computer won...") 
	
	time.sleep(2)

	#Repeating statement if user wants to play again or not
	print("Do you want to play again? (Y/N)")
	ans = input() 

	time.sleep(2)
	
	#If user wants to play again
	if ans == 'y' or ans == 'Y':
		continue

	# if user inputs n or N then game ends
	if ans == 'n' or ans == 'N': 

		print("Ok! Thanks for playing.") 
		break
	
	#If user inputs value other than n or N then invalid input will be returned and game ends
	if ans != 'n' or ans != 'N':
			
		print("Sorry Invalid Input.\nPlease Try again later..")
		time.sleep(2)
		exit()


