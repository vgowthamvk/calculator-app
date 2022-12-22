import os
from art import logo


def clear():
    return lambda: os.system('clear')


# Addition
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculation():
    print(logo)
    is_continue = True
    num1 = float(input("What's the first number?: "))
    while is_continue:
        symbols = []

        for operand in operations:
            symbols.append(operand)
            print(operand)

        operation_symbol = input("Pick an operation: ")
        if operation_symbol in symbols:
            num2 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")
            y_r_n = input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to exit or 'new' to start a new calculation: ")
            if y_r_n == 'y':
                is_continue = True
                num1 = answer
            elif y_r_n == 'new':
                clear()
                is_continue = False
                calculation()
            else:
                print("Thank you for using Calculator have a great day!")
                is_continue = False

        else:
            print("Invalid input choose again")


calculation()
