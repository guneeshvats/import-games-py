import random 
# print(random.randrange(-1, 10)) # will randomly choose from -1 to 9 
# randint() will include the last one as well unline randrange()

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time...")
        quit()
else:
    print("Please type a number next time...")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True: # we can also do by doing while user_guess!= random_number
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time...")
        continue

    if user_guess == random_number:
        print("You got it right brother!...")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")
    # else:
    #     if user_guess > random_number:
    #         print("You were above the number")
    #     else: 
    #         print("You were below the number")

print("In", guesses, "guesses") # when we are using commas - it will automatically add space in between & here no need to even convert to string 


