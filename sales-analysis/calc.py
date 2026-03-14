def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


print("===CALCULATOR FUNCTIONS TEST===")

print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice.lower() == "q":
        break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
