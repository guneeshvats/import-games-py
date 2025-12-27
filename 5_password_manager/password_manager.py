# Here we are going to organise and store all the passwords in a txt file 
# we are going to encrypt the password and then one master password to decrypt all the paswords

# First we won't encrypt anything and then we'll do the encryption one 

pwd = input("What is the master password: ")

mode = input("Would you like to add a new password or view the existing ones (view, add): ")

if mode == "view":
    pass
elif mode == "add":
    pass
else:
    print("Invaid mode")
