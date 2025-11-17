# Coco Woo
# Nov 12, 2025

# Maths Stuff with Python
# Author: Ubial
# 12 November 2025

import math

# Do math things with Python
# Machines are good at crunching numbers - faster
# and more accurately than most humans!
# Create a small program that calculates something useful
# to you (making you smile is useful). It should take
# user input, at use at least one of the number
# operators we saw in class: + / * -. You may modify one
# of your previous exercises to include calculations,
# if you wish.


def main():
    # give me a numeber and i ll return it with the squareroot of that number
    """give me a numeber and i ll return it with the squareroot of that number"""
    print(
        "Give me a whole number like 1 , 100, 27 and I am gonna square root the number u gave me."
    )
    number = int(input(" "))
    square_root = math.sqrt(number)
    print(f"The square root of {number} is: {square_root}")


if __name__ == "__main__":
    main()


# def main():
#     print("How old are you now?")
#     number = int(input(" "))
#     addition = number + 24
#     print(f"In 2049, you will be {addition}.")


# if __name__ == "__main__":
#     main()

# def main()
#     a =  "1",
#     b = "2",
#     c = "3",
#     d = "4",
#     e = "5"
#     person_percentage = ("1" + "2" + "3" + "4" + "5") / 5
#     print(f"person percentage: {person_percentage * 100}% ")
