def Calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    Operator = str(input("Select operation (x, /, +, -, %): "))

    if Operator == "x":
        result = float(num1) * float(num2)
        print(result)
    elif Operator == "/":
        result = float(num1) / float(num2)
        print(result)
    elif Operator == "+":
        result = float(num1) + float(num2)
        print(result)
    elif Operator == "-":
        result = float(num1) - float(num2)
        print(result)
    elif Operator == "%":
        result = float(num1) % float(num2)
        print(result)
    if Operator not in ["x", "/", "+", "-", "%"]:
        print("Invalid operator selected. Please choose from x, /, +, -, %.")

Calculator()