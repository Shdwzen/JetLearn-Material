def linear_equation(a, b, x):
    return a * x + b

def quadratic_equation(a, b, c, x):
    return a * x**2 + b * x + c


print("Choose the type of equation:")
print("1. Linear (y = ax + b)")
print("2. Quadratic (y = ax^2 + bx + c)")
    
choice = int(input("Enter 1 for Linear or 2 for Quadratic: "))
    
if choice == 1:
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    print("Output values for x = 0 to x = 10:")
    for x in range(11):
        y = linear_equation(a, b, x)
        print(f"x = {x}, y = {y}")
elif choice == 2:
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    print("Output values for x = 0 to x = 10:")
    for x in range(11):
        y = quadratic_equation(a, b, c, x)
        print(f"x = {x}, y = {y}")
else:
    print("Seriously? Please run the program again and choose either 1 or 2")