from random import seed
from random import randint
import time # I imported this to add the delays between functions

def level1():
	value = randint(0, 1) # used to make random values

	number1 = value
	number2 = value
	number3 = value
	codesum = number1+number2+number3
	codeproduct =number1*number2*number3 

	print("#  We have found out that the sysadmin's account name is Admin")
	print("#  And the pin adds up to",codesum)
	print("#  And it multiplies to make",codeproduct)
	print("#  Also, for security reasons, they make you enter the digit of the pin one at a time.\n\n")

	print(" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
	print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
	print("| | ____    ____ | || |      __      | || |     ______   | || |  _______     | || |     ____     | || | _____  _____ | || |      __      | || |  _______     | || |  _________   | |")
	print("| ||_   \\  /   _|| || |     /  \\     | || |   .' ___  |  | || | |_   __ \\    | || |   .'    `.   | || ||_   _||_   _|| || |     /  \\     | || | |_   __ \\    | || | |_   ___  |  | |")
	print("| |  |   \\/   |  | || |    / /\\ \\    | || |  / .'   \\_|  | || |   | |__) |   | || |  /  .--.  \\  | || |  | | /\\ | |  | || |    / /\\ \\    | || |   | |__) |   | || |   | |_  \\_|  | |")
	print("| |  | |\\  /| |  | || |   / ____ \\   | || |  | |         | || |   |  __ /    | || |  | |    | |  | || |  | |/  \\| |  | || |   / ____ \\   | || |   |  __ /    | || |   |  _|  _   | |")
	print("| | _| |_\\/_| |_ | || | _/ /    \\ \\_ | || |  \\ `.___.'\\  | || |  _| |  \\ \\_  | || |  \\  `--'  /  | || |  |   /\\   |  | || | _/ /    \\ \\_ | || |  _| |  \\ \\_  | || |  _| |___/ |  | |")
	print("| ||_____||_____|| || ||____|  |____|| || |   `._____.'  | || | |____| |___| | || |   `.____.'   | || |  |__/  \\__|  | || ||____|  |____|| || | |____| |___| | || | |_________|  | |")
	print("| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
	print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
	print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' \n")
	print("Username: Admin")
	firstdigit = int(input("Pin: "))

	# The condition is that if the player enters the first digit correctly, then the player can continue to second number and this is same for the rest of the if statements. If the player gets a single digit the code wrong, they get arrested and fired by the FCA and it would be game over for the player.
	if firstdigit == number1:
		print("Well done! You got the first digit correct\n")
		seconddigit = int(input("Second Digit: "))

		if seconddigit == number2:
			print("Good, now, what is the third digit?\n")
			thirddigit = int(input("3rd digit: "))
			if thirddigit == number3:
				print("Logged in successfully")
				print("Hello Administrator.\n")
				import lvl2
			else:
				import end1		
		
		else:
			import end1
			
	# Game over for player if the player couldn't pass the first level
	else:
		import end1
		
level1()
