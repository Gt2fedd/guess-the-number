#Shariyf, Delroy, Gerald
# Many aspects of your code work well.
# The most basic functonality is there across multiple 
# rounds.
# Missing Features:
#
# 1. You should have limited the number of guesses.
# 2. You sould track the guesses already made by the user.

# I am also concerned that there may be an uneven level
# of work and understanding here. Did you all 
# participate as equals? Or was one of you doing the 
# majority? Do you all understand how the code works?

import random

guess = -100
play_again = True


while play_again:
  cpu_number = random.randint (0,100)
  print(cpu_number)
  while guess != cpu_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess != cpu_number:
      print("Wrong")
    if guess > cpu_number:
      print("You guessed too high")
    elif guess < cpu_number:
      print("You guessed too low")

  print("Correct")  

  if guess == cpu_number:
    print("Would you like to play again?")
    print("Enter 1 for yes")
    print("Enter 2 for no")
    play_again = int(input())
    if play_again == 1:
      play_again = True
    elif play_again == 2:
      play_again = False

