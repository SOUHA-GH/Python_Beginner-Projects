import random
import math
lower = int(input("Enter Lower limit:- "))
upper = int(input("Enter Upper limit:- "))
x = random.randint(lower, upper)
print("\n\tYou only have ",round(math.log(upper - lower + 1, 2))," chances to guess the integer! Good luck.\n")
count = 0
while count < math.log(upper - lower + 1, 2):
	count += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
	    if count == 1:
	        print("Congrats you did it in ",count, " try")	    
	    else:
	        print("Congrats you did it in ",count, " tries")
	        break
	elif x > guess:
		print("Wrong! You guessed too small!")
	elif x < guess:
		print("Wrong! You Guessed too high!")
if count >= math.log(upper - lower + 1, 2):
	print("\nOoups it's not that too, The number is %d" % x)
	print("\tBetter Luck Next time!")
