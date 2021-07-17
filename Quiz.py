print("You Have 5 chance\nIf exceeds it will be locked !!!")	
Password="1921u0030"
b=input("Password : ")	
c=5
while b!=Password and c>1:
	print("\nACCESS DENIED\nTry again\n")
	if c>2:
		print("You have ",c-1, "chance more")
	else:
		print("This is your last chance\nIf it is wrong it will be locked\nThink before you type☠")
	b=input("Password : ")
	c-=1
while b==Password:
	print("---ACCEPTED--- ")
	print("\n		###############")
	print("		### WELCOME ###")
	print("		###############\n")
	while True:
		print("1. First President of India\na.Pranab Mukerji	b.Dr. Rajendra Prasad \nc.Dr. Radhakrishnan	d.Javaharlal Nehru")
		a=input("Ans : ")
		if a=="a"or a=="b"or a=="c"or a=="d"or a=="A"or a=="B"or a=="C"or a=="D":
			print()
			if a=='b'or a=="B":
				print("\nRight answer\n")
			else:
				print("Wrong answer\n")	
		else:
			print("\nChoose a proper option\n")

	c-=1
			
