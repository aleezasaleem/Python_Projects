# Write a function that takes two numbers and finds the average between the two.
def main():
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    average = num1 + num2
    result = average / 2
    print(f"The average of {num1} and {num2} is {result}")


if __name__ == "__main__":
    main()


import random

DONE_LIKELIHOOD = 0.3


def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num)


def done():

    if random.random() < DONE_LIKELIHOOD:
        return True
    return False


def main():
    print(
        "I'm going to count until 10 or until I feel like stopping, whichever comes first."
    )
    chaotic_counting()
    print("I'm done")


if __name__ == "__main__":
    main()

# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task


def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1

    print(count)


def get_list_of_ints():

    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")

    return lst


def main():
    lst = get_list_of_ints()
    count_even(lst)


if __name__ == "__main__":
    main()

# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4


def main():
    input_num = int(input("Enter a number:"))
    double_num = input_num * 2
    print(f"The double of {input_num} is {double_num}")


if __name__ == "__main__":
    main()

# Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.

# Here's a sample run of the program where the name we've decided to return is Sophia (the autograder expects the returned name to be Sophia):

# Howdy Sophia ! 🤠


def main():
    get_name = "Aleeza"
    print("Here", get_name, "😩")


if __name__ == "__main__":
    main()


def is_odd(value: int):
    remainder = value % 2
    return remainder == 1


def main():
    for i in range(10, 20):  # Updated range to start at 10 and end at 19
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")


if __name__ == "__main__":
    main()

# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):


# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12
def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)


def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


if __name__ == "__main__":
    main()


def print_multiple(message: str, repeats: int):
    for _ in range(repeats):
        print(message)


def main():

    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))

    print_multiple(message, repeats)


if __name__ == "__main__":
    main()


def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print(
            "Invalid part of speech. Please enter 0 for noun, 1 for verb, or 2 for adjective."
        )


def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(
        input(
            "Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "
        )
    )
    make_sentence(word, part_of_speech)


if __name__ == "__main__":
    main()
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):


# Enter a number: 42 The ones digit is 2
def print_ones_digit(num: int):
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")


def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)


if __name__ == "__main__":
    main()
