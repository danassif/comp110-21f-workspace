"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730243388"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
<<<<<<< HEAD
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
=======

rand_int: int = randint(0, 3)
print("Your fortune cookie says...")
if (rand_int == 0):
    print("you will get married")
elif (rand_int == 1):
    print("you should take a nap")
elif (rand_int == 2):
    print("you need therapy")
else:
    print("you will meet a new friend tommorow")
print("Now, go spread positive vibes!")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
