# Imporing OS for executing the Linux Commands 
import os
#importing getpass for echo back less authentication
import getpass

print("\n")

#-------------------------------------------Functions--------------------------------------------------

# Heading Display function
def Head(): 
	os.system("tput setaf 3")
	print("\t\t\tHey, Welcome! This is my TUI that makes Life Simple without memorizing the commands for RHEL8")
	os.system("tput setaf 3")
	print("\t\t\t---------------------------------------------------------------------------------------------")
	
#Username Password Auth Function
def Auth():
	passwd = getpass.getpass("Enter your Password :")
	apass = "redhat"
	if passwd != apass:
		print("\n")
		os.system("tput setaf 1")
		print("Incorrect Password! Try Again.....")
		Credits()
		exit()
  
  # Display the Options
def Task():
	os.system("tput setaf 4")
	print("""
	Press 1: To Check Date
	Press 2: To Check Calender
	Press 3: To Add User
	Press 4: To Configure Web_server
	Press 5: To configure SSH_Server
	Press 6: To Start Docker 
	Press 7: To Exit
	""")
