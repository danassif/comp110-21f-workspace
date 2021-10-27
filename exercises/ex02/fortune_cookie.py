"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
awesome: str = "You are so so awesome!"
joy: str = "You will have much joy in your life"
lottery: str = "You should play the lottery soon ;)"
friend: str = "You will find a new friend soon"
number: int = randint(1, 4)
print("Your fortune cookie says...")
if number == 1:
    print(awesome)
else:
    if number == 2:
        print(joy)
    else:
        if number == 3:
            print(lottery)
        else:
            print(friend)
print("Now, go spread some positive vibes!")