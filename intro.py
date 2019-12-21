import getpass # I imported this so that I can hide the input of the player when he enters a password

def intro():
	print("") # I put that there so that the game could be seperated from the Linux terminal
	username = input("Username: ")
	password = getpass.getpass() # Players can enter anything for the password
	print("\nWelcome to Cracker-02!\n")

	print("Email\n")
	print("To:", username)
	print("From: C0mpUt3r_CrAck3r\n")
	print("There is another trouble that disturbs us.")
	print("And we need your help again!")
	print("We may have defeated the directors but once you defeat one evil, another one rises.")
	print("This particular company is called Macroware and they breach people's privacy through")
	print("making smart devices and they collect people's data and Macroware sells that data to advertisers")
	print("And we believe that some of the business practices of Macroware is wrong and unethical and could harm people.")
	print("Also, the CEO of the company Bob Morrison should also be stopped.")
	print("Which is why we here at FCA have recruited you again since you have helped defeat the directors.")
	print("Alas, 'The Exterminat0r' isn't able to help us this time. It just doesn't work with Macroware security systems.")
	print("Okay, enough talk, the world is depending on us.")
	print("Here are the details:\n")
intro()
