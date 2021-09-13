from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide,
}

chaining = True

print(logo)

num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

num2 = float(input("What's the second number?: "))

result = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")

while chaining:
    flag = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to exit: "
    ).lower()

    if flag != "y":
        chaining = False
        print("Goodbye!")
        break

    operation_symbol = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))

    old_result = result
    result = operations[operation_symbol](result, next_number)
    print(f"{old_result} {operation_symbol} {next_number} = {result}")
