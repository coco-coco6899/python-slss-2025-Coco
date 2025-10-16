# Function
# Author: Coco
# Oct 8
#
#  function to print "hello" to the console
def say_hello():
    print("Hello")


say_hello()


# function to print a personalized hello
def say_hello_personal(name: str):
    print(f"Hello {name}!")


say_hello_personal("Coco")
say_hello_personal("Rachel")


def normalized_inut():
    """Clean up the user's input"""
    # get input from the user
    output = input()
    # .strip and .lower the input
    output = output.strip(".,").lower()
    # return the output


# Ask the user for the weather
print("What's the weather like?")
weather_reply = normalized_inut()

if weather_reply == "rainy":
    print("You should bring an unbrella.")


def some_fun():
    print("hello!")


def some_fun_return() -> str:
    print("hello!")
    return "purrr plee moom kii di shhs waoo sherr"

return_val = some_fun_return()

print(return_val)  # what's the difference?

return_val = some_fun_return()

print(return_val)  # what's the difference?

def say_hello_personal(name = "Tiger"):

say_hello_personal("Tiger")
