try:
  x = int(input('How far would you like to travel in miles?\n'))
except:
  print('Try again.')
if x <= 3:
 print('I suggest walking to your destination.')
elif 3 < x < 300:
  print('I suggest driving to your destination.')
elif x >= 300:
  print('I suggest flying to your destination.')
def noun_input():
  input()
