# Functions
# Author: Coco
# Oct 10
#


def create_mood_message(name: str, mood: str):
    if mood == "happy":
        return f"Hey {name}, great to see you smiling!"

    elif mood.strip(".,").lower() == "sad":
        return f"I hope your day gets better, {name}."

    elif mood.strip(".,").lower() == "neutral":
        return f"Sometimes you have average days, {name}."

    else:
        return f"Hi {name}, hope you're having a good day."


result = create_mood_message("Coco", "happy")
print(result)
result = create_mood_message("Alicia", "sad")
print(result)


def the_result_message(name: str, mood: str):  # str is ""
    if mood.strip(".,").lower() == "apple":
        return f" {name}, u are a healthy eater."

    elif mood.strip(".,").lower() == "pizza":
        return f" {name} , this sounds delicious."

    elif mood.strip(".,").lower() == "ice-cream":
        return f" {name} , this sounds yummy."

    else:
        return f" {name} ok, good for u."


# def - if + elif + else
# .strip(".,").lower() == "x":
# return

#
result = the_result_message(
    "Coco", "pizza"
)  # (name: str, mood: str)-> putting the result here
print(result)
result = the_result_message("Rachel", "apple")
print(result)


def average(num_one: int, num_two: int, num_three: int):
    output = (num_one + num_two + num_three) / 3
    return output


result = average(41, 33, 36)
print(result)
