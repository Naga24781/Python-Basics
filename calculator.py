A = float(input("Enter a number: "))
B = float(input("Enter another number: "))
C = input("Select an Operator (+, -, %, /, *, //): ")

if C == "+":
    print("The value is:", A + B)
elif C == "-":
    print("The value is:", A - B)
elif C == "*":
    print("The value is:", A * B)
elif C == "%":
    if B!= 0:
        print("The value is:",A%B)
    else:
        print("Zero division error")
elif C == "/":
    if B != 0:
        print("The value is:", A / B)
    else:
        print("Error: Division by zero ❌")
elif C == "//":
    if B != 0:
        print("The value is:", A // B)
    else:
        print("Error: Division by zero ❌")
else:
    print("Invalid Operator ❌")
