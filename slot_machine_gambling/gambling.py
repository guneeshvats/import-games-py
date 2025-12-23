# Text based slot machine game 

import random
import numpy as np


MAX_LINES = 3   # did it in caps because it is a constant vaulue and we are not going to change it later on
MAX_BET = 100 # max amount of money that can be bet on each line
MIN_BET = 1 # min amount of money that can be bet on each line

# Responsible for collecting user input that get the deposit from user for the game 
def deposit():
    while True: 
        amount = input("What would you like to deposit? $")
        # Checking if the user input is a valid whole number or not (only for whole numbers not integers)  because we dont want to accept any other input like decimals or strings or negative numbers
        if amount.isdigit():    
            amount = int(amount)
            if(amount > 0):      
                break # if the user input is a valid whole number and greater than zero then we break out of the loop
            else:
                print("Amount must be greater than zero!") 
        else:
            print("Enter a valid number...  $")
    return amount


def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():    
            lines = int(lines)
            if(1 <= lines <= MAX_LINES):      
                break 
            else:
                print("Enter a valid number of lines!") 
        else:
            print("Enter a valid number...")
    return lines


def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():    
            amount = int(amount)
            if(MIN_BET <= amount <= MAX_BET):      
                break 
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}!") 
        else:
            print("Enter a valid number...")
    return amount

# we are putting it in the main function because if we end our programme we can run it all again saying do you want to play again. 
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet. Your balance is ${balance}")
            continue
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${bet * lines}")

main()
