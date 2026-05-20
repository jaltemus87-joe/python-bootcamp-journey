# Day 4 - Rock Paper Scissors - My Version

import random

# My ASCII art for the choices
rock = '''
    _______
---'   ____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors!\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Show what the user picked
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
else:
    print("You typed an invalid number. You lose!")

# Computer picks
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Decide who wins
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice!")
elif user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")


# === My Personal Notes ===
# This was my first time using the random module and it felt really cool to play against the computer.
# 
# What was confusing at first:
# Remembering to use different conditions for winning.
# 
# What I changed from the course:
# - I reorganized the win conditions to be easier for me to read
# - Added clearer messages
