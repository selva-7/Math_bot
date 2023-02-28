import operator

# Define a dictionary to map operator names to functions
OPERATORS = {
    "addition": operator.add,
    "subtraction": operator.sub,
    "multiplication": operator.mul,
    "division": operator.truediv,
}

def math_bot():
    print("Hi! I'm a math bot. What mathematical operation do you want to do?")
    while True:
        operation = input("> ").lower()
        if operation not in OPERATORS:
            print("Invalid operation. Please choose from the following options:")
            print(", ".join(OPERATORS.keys()))
            continue
        print(f"What is the first operand for {operation}?")
        operand1 = float(input("> "))
        print(f"What is the second operand for {operation}?")
        operand2 = float(input("> "))
        if operation == "division" and operand2 == 0:
            print("Error: can't divide by zero")
            continue
        result = OPERATORS[operation](operand1, operand2)
        print(f"{operation} of {operand1} and {operand2} is {result}")
        print("Do you want to start another operation? (yes/no)")
        another_operation = input("> ").lower()
        if another_operation != "yes":
            print("Goodbye!")
            break

math_bot()
