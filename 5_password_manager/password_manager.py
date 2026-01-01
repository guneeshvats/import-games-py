from cryptography.fernet import Fernet
# Here we are going to organise and store all the passwords in a txt file 
# we are going to encrypt the password and then one master password to decrypt all the paswords

# First we won't encrypt anything and then we'll do the encryption one 

master_pwd = input("What is the master password: ")

# key + password ---> is what we will use to encrypt and decrypt the passwords

def view(): 
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(" | ")
            print(f"User: {user} | Password: {pwd}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    # with keyword is used to open a file and it will automatically close the file after the block of code is executed
    # append mode is used to add new lines to the file - most flexible mode to use - we can write from the end of the file and not overwrite the existing data
    with open("passwords.txt", 'a') as f:
        f.write(name + " | " + pwd + "\n")

while True: 
    mode = input("Would you like to add a new password or view the existing ones (view, add, q): ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invaid mode")
        continue
