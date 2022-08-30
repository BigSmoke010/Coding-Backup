import math
import fire

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


if __name__ == '__main__':
    fire.Fire(calc)
