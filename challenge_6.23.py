import numbers
from unittest import result

# Working on their own, a senior developer can write an entire application in five hours.
# A mid-level developer would take ten hours to get the same amount of work done.
# A junior developer would need twenty hours to write the same app.

# Developers working together can combine their expertise, so two mid-level engineers can each do half the work, completing the app in five hours.

# By default, a team consists of one senior dev, two mid-level devs, and four junior devs.

# Write a function called calculate_development_time which takes the following parameters:
# num_senior_devs
# num_mid_devs
# num_junior_devs

# If no arguments are supplied, your function should return the time in hours it takes for a default-sized team to complete the app. If arguments are supplied, the function should return the time it would take the specified team to complete the app. For example:

# calculate_development_time() returns 1.66666...
# calculate_development_time(1, 4, 4) returns 1.25


def _introduction():
    print("Welcome to the calculator program.")
    print("Can you describe your team?")


def _get_number(x):
    number = int(input(f"The number of {x}: "))
    return number
    

#-------------------#

def calculate_development_time():
    _introduction()
    num1 = _get_number("Senior Developer")
    num2 = _get_number("Mid-level Developer")
    num3 = _get_number("Junior Developer")
    result = 20 / (4 * num1 + 2 * num2 + num3)
    return result

print(calculate_development_time())
