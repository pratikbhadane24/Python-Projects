import os
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(art.logo)
    num1 = float(input("What is the first number?\n"))
    print("Operations:")
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue == True:
        operform = input("Pick an operation: ")
        num2 = float(input("What is the next number?\n"))
        calculation_function = operations[operform]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operform} {num2} = {answer} ")

        continuation = input(f"Type 'y' to continue working with {answer} OR 'n' to start new calculator\n(Type anything else to exit!)\n").lower()
        if continuation == "y":
            num1 = answer
        elif continuation == "n":
            print("Thank You!\nGoodbye!!")
            should_continue = False
            os.system('cls')
            calculator()
        else:
            print("Exiting.....!")
            exit()

calculator()