FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):

    """ Read a text file and returns a to-do list"""

    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):

    """Write the to-do items list in the text file """

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# Below code will only be executed if functions.py is ran directly. It will not be executed if Main Program calls this function(Import function)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())