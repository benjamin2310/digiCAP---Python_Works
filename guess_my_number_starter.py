#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This program checks if a user's guess of a number matches that which is guessed by the computer, it uses the random module

import random

def welcomeMessage():
    print("Hello there!, Welcome to the game of guessing\n")
    print("I am thinking of a number between 1 and 99")

welcomeMessage()

while True:
    
#Accepting user inputs
    guessNumber = input("Please enter your guess between 1 and 99: ")
    guess = int(guessNumber)
    
#This code tells the computer to give out random numbers between 1 and 99. It is assigned to the variable randomNumber, it keeps checking till the condition is met. 
    randomNumber = random.randint(1, 99)
    if guess > randomNumber:
        print("Your guess is too high, try again\n")
        
    elif guess < randomNumber:
        print("Oops! your guess is too low, try again\n")

    elif guess == randomNumber:
        print("Congrats! That was the number\n")
        
#Stopping the loop we use the break function
        break

print("Thank you for taking this challange, see you next time.")


# In[ ]:




