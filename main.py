from cgi import print_directory
import numbers
from unittest import result


def my_function():
    print("Hello")
    print("This is a function!")
    result = 900 + 1
    return result

print(my_function())



def my_function():
    print("Hello")
    print("This is a function!")
    result = 900 + 1
    return result

function_output = my_function()
print(function_output+2)


def my_function(number: int):
    print("Hello")
    print("This is a function!")
    number = int(input("Give me a number: "))
    result = number + 1
    return result

function_output = my_function()
print(function_output+2)



# The function definition needs to give a name to the expected inputs.
# There names are *parameters*

# When the function id called, the inputs that are given are called the *arguments*

def my_function(some_parameter):
    some_value = "a string, maybe"
    return f"{some_value}, {some_parameter}"

    # some_argument = 7

    my_function(some_argument)
