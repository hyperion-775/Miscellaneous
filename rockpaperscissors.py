import random
import sys
from sys import exit
icon = ["Rock","Paper","Scissors"]
userInput = ""
userChoice = ""
winScore = 0
loseScore = 0
drawScore = 0
i = 0
winner = ""

print("Type 'stop' to end the game.")

while i<1 :
  randomNumber = random.randint(0, len(icon)-1)
  computerChoice = (icon[randomNumber])
  
  userInput = input("Rock, paper, or scissors? ")
  userChoice = userInput.lower()
  
  if userChoice == "rock":
    if computerChoice == "Rock":
      winner = "Draw"
    elif computerChoice == "Scissors":
      winner = "Player"
    elif computerChoice == "Paper":
      winner = "Computer"
  elif userChoice == "paper":
    if computerChoice == "Rock":
       winner = "Player"
    elif computerChoice == "Scissors":
      winner = "Computer"
    elif computerChoice == "Paper":
      winner = "Draw"
  elif userChoice == "scissors":
    if computerChoice == "Rock":
      winner = "Computer"
    elif computerChoice == "Scissors":
      winner = "Draw"
    elif computerChoice == "Paper":
      winner = "Player"
  elif userChoice == "stop":
    i= i +1
    print("Game over!")
    sys.exit()
  else:
    print("Uh oh! Check your spelling.")

  if winner == "Player":
    print("The computer chose " + computerChoice)
    print("Congrats! You won!")
    print("You have " + str(winScore) + " wins, "+ str(loseScore) + " losses, and " + str(drawScore) + " draws.")
    winScore = winScore + 1
  elif winner == "Computer":
    print("The computer chose " + computerChoice)
    print("You lost :(")
    print("You have " + str(winScore) + " wins, "+ str(loseScore) + " losses, and " + str(drawScore) + " draws.")
    loseScore = loseScore + 1
  elif winner == "Draw":
    print("The computer chose " + computerChoice)
    print("That was a draw, try again.")
    print("You have " + str(winScore) + " wins, "+ str(loseScore) + " losses, and " + str(drawScore) + " draws.")
    drawScore = drawScore + 1


x = input("")
if x == "resume":
  i=0
