# Day 10. calculator program

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "invalid input"


def calculator():
    answer = int(input("Enter the first number."))
    end = False
    count = 0
    while not end:
        operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
        if count == 0:
            answer1 = int(input("Enter the second number."))
            count += 1
        else:
            answer1 = int(input("Enter a number."))
        operation = input(f"Pick an operation. {operations.keys()}")

        cal_func = operations[operation]

        answer = cal_func(answer, answer1)

        print(answer)
        cont = input(
            "Do you want to continue? y for continuing the calculation or n for exiting. Type 'new' for starting a "
            "new calculation.").lower()
        if cont == "n" or cont == "no":
            end = True
        if cont == "new":
            calculator()


calculator()
