import math
print("SCIENTIFIC CALCULATOR")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def division(x, y):
    
    if y == 0:
        return "Error! Cannot divide by zero!"
    return x / y

def multiplication (x, y):
    return x * y

def exponent(x, y):
    return x ** y

def percentage(x, y):
    if y == 0:
        return "Error! Cannot calculate percentage with a zero denominator!"
    return (x / y) * 100

# Trigonometric functions take degrees, convert to radians for math module
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))
    
def sec(x):
    return 1/math.sin(math.radians(x))
def cosec(x):
    return 1/math.cos(math.radians(x))
def cot(x):
    return 1/math.tan(math.radians(x))           

# Logarithm function
def log(x, y):
    # x is the number, y is the base
    if x <= 0 or y <= 0 or y == 1:
        return "Error! Logarithm requires a positive number and a positive base not equal to 1."
    return math.log(x, y)
    
def sqrt(x):
    return math.sqrt(x)    

def fact(x):
    # Factorial is only defined for non-negative integers
    if x < 0 or x != int(x):
        return "Error! Factorial is only defined for non-negative integers."
    return math.factorial(int(x))
    
        
while True:
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exponent")
    print("6. Percentage (x is part of y)")
    print("7. Sine (degrees)")
    print("8. Cosine (degrees)")
    print("9. Tangent (degrees)")
    print("10. Secant (degrees)")
    print("11. Cosecant (degrees)")
    print("12. Cotangent (degrees)")
    print("13. Logarithm (log(x) base y)")
    print("14. Factorial")
    print("15. Square Root")
    print("16. Exit")
    
    # All inputs from 'input()' are strings
    choice = input("Enter choice (1-16): ")

    if choice == '16':
        print("Exiting Calculator...")
        break
    
    # Two-number operations
    if choice in ('1', '2', '3', '4', '5', '6', '13'):
        try:
            num1 = float(input("Enter first number (x): "))
            num2 = float(input("Enter second number (y/base): "))
            
            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                result = division(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == "4":
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == "5":
                print(f"{num1} ** {num2} = {exponent(num1, num2)}")
            elif choice == "6":
                result = percentage(num1, num2)
                print(f"({num1} / {num2}) * 100 = {result}")
            elif choice == "13":
                result = log(num1, num2)
                print(f"Log({num1}) base {num2}: {result}")
                
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            
    # Single-number operations
    elif choice in ('7', '8', '9', '10', '11', '12', '14', '15'):
        try:
            # Factorial only works for integers, but others can be float
            if choice == '14':
                num = float(input("Enter non-negative integer for factorial: "))
            elif choice == '15':
                num = float(input("Enter number:"))  
            else:
                num = float(input("Enter number (degrees for sin/cos/tan/asin/acos/atan): "))

            if choice == '7':
                print(f"sin({num}°): {sin(num)}")
            elif choice == '8':
                print(f"cos({num}°): {cos(num)}")
            elif choice == '9':
                print(f"tan({num}°): {tan(num)}")
            elif choice == '10':
                print(f"sec({num}°): {sec(num)}")
            elif choice == '11':
                print(f"cosec({num}°): {cosec(num)}")
            elif choice == '12':
                print(f"cot({num}°): {cot(num)}")           
            elif choice == '14':
                result = fact(num)
                # Display the input as an integer if the operation was successful
                if isinstance(result, str):
                    print(result) # Print the error message
                else:
                    print(f"Factorial({int(num)}): {result}")
            elif choice == '15':
                print(f"Square Root({num}): {sqrt(num)}")       
                    
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Invalid choice. Please enter a number between 1 and 16.")
        