#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This program is able to generate simple addition problems that involve adding two 2-digit integers
(i.e., the numbers 10 through 99).
The user is asked for an answer to each problem.  This program determines if the answer was correct or not,
and give the user an appropriate message to let them know.
This program keeps giving the user problems until the user has gotten 3 problems correct in a row.
"""
import random


usr_correct_answer = 0
while usr_correct_answer <= 3:
    
    # generate first random number
    first_rand = random.randint(10, 99)
    
    # generate second random number
    second_rand = random.randint(10, 99)
    
    randomNumber = first_rand + second_rand
    
    # ask the question
    print("What is", first_rand, "+", str(second_rand) + '?')
  
    answer = int(input("Your answer: "))

    if answer == randomNumber:
        print("Correct!.You have gotten", usr_correct_answer, "in a row.\n")
        usr_correct_answer += 1

    else:
        print("Incorrect. The expected answer is", str(first_rand + second_rand))
        usr_correct_answer = 1

print("Congratulations!  You mastered addition.")

 


# In[ ]:




