from random import randrange
num = int(input("Enter a number within 0 and 10 " + "\n"))
t = randrange(10)
if (num<t): 
    print("Number was low")
    print("Random number was: ", t)
    print("Your guess was:", num, "\n")
elif (num>t): 
    print("Number was high")
    print("Random number was: ", t)
    print("Your guess was:", num, "\n")
else:
    print("Number was spot-on")
    print("Random number was: ", t)
    print("Your guess was:", num, "\n")