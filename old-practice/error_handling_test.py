def divide(a, b):
    return a / b

while True:
    try:
        num1 = int(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for the first number.")

while True:
    try:
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Second number cannot be zero. Please enter a non-zero number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number for the second number.")

result = divide(num1, num2)
print("Result:", result)
print("Done")