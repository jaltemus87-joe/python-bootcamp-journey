# Day 5 - Password Generator - My Version

import random

# Lists of characters I can choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Ask user how many of each they want
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create a list and add the random characters
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Mix up the password so it's stronger
random.shuffle(password_list)

# Turn the list back into a string
password = ""
for char in password_list:
    password += char

print(f"\nYour password is: {password}")


# === My Personal Notes ===
# This was one of the most satisfying projects so far because I could actually see something useful come out of it.
# 
# What was hard at first:
# Understanding how to build the password piece by piece and then shuffle it.
# 
# What finally clicked:
# Using a list to collect everything first, then shuffling it, made way more sense than trying to build the string directly.
# 
# What I changed from the course version:
# - Removed the Easy Level code to keep the file cleaner
# - Used a simpler loop style with `_` since I didn't need the loop variable
# - Added a blank line before showing the final password to make it look nicer
