# Day 2 - Tip Calculator - My Version

print("Welcome to the tip calculator!\n")

# Get inputs from user
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculate the tip and total
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount

# Split the bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_amount}")


# === My Personal Notes ===
# This one was tricky at first because there were so many steps (converting types,
# calculating percentages, rounding, etc.).
#
# What finally clicked: Breaking it down into small parts — first get the inputs,
# then do the math step by step.
#
# What I changed from the course version:
# - Added a newline after the welcome message to make it look cleaner
# - Used better variable name "tip_as_percentage" (easier for me to understand)
# - Used an f-string in the final print statement
