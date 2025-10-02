# Notes - Introduction
# Sep 16th
# Coco Woo

# Create an algorithm to solve a problem
# Problem: Create our own chatbot
#           CocoGPT

# 1. Greet the users with a predetermined statement
greeting = " Hello! I am a chatbot."

# 1a. Print the greeting
print(greeting)

# 2. Introduce the bot
print("My name is CocoGPT")
print("I'm not like the other guy")
print("I am completely deterministic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8*8 is.")
print("I can do it.")
print(f"8*8 is actually {8*8}.")

print("What is pi squared?")
print("I'm smart, I can do it too.")
print(f"It is {3.14159265359 ** 2}")

# 4. Make the bot crash out a little bit
print("The quick brown fox jumps over the lazy dog." * 10)

# 5. Get the name of the user, store it, and use ti
user_name = input("What's your name?")
print(f"It's nice to meet you, {user_name}!")

# 6. Ask them three questions
food = input("What food do you like to eat?")
print(f"{food} sounds so good!")

# 7. Know their dream vacation destination
place = input("What's your dream vacation destination?")
print(f" Really!! I've never been to {place} .That's also my dream.")

# 8. Know their favourite color
color = input("What is your favourite colour?")
print(f" I like blue the most , but {color} is one of my favourites too!!")

# 9. See IF the user is someone specific
# 9a. If they're someone specific, tell them a secret
if user_name == "Rachel":
    print("I know that you like to eat ice-cream.")
    print("But I won't tell anyone. Shhhhhh. 🤪")

    favourite_book = input("What's your favourite book?")

    if favourite_book == "Harry Potter":
        print("No way!! My favourite book is also Harry Potter.")

elif user_name == "Spongebob":
	print("Who lives in a pineapple under the sea?")
	print("Spongebob Squarepants.")
elif user_name == "Abrham Lincoln":
	print("Abe Lincoln? I heard you're a good wrestler.")
else:
	print("I don't have ant]y screts for you.")
