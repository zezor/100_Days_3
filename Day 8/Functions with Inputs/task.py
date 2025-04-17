# def greet():
#     print("Hello Emma")
#     print("How do you do?")
#     print("Isn't the weather nice?")
# greet()
#
#
# # Functions with input
#
# def greet_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name} ?")
#     print("Isn't the weather nice?")
#
# greet_name("Gloria")
from itertools import count


# name = parameter....name of that data being passed to that data
# Gloria = argument.... data to pass to a function

# import maths

# def life_in_weeks(age):
#     age = int(input("What is your age?"))
#     years_in_weeks = 52
#     weeks_in_90yrs = 52 * 90
#     weeks_left = weeks_in_90yrs - (age * 52)
#     print(f"You have {weeks_left} weeks to live")
#
#
# life_in_weeks(31)


# Functions with more than one input
#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Gloria" , "Kumasi")
#
#
# #adding keyword argument
# greet_with( name="Emma", location="Techiman")
# greet_with( location="Techiman", name="Emma")



def calculate_love_score(name1, name2):
    true_love = "TRUE LOVE"
    for char in true_love:
        if char in name1 and name2:
            char.count()
            print(char)
            print("Yes")

calculate_love_score("GLORIA", "EMMANUEL")