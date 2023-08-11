import os
import json


pathjoin = os.path.join


def notebook_new(notebook_name: str):
    try:
        print('===== Already Existing Notebooks =====')
        for notebook in os.listdir('notebooks'):
            print(notebook)

        if notebook_name not in os.listdir(pathjoin(THIS_DIR, 'notebooks')):
            open(pathjoin('notebooks', notebook_name), 'x').close()
    except FileExistsError:
        print("Notebook with that name already exists.")


def notebook_clear(notebook_name: str):
    open(pathjoin(THIS_DIR, 'notebooks', notebook_name), 'w').close()


def notebook_read(notebook_name: str):
    with open(pathjoin('notebooks', notebook_name), 'r') as notebook:
        print(f"----------- Start of Notebook: {notebook_name} ----------")
        for line_num, line in enumerate(notebook):
            print(f'{line_num + 1}. {line}', end='')
        print(f"\n----------- End of Notebook: {notebook_name}  -----------")


def notebook_write(notebook_name: str):
    notebook_input: str = input("What would you like to write: ")
    if notebook_input in r'exit-close':
        return False
    elif notebook_input in r'\n-new-line':
        with open(pathjoin('notebooks', notebook_name), 'a') as notebook:
            notebook.write('\n')
    else:
        with open(pathjoin('notebooks', notebook_name), 'a') as notebook:
            notebook.write(f'{notebook_input}\n')

        notebook_write(notebook_name)


def notebook_edit(notebook_name: str):
    try:
        line_to_edit: int = int(input("What line would you like to edit: "))
    except ValueError:
        print("That is not a valid line number")
        return
    new_content: str = input("What would you like the new content to be: ")
    with open(pathjoin('notebooks', notebook_name), 'r+') as notebook:
        notebook.seek(0)
        notebook_content = notebook.readlines()
        notebook_content[line_to_edit - 1] = f'{new_content}\n'

        notebook_clear(notebook_name)
        for line in notebook_content:
            notebook.write(line)


def notebook_command_processor():
    notebook_input: str = input("Enter a notebook command: ")

    if notebook_input in r'create-new':
        notebook_input = input("Enter the name of new notebook: ")

        notebook_new(notebook_input)
        notebook_command_processor()
    elif notebook_input in r'write':
        try:
            notebook_input = input("What notebok are you trying to access: ")
            notebook_write(notebook_input)
            notebook_command_processor()
        except FileNotFoundError:
            print("A notebook of that name doesn't exist")

            notebook_command_processor()
    elif notebook_input in r'edit':
        notebook_input: str = input("What notebook are you trying to access: ")
        notebook_edit(notebook_input)

        notebook_command_processor()
    elif notebook_input in 'delete-remove':
        notebook_input = input("Enter name of notebook to remove: ")
        notebook_remove(notebook_input)
        notebook_command_processor()
    elif notebook_input in r'read-peek-look-check':
        notebook_input = input("What notebook are you trying to access: ")
        notebook_read(notebook_input)
        notebook_command_processor()
    elif notebook_input in r'exit-close':
        return
    else:
        print('Invalid notebook command')

