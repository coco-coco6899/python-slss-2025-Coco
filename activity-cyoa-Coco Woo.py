# Choose your own adventure
# Coco Woo
# Sep 24, 2025

# Choose your own adventure story focusing on
# using vriables and branching/conitionals
#
#

import time
# time.sleep(1.5) unit is sec and type this if u wanna give time to read

# Introduction
# You and your friend Rachel decided to challenge the Grouse Grind mountain on this sunday afternoon.
# You and Rachel both think it's going to be easy hike so you both only backed a map, a bottle of water, and two sandwiches.

print("Welcome to little steps adventure.")
time.sleep(1.5)
user_name = input("Adventurer, What's your name?")
print(f"Nice to meet u, {user_name}!")
time.sleep(1)
print(
    "You and your friend Rachel decided to challenge the Grouse Grind mountain on this sunday afternoon."
)
time.sleep(1.5)
print(
    "You and Rachel both think it's going to be easy hike so you both only backed a map, a bottle of water, and two sandwiches."
)
time.sleep(2)
# Problem
# When you and Racehel start hiking. It's easy and so you both continues your way up.
# It's getting harder and harder and you both are getting tired(energy level down to 85%). Let them decide should they continue or take a break
print("When you and Racehel start hiking.")
time.sleep(1)
print("It's easy and so you both continues your way up.")
time.sleep(1.5)
print(
    "However, the trail is getting steeper and you both are getting tired(energy level down to 85%)."
)
time.sleep(2)
# problem 3
# After aother 30 minutes walk , you and Rachel are closer to the top.
# However, your energy level decreased 20% and the sky is getting darker.
# Your friend Rachel is super hungry.
# Option 1 : wanted to go back to the cave. ignore friend away
# Option 2&3 : find food and place no= food all eaten by Rachel yes = looked around and found some rabbits
# cature = food and no = food all eaten by Rachel


def player_choice5():
    # ans5 = input("Do you want to ")
    # def player_choice3():
    ans4 = input(
        "You and Rachel arrived a cave. Do you want to go into the cave to explore or no? ( Answer either yes or no)."
    )

    if ans4 == "yes":
        print("You and Rachel explored half an hour in the cave and found nothing.")
        time.sleep(1.5)
        print("Energy level decreased to 55% and continued your way up to the top.")
    else:
        print("You and Rachel continued your way to the top.")
        # def player_choice5()


def player_choice4():
    ans4 = input(
        "You and Rachel arrived a cave. Do you want to go into the cave to explore or no? ( Answer either yes or no)."
    )

    if ans4 == "yes":
        print("You and Rachel explored half an hour in the cave and found nothing.")
        time.sleep(1.5)
        print("Energy level decreased to 75% and continued your way up to the top.")

    elif ans4 == "no":
        print("You and Rachel continued your way to the top.")
    #   def player_choice6()


def player_choice1():
    ans2 = input(
        "After 30 minutes, there's three paths in front of you , which path do you pick? (Answer either right, middle, or left)."
    )
    if ans2 == "right":
        print("You decided to go to the right path.")
        time.sleep(1)
        print("You continue hiking and you and Rachel arrived a cave.")
        # player_choice3()
    elif ans2 == "middle":
        print("You decided to go to the middle path.")
        time.sleep(1)
        print(
            "You found some materials. +1 bottle of water & +1 energy bar & +1 flash light"
        )
        time.sleep(1)
        print("You and Rachel continued your way to the top.")
    #   def player_choice7()
    elif ans2 == "left":
        print("You decided to go to the left path.")
        time.sleep(1)
        print("You continue walking and nothing happened.")
        time.sleep(1.5)
        print("Energy level decreased down to 60%.")
        time.sleep(1)
        print("You continued your way to the top.")
    #  def player_choice8()


def player_choice2():
    ans3 = input(
        "After 30 minutes, there's three paths in front of you , which path do you pick? (Answer either right, middle, or left) "
    )
    if ans3 == "right":
        print("You decided to go to the right path.")
        time.sleep(1)
        print("You continue hiking and you and Rachel arrived a cave.")
        player_choice4()
    elif ans3 == "middle":
        print("You decided to go to the middle path.")
        time.sleep(1)
        print(
            "You found some materials. +1 bottle of water & +1 energy bar & +1 flash light"
        )
        time.sleep(1)
        print("You and Rachel continued your way up.")
    #  def player_choice(9)
    elif ans3 == "left":
        print("You decided to go to the left path.")
        time.sleep(1)
        print("You continue walking and nothing happened.")
        time.sleep(1.5)
        print("Energy level decreased down to 80%.")
        time.sleep(1)
        print("You continued your way up.")
    # def player_choice(10)


ans1 = input(
    "Do you want to take a break or continue the hike? (Ans either hike or rest)."
)

if ans1 == "hike":
    print(
        "You decide to hike and both your and her energy levels are decreased to 70%."
    )
    player_choice1()
elif ans1 == "rest":
    print("You decide to take a break and both energy levels are increased to 90%.")
    time.sleep(1)
    print("However, you used 1/3 of your water.")
    player_choice2()

print("After aother 30 minutes walk , you and Rachel are closer to the top.")
time.sleep(1.5)
print("However, your energy level decreased 20% and the sky is getting darker.")
time.sleep(1.5)
print("Your friend Rachel is super hungry.")
print(">")


# problem 2
# You both continue your hike towards the top.
# After 30 minutes, there's three paths in front of you , which path do you pick?
# time.sleep(1.5)
# print("You both continue your hike towards the top.")
# time.sleep(1.5)

# problem 3
# After aother 30 minutes walk , you and Rachel are closer to the top.
# However, your energy level decreased 20% and the sky is getting darker.
# Your friend Rachel is super hungry.
# Option 1 : wanted to go back to the cave. ignore friend away
# Option 2&3 : find food and place no= food all eaten by Rachel yes = looked around and found some rabbits
# cature = food and no = food all eaten by Rachel
#
# Rising actioon
#
#
#

# Climax
#
#
#
#

# Resolution
#
#
#
#
#
