print("*-------------------------------------------*")
print("Insert First Number: ", end="")

num1 = float(input())

print("Insert Second Number: ", end="")

num2 = float(input())\

print("*-------------------------------------------*")

print("Insert Arithmetic Operator:\n1. Multiply\n2. Divide\n3. Add\n4. Subtract")
print("input Operator: ", end="")
Operator = int(input())

if Operator == 1:
    print("Result:", num1 * num2)

elif Operator == 2:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

elif Operator == 3:
    print("Result:", num1 + num2)

elif Operator == 4:
    print("Result:", num1 - num2)

else: 
    print("Invalid operator")

print("*-------------------------------------------*")

