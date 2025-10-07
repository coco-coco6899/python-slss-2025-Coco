# McDoBot
# Author: Coco
# Oct 6, 2025
#
# Your Turn - McDoBot
# Write a McDonald's bot that asks if you want fries with your meal.
# Call it  work-mcdobot.py .
# It should accept  Yes/yes  or  No/no  as inputs, and reply
# appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.

fries = input("Do you want fries with your meals? (Yes/No)")
if fries.lower().strip() == "yes":
    print("Here's your meal with fries!")
elif fries.lower().strip() == "no":
    print("Here's your meal without fries!")
else:
    print("Sorry. I don't understand.")
