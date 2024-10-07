# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random


def main():
    secret_number = random.randint(1, 99)
    chances = 3

    for attempt in range(chances):
        guess_number = int(input(f"Attempt {attempt + 1} - Enter your guess: "))

        if guess_number == secret_number:
            print(f"Congrats! You guessed the number {secret_number}.")
            break  # Exit the loop if the user guesses correctly
        elif guess_number < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        # After 3rd attempt
        if attempt == chances - 1:
            print(
                f"Sorry, you failed to guess. The correct number was {secret_number}."
            )


if __name__ == "__main__":
    main()
# Write a program to print terms in the Fibonacci sequence up to a maximum value.

# In the 13th century, the Italian mathematician Leonardo Fibonacci, as a way to explain the geometric growth of a population of rabbits, devised a mathematical sequence that now bears his name. The first two terms in this sequence, Fib(0) and Fib(1), are 0 and 1, and every subsequent term is the sum of the preceding two. Thus, the first several terms in the Fibonacci sequence look like this:

# Fib(0) = 0 Fib(1) = 1 Fib(2) = 1 = 0 + 1 Fib(3) = 2 = 1 + 1 Fib(4) = 3 = 1 + 2 Fib(5) = 5 = 2 + 3

# Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!). Thus, your program should produce the following sample run:
MAX_TERM_VALUE: int = 10000


def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


# There is no need to edit code beyond this point

if __name__ == "__main__":
    main()


# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
def main():
    for i in range(20):
        print(i * 2)


if __name__ == "__main__":
    main()
# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

# Note that you can call input() with no prompt and it will still wait for a user to type something!

AFFIRMATION = "I am worthy of success and happiness"


def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()
        print("That's right! :)")


if __name__ == "__main__":
    main()


# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
def main():
    for i in range(10, 0, -1):
        print(i, end=",")
        print("LiftOff")


if __name__ == "__main__":
    main()


# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
def main():
    current_number = int(input("Enter a number:"))
    while current_number < 100:
        current_number *= 2
        print(current_number)
        if current_number > 100:
            break


if __name__ == "__main__":
    main()
