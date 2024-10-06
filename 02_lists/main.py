# 1. ADD_MANY_NUMBERS
# Write a function that takes a list of numbers and returns the sum of those numbers.
def sum_of_num(number):
    return sum(number)


def main():
    print("This program is to calculate sum of list ")
    numbers_list: list[int] = [2, 4, 3, 2, 1, 7]
    total = sum_of_num(numbers_list)
    print(f"The sum of numbers is {total} ")


if __name__ == "__main__":
    main()

# 2.Double list
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]


def double(number):
    return [num * 2 for num in number]


def main():
    print("This program is double sum of list")
    double_list: list[int] = [1, 2, 3, 4, 5]
    result = double(double_list)
    print(f"The double sum of list is {result}")


if __name__ == "__main__":
    main()

# 3.Erase Canvas
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Canvas Eraser Example")

# Canvas size and grid parameters
canvas_width = 500
canvas_height = 500
cell_size = 50

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create a list to hold references to the grid cells
cells = []


# Function to create a grid of blue cells
def create_grid():
    for i in range(0, canvas_width, cell_size):
        row = []
        for j in range(0, canvas_height, cell_size):
            rect = canvas.create_rectangle(
                i, j, i + cell_size, j + cell_size, fill="blue", outline="black"
            )
            row.append(rect)
        cells.append(row)


# Eraser properties
eraser_size = 100
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, outline="black")


# Function to handle the erasing process
def erase(event):
    # Move the eraser to the mouse pointer's position
    canvas.coords(
        eraser,
        event.x - eraser_size // 2,
        event.y - eraser_size // 2,
        event.x + eraser_size // 2,
        event.y + eraser_size // 2,
    )

    # Get eraser coordinates
    eraser_coords = canvas.coords(eraser)
    x1, y1, x2, y2 = eraser_coords

    # Check which cells are within the eraser's bounds and turn them white
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            cell_coords = canvas.coords(cell)
            if (cell_coords[2] > x1 and cell_coords[0] < x2) and (
                cell_coords[3] > y1 and cell_coords[1] < y2
            ):
                canvas.itemconfig(cell, fill="white")


# Bind the mouse motion to the erase function
canvas.bind("<B1-Motion>", erase)

# Create the grid
create_grid()

# Start the main loop
root.mainloop()
# 4.Flowing with data structure
# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

# However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.


def add_three_copies(list, data):
    for i in range(3):
        list.append(data)


def main():
    print("This program is used to add data flow ")
    message = input("Enter a message to copy: ")
    my_list = []
    print("My list before", my_list)
    add_data = add_three_copies(my_list, message)
    print("My list after added data", add_data)


if __name__ == "__main__":
    main()


# 5.Get First Element
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
def get_first_element(lst):
    # Print the first element of the list
    print("The first element is:", lst[0])


# Function to prompt the user for a list
def input_list():
    # Ask the user how many elements they want in the list
    n = int(input("Enter the number of elements in the list: "))

    # Initialize an empty list
    lst = []

    # Prompt the user for list elements one by one
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)

    return lst


# Get the list from user input
user_list = input_list()

# Call the function to print the first element
get_first_element(user_list)


# 6.Get last element
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
def get_last_element(lst):
    # Print the last element of the list
    print("The last element is:", lst[-1])


def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")

    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")

    return lst


def main():
    lst = get_lst()
    get_last_element(lst)


if __name__ == "__main__":
    main()

# 7.get list
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.


def input_values():
    # Initialize an empty list to store the user's inputs
    values = []

    # Continuously ask for input
    while True:
        user_input = input("Enter a value (or press Enter to finish): ")

        # If the user presses Enter without typing, break the loop
        if user_input == "":
            break

        # Add the entered value to the list
        values.append(user_input)

    # Print the final list
    print("Your list:", values)


# Call the function to start the program
input_values()

# 8.Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.
MAX_LENGTH: int = 3


def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)


# There is no need to edit code beyond this point


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst


def main():
    lst = get_lst()
    shorten(lst)


if __name__ == "__main__":
    main()
