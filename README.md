# B-bot v.a.1.0.0
This is B-bot, my personal virtual assistant. B-bot's purpose is to house all of the virtual functionality that would normally be spread out over multiple different applications.
## ===== Commands =====
B-bot has many built in commands which can be used for completing several different tasks. All commmands must be lower case. If a command isn't properly formatted, or it doesn't exist, B-bot will state "Invalid Command"

### ==== Help ====
___
If you would like to know about all of B-bots features, you can type "help" into the command prompt, and he will give you a list of all the subjects that he's versed in. Form that list, you can select one subject, then see all of B-bots functionalities that fall under that subject. 

Currently, the subjects B-bot has include:
- Calculator
    - Arithmetic
    - Area & Volume
    - Quadratic Formula
- Notebooks
    - Create new notebooks
    - Edit existing notebooks
    - Read notebooks

**If you want to check the version of B-bot you are using, you can type the command "version" or "model"**

### ==== Calculator ====
___
B-bot comes with a built in calculator tha can be used for helping with math. B-bot's calculator has three main functions: arithmetic, area, and volume. I want to add trigonometry featurs in version 1.0.0+, but I currently don't possess the knowledge to implement such features.

B-bot accepts a calculation in three parts. First, he prompts the user to enter an operator. Secondly, he prompts the user to enter the first number for calculation. Finally, he prompts the user the enter the second number for calculation, before displaying the equation with the result.
```
Enter an operation: -
Enter first number: 6
Enter second number: 4
6.0 - 4.0 = 2.0
```

### ==== Notebooks ====
___
Allows for the user to create and edit notebooks. These notebooks only hold plain text. In version 1.0.0+, the notebooks will be able to contain bolded text, italicized text, underlined text, images, bulleted lists, and hyperlinks.

To enter notebook mode, simply type "note" or "notebook" into B-bot's command prompt. If you would like to back to the standard command prompt, just type "exit"

While in notebook mode, B-bot will prompt you to 
```
Enter a notebook command: 
```
There are three (soon to be four) different notebook commands that you can use.
* Create
  * To create a new notebook, you can type either "create" or "new" into the notebook prompt
* Write
  * To write into a notebook, you can type "write". The text will automatically be added on to the end of the notebook.
* Edit
  * To edit a notebook, you can type "edit". B-bot will them prompt you to enter a line number, and once you do, he will prompt you to enter what you want the new line to be.
* Read
  * To read the contents of a notebook, you can type "read", and B-bot will them prompt you to open a notebook.

**When typing in a notebook name, only type the name of the notebook, and not the file extension ".txt"**

## ===== Limitations =====
- Calculator
  - B-bot cannot evaluate expressions or equations (this feature will be present in version 1.0.0+)
- B-bot doesn't have any functionality that wasn't already programmed into him, which I am hoping to either adress in versions 2.0.0 or 3.0.0
