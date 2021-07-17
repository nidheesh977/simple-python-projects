
Password="1921u0030"

while True:
	c=5
	print("\nSystem Locked Enter password")
	print("You Have 5 chance \nIf exceeds it will be locked !!!\n")
	b=input("Password : ")		
	while b!=Password and c>=1:
		print("\nACCESS DENIED\n")
		if c>2:
			print("You have ",c-1, "chance more\n")
			b=input("Password : ")
		elif c==2:
			print("This is your last chance\n☠Think before you type☠\n")
			b=input("Password : ")
		else:
			print("!!! System Locked !!!")
		c-=1
	if b==Password:
		print("\n---ACCEPTED--- ")
		
		print("\n		#####################")
		print("		### SYSTEM OPENED ###")
		print("		#####################\n")
	
		Password=input("Enter your new password : ")
