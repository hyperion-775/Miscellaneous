from random import randint
from math import log
from math import floor
max_number = 10
target = randint(1,max_number)
max_guesses = floor(log(max_number, 2)) + 1
guessed = False
counter = 0
low = 1
high = max_number
while not guessed:
  guess = int(input('What is your guess (' + str(low) + ' - ' + str(high)+ ')? '))
  counter = counter + 1
  if guess == target:
    print("Correct!, It took you " +str(counter) + " guesses.")
    guessed = True
  elif guess < target:
    print("Your guess is tooooooooooooooooooo low")
    low = guess + 1
  elif guess > target:
    print("Your guess is tooooooooooooooooooo high")  
    high = guess - 1
#  else: 
#    print("No, try again")
