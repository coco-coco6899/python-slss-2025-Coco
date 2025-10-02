# Choose Your Own Adventure
# Author: Alicia Tong
# 24 September 2025

# Choose your own adventure story focusing on using variables and branching/conditions.

import time
import os
import functions


# Intro
print("Hello everyone! Welcome to Time Travel 1.0!")
time.sleep(1.0)
name1 = input("Before we start, please enter you name.").strip("!?,.")
print(f"Welcome {name1}!")
time.sleep(1.0)
print("Now, lets get started!")
time.sleep(2.0)
os.system("clear")


# Rising
print(
    "You are chatting with your bestie, Alex, and you learn that he just invented a new time travel machine...\n"
)
time.sleep(2.0)
print(f"{name1}: Hi Alex, long time no see, what are you working on now?")
time.sleep(2.0)
print(
    "Alex: Oh hi! I just invented a time travelling machiene! I am pretty pround of myself!"
)
time.sleep(2.0)
print(f"{name1}: Wow, that is impressive!!")
time.sleep(1.0)
print("Alex: YESS! Do you want to come try out this lovely machiene?")
time.sleep(2.0)
ans1 = (
    input("Please type you answer here, if yes type yes, if no type no")
    .strip("?!,.")
    .lower()
)
os.system("clear")


counter = 0
while counter != 100:
    if ans1 == "yes":
        functions.choiceOfDestination()
        break
    elif ans1 == "no":
        functions.goHome()
        break
    else:
        counter += 1
        ans1 = (
            input("Please type you answer here, if yes type yes, if no type no")
            .strip("?!,.")
            .lower()
        )
