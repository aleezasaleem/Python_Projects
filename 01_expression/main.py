# 1. DiCESIMULATOR
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random

num_sides = 6


def roll_dice():
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)
    total: int = die1 + die2
    print("Total of two dice:", total)


def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()

print("___________________________\n")

# 2. E=MC2
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.
C: int = 299792458  # The speed of light in m/s


def main():
    print("This program is to calculate Einstein energy formula ")
    mass = float(input("Enter a mass in kg:"))
    print("e = m*c**2")
    print(f"mass={mass} kg")
    print(f"C={C} m/s")
    energy = mass * C**2
    print(f"{energy} joules of energy!")


if __name__ == "__main__":
    main()


print("___________________________\n")

# 3. FEET TO INCHES
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

inches_per_foot: int = 12


def main():
    print("This program is to convert feet to inches")
    feet: float = float(input("Enter the number of feet:"))
    inches = feet * inches_per_foot
    print(f"{feet} feet is equal to {inches} inches")


if __name__ == "__main__":
    main()


print("___________________________\n")
# 4. PYTHAGOREAN_THEOREM
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.
import math


def main():
    print("This program is to calculate pythagoream theorem of right triangle")
    side_AB: float = float(input("Enter the length of AB:"))
    side_AC: float = float(input("Enter the length of AC:"))
    side_BC: float = math.sqrt(side_AB**2 + side_AC**2)
    print(f"The length of side BC (Hypotenous) is {side_BC}")


if __name__ == "__main__":
    main()


print("___________________________\n")

# 5.Remainder_Division
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.


def main():
    print("This program is to calculate remainder of division ")
    num1: int = int(input("Enter the first number:"))
    num2: int = int(input("Enter the second number:"))
    qoutient: int = num1 // num2
    remainder: int = num1 % num2
    print(
        "The result of this division is "
        + str(qoutient)
        + " with a remainder of "
        + str(remainder)
    )


if __name__ == "__main__":
    main()

print("___________________________\n")
# 6.Roll-Dice
# Simulate rolling two dice, and prints results of each roll as well as the total
import random

side_of_dice = 6


def main():
    print("This is roll dice program")
    die1 = random.randint(1, side_of_dice)
    die2 = random.randint(1, side_of_dice)
    total = die1 + die2
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")


if __name__ == "__main__":
    main()

print("___________________________\n")
# 6b:Seconds in year

# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.


def main():
    print("This program is to calculate seconds in a year")
    seconds_in_minute = 60
    minute_in_hour = 60
    hours_in_a_day = 24
    day_in_a_year = 365
    total_Seconds = seconds_in_minute * minute_in_hour * hours_in_a_day * day_in_a_year
    print(f"There are {total_Seconds} in a year!")


if __name__ == "__main__":
    main()
print("___________________________\n")

# 7.Tiny Mad Lib
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.
Starter_Sentence = "Coding is complex . I had start some fun with"


def main():
    print("This is Tiny Mad libs fun program")
    adj: str = str(input("Please type an adjective and press enter: "))
    noun: str = str(input("Please type a noun and press enter: "))
    verb: str = str(input("Please type a verb and press enter: "))
    print(f"{Starter_Sentence},{adj},{noun},{verb}")


if __name__ == "__main__":
    main()
