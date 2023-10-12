#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random 

print("""Welcome to the number guessing game!!
Guess a number from 1 to 100.
Please choose a difficulty level:
1. Easy (10 guesses)
2. Hard (5 guesses)
""")

number = random.randint(1,100)

def dif_level(uc):
    if uc == "easy":
      return 10
    else:
      return 5

def guess(guess, number):
  if guess == number:
    return "correct"
  elif guess > number:
    return "lt"
  elif guess < number:
    return "gt"

user_choice = input("Choose the difficulty level: ")

turns = dif_level(user_choice)

def game(turns,number):
  while True:
    print(f"You have {turns} guesses remaining")
    gues = int(input("make a guess: "))
    decision = guess(gues, number)
    if decision == "correct":
      print("You Win!!!")
      break
    elif turns == 1:
      print("You Lose!!!")
      print(f"The number was : {number}")
      break
    elif decision == "lt":
      print("Guess Lower")
      turns-=1
    elif decision == "gt":
      print("Guess Higher")
      turns-=1
    
    
game(turns,number)
    
  


