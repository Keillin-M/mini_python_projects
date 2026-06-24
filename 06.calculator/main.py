
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    loop = True
    result = 0
    first_number = float(input("Enter the first number: "))
    while loop:
        for key in operation:
            print(key)
        op = input("Pick an operation: ")
        second_number = float(input("Enter the second number: "))
        result = operation[op](first_number, second_number)
        print(f"{first_number} {op} {second_number} = {result}")
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if answer == "y":
            first_number = result
        else:
            first_number = float(input("Enter the first number: "))
            loop = False
            print("\n" * 20)

calculator()
