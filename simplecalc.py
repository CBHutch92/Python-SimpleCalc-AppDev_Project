while True:
    print ("\n Simple Calculator Menu:")
    print ("a. Addition")
    print ("b. Subtraction")
    print ("c. Multiplication")
    print ("d. Division")
    print ("e. Exit")

    choice = input("Enter your choice of operator (a/b/c/d or e to exit):").lower()

    if choice == 'e':
        print("Thank you for using the calculator. Have a great day.")
        break
    elif choice == 'a':
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
        result = num1 + num2
        print(f"Result: {num1} + {num2} + {result}")
    elif choice == 'b':
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == 'c':
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == 'd':
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
        if num2 == 0:
            result = None
        else:    
            result = num1 / num2
        if result is None:
            print("Cannot divide by zero")
        else:
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid input. Please select from the available options and try again.")