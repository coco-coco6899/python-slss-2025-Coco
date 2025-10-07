# (String) Methods
# Author: Coco
# Oct 6, 2025
#
# Ask the user what the weather is like
weather = input("What's the weather like today?")

if weather.lower().strip("!.?") == "rainy":
    print("You should ring an umbrella.")
else:
    print("iccc.")
