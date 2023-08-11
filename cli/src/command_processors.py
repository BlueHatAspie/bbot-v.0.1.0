import mMathPy  # Calculator(Arithmetic, Area, Volume)
import mSciPy  # Periodic Table Functions
import mNotebooksPy # Notebook Functions
import mCookingPy # Email List To Mom

import os
import datetime
from time import sleep


def text_command_processor(command_input: str):
    if command_input.lower() == "help":
        print(
            "Examples: \n"
            "    Math\n"
        )
        help_input = input("What subject are you looking for help on: ")

        if help_input in "mathematics area calculate graph":
            print(
                "Math functions:"
                "\n    calculator/calc"
                "\n      arithmetic (addition, subtraction, multiplication, division, modulus, exponent)"
                "\n      area (circle, triangle, square, rectangle, trapezoid)"
                "\n      volume (sphere, cube, cylinder, rectangular prism)"
            )
        else:
            print("I apologize, that is not a subject I can help you with")
    elif command_input.lower() == "calc" or command_input == "calculator":
        mMathPy.calc()
        print("Placeholder")
    elif command_input.lower() in "notebooks":
        mNotebooksPy.notebook_command_processor()
    elif command_input.lower() == "date":
        dt = datetime.date.today()
        print(f'{dt.month}/{dt.day}/{dt.year}')
        del dt
    elif command_input.lower() == "time":
        print(f'{datetime.time.hour}')
    elif command_input.lower() == "send list":
        mCookingPy.send_list()
    elif command_input.lower() in 'version-model':
        print("B-bot(Python) v.a.1.0.0")
    elif command_input.lower() == "clear":
        os.system('cls')
    elif command_input.lower() == "debug":
        print("Placeholder")
    else:
        print("Invalid Command")


