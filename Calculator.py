def addition(x, y):
    return x + y
def substraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y

print("Select operation:\n1: Addition\n2: Substraction\n3: Multiplication\n4: Division")

while True: 
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter your first number: "))
            number2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invlaid Input.")
            continue
        if choice == '1':
            print(number1, " + ", number2, ' = ', addition(number1, number2))
        if choice == '2':
            print(number1, " - ", number2, ' = ', substraction(number1, number2))
        if choice == '3':
            print(number1, " * ", number2, ' = ', multiplication(number1, number2))
        if choice == '4':
            print(number1, " / ", number2, ' = ', division(number1, number2))
        new_calculation = input("Do you want a new calculation? (yes/no) ")
        if new_calculation == "no":
            break
    else:
        print("Invalid Input")
