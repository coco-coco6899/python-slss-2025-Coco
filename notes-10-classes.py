# classes and objects
# Author: Coco
# Dec 11, 2025

import random


class Pokemon:
    def __init__(self):  # what's the pokemoon have
        """Constructor"""
        self.name = ""  # name for pokemon
        self.species = ""
        self.type = "normal"
        self.level = 1
        self.age = 0
        self.dance = "knows how to dance"
        # 1 in 4096
        if random.randint(0, 4096):
            self.is_shiny = False
        else:
            self.is_shiny = True
            print("tHIS pokemon is shinny.")

        print("A pokemon is born!")

    def talk(self):  # self refers to the pokemon itself
        """HEar what the pokemon has to say
        the pokemon says its species name"""
        print(f'{self.name} says, "{self.species}".')

    def stats(self):
        """Display the stats of the pokemon"""
        print(f"---({self.species})--------------")
        print(f"   Name:  {self.name}")
        print(f"   Type:  {self.type}")
        print(f"   Age:  {self.age}")
        print(f"   Level:  {self.level}")
        print(f"   Dance:  {self.dance}")
        print("----------------------------------")


class Squirtle(Pokemon):
    def ___init___(self):
        # Call the constructor of Pokemon
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "water"

    def water_gun(self):
        """Squirtle shoots water out of its mouth"""
        print(f"{self.name} used water gun!")


class Jolteon(Pokemon):
    def ___init___(self):
        # Call the constructor of Pokemon
        super().__init__()
        self.name = "Jolteon"
        self.species = "Jolteon"
        self.type = "electrical"

    def thunder_bolt(self):
        """Jolteon shoots a thunder bolt out of its furrrrrr."""
        print(f"{self.name} used a thunder bolt!")


if __name__ == "__main__":
    # create a pokemon object
    pokemon_one = Pokemon()  # create pokemon
    # access the pokemn's properties
    print("Pokemon name: ", pokemon_one.name)
    # change the pokemone's properties
    pokemon_one.name = "Rachel"
    pokemon_one.species = "Pikachu"
    print("Pokemon name: ", pokemon_one.name)
    # ceate another pokemon object
    pokemon_two = Pokemon()
    pokemon_two.name = "Alicia"
    pokemon_two.species = "Pikachu"
    # check to see if a value is a pokemon
    if pokemon_one == pokemon_two:
        print("They are the same.")
    else:
        print("They are individual pokemon.")

    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon.")

    # tell pokemon to talk
    pokemon_one.talk()
    pokemon_two.talk()

    # Display stats
    pokemon_one.stats()
    pokemon_two.stats()

    squirtle_one = Squirtle()
    # use water gun()
    squirtle_one.water_gun()
    # use talk ()
    squirtle_one.talk()

    jolteon_one = Jolteon()
    # use water gun()
    jolteon_one.thunder_bolt()
    # use talk ()
    jolteon_one.talk()
