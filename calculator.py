# functions for add, subtract, multiply and divide
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


while True:
    # for user input
    x = float(input("Enter the first number"))
    y = float(input("Enter the second number"))

    # creating list of operation
    operation = ["+", "-", "*", "/"]

    # Loop until a valid operator is chosen
    while True:
        choice = input("Choose the operator (+, -, *, /): ")
        if choice in operation:
            break
        else:
            print("Invalid operator. Please choose from +, -, *, /")

# choosing required operation
    if choice == "+":
        result = add(x, y)

    if choice == "-":
        result = subtract(x, y)

    if choice == "*":
        result = multiply(x, y)

    if choice == "/":
        result = divide(x, y)

    print("Result:", result)
    print("")


