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
	
#Function Asking the Available Options from user to perform that task
def Asking_option():
	os.system("tput setaf 2")
	print("Enter Your Choice:", end="")
	ch=input()	
	print("\n")
	return ch

#Function with various options and their working for Local System call
def Options_local(ch):
		os.system("tput setaf 6")
		if int(ch)==1:
			os.system("date")

		elif int(ch)==2:
    			os.system("cal")

		elif int(ch)==3:
			print("Name of the User: ", end="")
			create_user=input()
			os.system("useradd {}".format(create_user))

		elif int(ch)==4:
    			os.system("")

		elif int(ch)==5:
    			os.system("")

		elif int(ch)==6:
    			os.system("systemctl start docker")

		elif int(ch)==7:
			Credits()
			exit()

		else:
    			print("Error! Option Not Supported")


#Functions for Credits
def Credits():
	os.system("tput setaf 11")
	print("\t\t\t\t\t\t\tMade By Gursimar Singh")
	print("\n")
	os.system("tput setaf 7")
	

#Function with various options and their working for Remote System call
def Options_remote(ch):
		os.system("tput setaf 6")
		if int(ch)==1:
			os.print("ssh {} date".format(ip_address))

		elif int(ch)==2:
			os.print("ssh {} cal".format(ip_address))

		elif int(ch)==3:
			print("Name of the User you want to Add: ", end="")
			create_user=input()
			os.print("ssh {} useradd {}".format(ip_address,create_user))

		elif int(ch)==4:
    			print("")	#Change print in all options to os.system when actually working with
					#two systems. I am doing as I am doing alone.
		elif int(ch)==5:
    			print("")

		elif int(ch)==6:
    			print("")

		elif int(ch)==7:
			Credits()
			exit()

		else:
    			print("Error! Option Not Supported")
