import sys
import os
import time
import getpass
import briefing2

print(" __  __                      __  __       _ _") 
print("|  \\/  |                    |  \\/  |     (_) |")
print("| \\  / | __ _  ___ _ __ ___ | \\  / | __ _ _| |")
print("| |\\/| |/ _` |/ __| '__/ _ \\| |\\/| |/ _` | | |")
print("| |  | | (_| | (__| | | (_) | |  | | (_| | | |")
print("|_|  |_|\\__,_|\\___|_|  \\___/|_|  |_|\\__,_|_|_|\n")

email=input("email: ")
password=getpass.getpass()

if email == "BMorrison@Macroware.com" and password == "BobMorrisonMacroware245":
	print("To prove that this is really you, a verification code will be sent to your phone.")
	time.sleep(3)
	print("You: Oh shit!")
	time.sleep(3)
	print("You: that wasn't supposed to happen!")
	time.sleep(3)
	print("You: If this happens, then I will be arrested by the police.")
	time.sleep(3)
	print("You: Oh wait, I know what to do.\n")
	time.sleep(3)
	
	while(True):
		vercode=input("Verification code: ")
		if vercode == "ExterCMD":
			while(True):
				command=input("FCA@EXTERMINAT0R:$ ")
				print("")
				if command == "help":
					print("vercode: shows any verification code for any website")
					print("help: gives you help and tells you what the commands do")
					print("location: shows the current directory that you are in")
					print("rm32: removes system files on all computers connected to a network (Entered as verification code)")
					print("creator: gives the name of the game developer")
					print("exit: exites the command line\n")
								                       
				elif command == "vercode":
					print("The verification code for 'BMorrison@Macroware.com' is: 46Y2XY3\n")
						
				elif command == "location":
					print("This command doesn't work at the moment\n")

				elif command == "creator":
					print("The creator's name is: Fahad\n")

				elif command == "exit":
					break
				
				else:
					print("The command you entered", command,"isn't recognized by the terminal")
					print("If you need help with using the terminal, enter the command 'help'")
	

		elif vercode == "46Y2XY3":
			import lvl3		
			
		elif vercode == "rm32":
			import end2
			break

		elif vercode == "":
			print("Please enter your verification code\n")
		
		else:
			print("You have entered the wrong verification code\n")

else:
	print("You've entered the wrong email or password")
