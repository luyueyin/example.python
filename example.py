import numbers
from unittest import result


def _introduction(operation):
    weclome_string = "Welcome to the calculator program."
    prompt_string = f"Please give me two values to {operation}."
    print(f"welcome_string\n{prompt_string}")

def _get_number(i):
    number = float(input(f"Number {i}: "))
    return number

# _get_number(1)
# _get_number(2)

def _print_result(first_number, second_number, operation, result):
    # 7 + 6 =13
    print(f"{first_number} {operation} {second_number} = {result}")




# ---------


def add_number():
    _introduction("add")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 + num2
    _print_result(num1, num2, "+", result)


def subtract_number ():
    _introduction("subtract")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 - num2
    _print_result(num1, num2, "-", result)

def multiply_number():
    _introduction("multiple")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 * num2
    _print_result(num1, num2, "*", result)

def divide_number():
    _introduction("divide")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 / num2
    _print_result(num1, num2, "/", result)

# add_number()
# subtract_number()
# multiply_number()
# divide_number()