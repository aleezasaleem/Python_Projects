# QUESTION: ADD TWO NUMBER
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.


def main():
    print("This program adds two numbers.")
    num1 = str(input("Enter Your first number:"))
    num1 = int(num1)
    num2 = str(input("Enter Your second number:"))
    num2 = int(num2)
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")


if __name__ == "__main__":
    main()

print("____________________________________________________\n")

# QUESTION: AGREEMENT BOT
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow


def main():
    print("This program ask the user what's their favourite animal. ")
    favourite_animal = str(input("What's your favorite animal:"))
    print(f" My favorite animal is also {favourite_animal} !")


if __name__ == "__main__":
    main()

# QUESTION: FAHRENHEIT TO CELCIUS
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)


print("____________________________________________________\n")


def main():
    print("This program is for convert fahrenheit to celcius")
    degrees_fahrenheit = float(input("Enter  temperature in fahrenheit:"))
    degrees_celcius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature {degrees_fahrenheit} F = {degrees_celcius} C")


if __name__ == "__main__":
    main()

print("____________________________________________________\n")

# QUESTION: HOW_OLD_ARE_THEY
# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!)


def main():
    print("This program is to solve this age-related riddle!")
    Anton: int = 21
    Beth: int = 6 + Anton
    Chen: int = 20 + Beth
    Drew: int = Chen + Anton
    Ethan: int = Chen
    print(f"Anthon is {Anton} year old")
    print(f"Beth is {Beth} year old")
    print(f"Chen is {Chen} year old")
    print(f"Drew is {Drew} year old")
    print(f"Ethan is {Ethan} year old")


if __name__ == "__main__":
    main()

print("____________________________________________________\n")

# QUESTION: TRIANGLE PERIMETER
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5


def main():
    print("This program is to calculate perimeter of the triangle ")
    side1 = int(input("What is the length of side 1:"))
    side2 = int(input("What is the length of side 2:"))
    side3 = int(input("What is the length of side 3:"))
    perimeter_of_triangle = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter_of_triangle}")


if __name__ == "__main__":
    main()

print("____________________________________________________\n")
# QUESTION:SQUARE NUMBER


# Ask the user for a number and print its square (the product of the number times itself).
def main():
    print("This program is to ask the user for number and print its square")
    num = float(input("Type a number to see its square:"))
    square: float = num * num
    print(f"{num} squared is {square}")


if __name__ == "__main__":
    main()
