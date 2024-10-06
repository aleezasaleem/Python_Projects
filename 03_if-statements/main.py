# Print Events
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements


def main():
    for i in range(20):
        print(i * 2)


if __name__ == "__main__":
    main()

# International-voting-age
# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.
PETURKSBOUIPO = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48


def main():
    print("This program is for international voting age")
    candidate_age = int(input("Enter Your age:"))
    if candidate_age >= PETURKSBOUIPO:
        print(f"You can vote in PETURKSBOUIPO where the voting age is ,{PETURKSBOUIPO}")
    else:
        print(
            (
                f"You cannot vote in PETURKSBOUIPO where the voting age is ,{PETURKSBOUIPO}"
            )
        )
    if candidate_age >= STANLAU_AGE:
        print(f"You can vote in STANLAU where the voting age is ,{STANLAU_AGE}")
    else:
        print((f"You cannot vote in STANLAU where the voting age is ,{STANLAU_AGE}"))
    if candidate_age >= MAYENGUA_AGE:
        print(f"You can vote in MAYENGUA where the voting age is ,{MAYENGUA_AGE}")
    else:
        print((f"You cannot vote in MAYENGUA where the voting age is ,{MAYENGUA_AGE}"))


if __name__ == "__main__":
    main()
# leap year
# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.

# In the Gregorian calendar, three criteria must be checked to identify leap years:

# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year


def main():
    print("This program is to read a leap year or not")
    year = int(input("Please input a year:"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year")
            else:
                print("That's  not a leap year")
        else:
            print("That's a leap year")
    else:
        print("That's  a leap year")


if __name__ == "__main__":
    main()

# Tall enough to ride
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

minimum_height: int = 50


def main():
    height = float(input("Please tell your height:"))
    if height >= minimum_height:
        print("You are tall enough to ride")
    else:
        print("You are not able to ride,may be next year you will be able to ride")


if __name__ == "__main__":
    main()

# Random Number
# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)

import random


def main():
    print("This code is to generate 10 random number")
    random_number = [random.randint(1, 100) for _ in range(10)]
    print(random_number)


if __name__ == "__main__":
    main()
