# ---------------------------------- Arithmetic  ----------------------------------------------------- #

from math import sqrt

def calc_volume():
    volume_input: str = ""
    a = 0.0
    b = 0.0
    c = 0.0
    r = 0.0  # r = result

    volume_input = input("Enter shape you are trying to find the volume of: ")

    if volume_input == "sphere":  # volume of sphere: (4/3) * PI * radius ^ 3
        a = float(input("Enter radius of sphere: "))
        r = (4 / 3) * 3.14159 * (a * a * a)

        print(f'The volume a sphere with a radius of {a} is {r}')
    elif volume_input == "cone":  # volume of cone: ( (PI * radius ^ 2) * height) / 3
        a = float(input("Enter radius of base of cone: "))
        b = float(input("Enter height of cone: "))
        r = ((3.14159 * (a * a)) * b) / 3

        print(f'The volume of a cone with a radius of {a} and a height of {b} is {r}')
    elif volume_input == "cube":
        a = float(input("Enter side length of cube: "))
        r = a * a * a

        print(f'The volume of a cube with a side length of {a} is  {r}')
    elif volume_input in "rectangular prism":  # volume of rectangular prism: length * width * height
        a = float(input("Enter length of rectangular prism: "))
        b = float(input("Enter width of rectangular prism: "))
        c = float(input("Enter height of rectangular prism: "))
        r = a * b * c

        print(f'The volume of rectangular prism with the dimensions L:{a} W:{b} H:{c} is {r}')
    elif volume_input == "cylinder":  # volume of cylinder: (PI * radius ^ 2) * height
        a = float(input("Enter radius of cylinder: "))
        b = float(input("Enter height of cylinder: "))
        r = (3.14159 * (a * a)) * b

        print(f'The volume a cylinder with a radius of {a} and a height of {b} is {r}')
    else:
        print("Invalid Shape")


def calc_area():
    area_input: str = ""
    a = 0.0
    b = 0.0
    c = 0.0
    r = 0.0  # r = result

    area_input = input("Enter shape you are trying to find the area of: ")

    if area_input == "square":
        a = float(input("Enter side length of square: "))
        r = a * a
        print(f'The area of a square with a side length of {a} is {r}')

    elif area_input in "rect rectangle":
        a = float(input("Enter width of rectangle: "))
        b = float(input("Enter length of rectangle: "))
        r = a * b

        print(f'The area of a rectangle with the dimensions:{b} W:{a} H:{c} is {r}')
    elif area_input == "circle":  # area of circle: PI * r ^ 2
        a = float(input("Enter radius of circle: "))
        r = 3.14159 * (a * a)

        print(f'The area of a circle with a radius of {a} is {r}')
    elif area_input == "triangle":  # area of triangle: (1/2) * base * height
        a = float(input("Enter base of triangle: "))
        b = float(input("Enter height of triangle"))
        r = 0.5 * a * b

        print(f'The area of a triangle with a base of {a} and a height of {b} is {r}')
    elif area_input == "trapezoid":  # area of trapezoid: (a + b)/2 * height
        a = float(input("Enter top length of trapezoid: "))
        b = float(input("Enter bottom length of trapezoid: "))
        c = float(input("Enter height of trapezoid: "))
        r = ((a + b) / 2) * c

        print(
            f'The area of a trapezoid with a top side length of {a}, bottom side length of {b}, and height of {c} is {r}')
    else:
        print("Invalid Shape")


def quadratic_equation(a: float, b: float, c: float):
    if a > 0:
        result_one =  ((-1)*b + sqrt(b**2 - (4 * a * c) )) / 2 * a
        result_two =  ((-1)*b - sqrt(b**2 - (4 * a * c) )) / 2 * a

        if result_one != result_two:
            return (result_one, result_two)
        else:
            return result_one


def calc():
    a: float = 0
    b: float = 0
    result: float = 0
    calc_input: str = input("Enter type of calculation: ")

    if calc_input in "+ add addition":
        a = float(input("Enter first number for calculation: "))
        b = float(input("Enter second number for calculation: "))

        result = a + b
        print(f'{a} + {b} = {result}')
        calc()
    elif calc_input in "- subtract subtraction":
        a = float(input("Enter first number for calculation: "))
        b = float(input("Enter second number for calculation: "))

        result = a - b
        print(f'{a} - {b} = {result}')
        calc()
    elif calc_input in "* multiply multiplication":
        a = float(input("Enter first number for calculation: "))
        b = float(input("Enter second number for calculation: "))

        result = a * b
        print(f'{a} * {b} = {result}')
        calc()
    elif calc_input in "/ divide division":
        a = float(input("Enter first number for calculation: "))
        b = float(input("Enter second number for calculation: "))

        result = a / b
        print(f'{a} / {b} = {result}')
        calc()
    elif calc_input in "% mod modulo remainder":
        a = int(input("Enter first number for calculation: "))
        b = int(input("Enter second number for calculation: "))

        result = a % b
        print(f'{a} % {b} = {result}')
        calc()
    elif calc_input in "^ pow power exp exponent":
        a = float(input("Enter first number for calculation: "))
        b = int(input("Enter second number for calculation: "))

        result = a ** b
        print(f'{a} ^ {b} = {result}')
        calc()
    elif calc_input in "volume":
        calc_volume()
        calc()
    elif calc_input in "area":
        calc_area()
        calc()
    elif calc_input in "quadratic equation quadratic formula":
        a = float(input("Enter a (ax^2): "))
        b = float(input("Enter b (bx): "))
        result = float(input("Enter c (constant): "))
        quadratic_equation(a, b, result)
    elif calc_input == "exit":
        print("Exited calculator")
    else:
        print("Invalid Calculation")
        calc()