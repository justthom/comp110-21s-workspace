"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730336470"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune: int = randint(1,100)

if fortune < 40:
    if fortune < 20:
        print("You are going to move mountains!")
    else:
        print("Good things are coming your way!")
else:
    if fortune < 60:
        print("You shouldn't seek advice from fortune cookies.")
    if fortune > 80:
        print("The stars of riches are watching over you.")
    else:
        print("Life is a performance.")

print("Now, go spread positive vibes!")