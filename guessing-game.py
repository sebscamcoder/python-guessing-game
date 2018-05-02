from random import *

computerNumber = randint(1,10)
print "The correct numbner is: " + str(computerNumber) + ". This is for debugging purposes only -DELETE"

playerGuess = raw_input("I have a number 1-10. Whats the number? ")

if int(playerGuess) == computerNumber:
    print ("Correct!")
    
if int(playerGuess) != computerNumber:
    print ("WRONGGGGGGGG!!!")
    
# TODO Tell the user to guess higher or lower
# TODO Keep asking until the answer is correct

# BONUS TODO write using a while statement & then rewrite using a for loop
