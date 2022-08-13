import math


def calc(x, y, z=None) -> int:
    
    if y == "/":
        result = x / z
        print(f"{x} / {z} = {result}")
    
    elif y == "*":
        result1 = x * z
        print(f"{x} * {z} = {result1}")
    
    elif y == "-":
        result2 = x - z
        print(f"{x} - {z} = {result2}")
    
    elif y == "+":
        result3 = x + z
        print(f"{x} + {z} = {result3}")
    elif y == "sqr":
        print(f"√{x} = {math.sqrt(x)}")
    
    elif y == "pow":
        print(f"{x}**2 = {x**2}")
        
    else:
        print("invalid input")


x1 = int(input("number1 : "))
y1 = str(input("operator : "))

if y1 == "sqr":
    calc(x1, y1)

else:
    z1 = int(input("number2 :"))
    calc(x1, y1, z1)
