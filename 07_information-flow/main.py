# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!


# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead
def is_adult(age):
    adult_age = 7
    if age <= adult_age:
        return True
    return False
    return age


def main():
    age = int(input("Enter your age: "))
    print(is_adult(age))


if __name__ == "__main__":
    main()
# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Here's a sample run of the program (user input in bold italics):

# What's your name? Sophia


# Greetings Sophia!
def main():
    name = str(input("What's your name?"))
    print(f"Greetings {name}")


if __name__ == "__main__":
    main()
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def in_range(n, low, high):

    if n >= low and n <= high:
        return True

    return False


result = in_range(5, 1, 10)
print(result)

# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.


def fruit_in_stock(fruit):
    if fruit == "apple":
        return 4
    if fruit == "mango":
        return 7
    if fruit == "banana":
        return 2
    if fruit == "watermelon":
        return 9
    else:
        return 0


def main():
    enter_fruit = str(input("Enter a fruit:"))
    stock = fruit_in_stock(enter_fruit)
    if stock == 0:
        print("There is no fruit in stock!")
    else:
        print("This fruit is in stock! Here is how many:")
    print(stock)


if __name__ == "__main__":
    main()

# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable

# Asks the user for their last name and stores it in a variable

# Asks the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked

# You can return multiple pieces of data by separating each piece with a comma in the return line


def get_user_info():
    first_name = str(input("What's your first name?:"))
    last_name = str(input("What's your last name?:"))
    email_address = str(input("What's youremail address?:"))
    return first_name, last_name, email_address


def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)


if __name__ == "__main__":
    main()

# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture


def main():
    num: int = 7
    num = subtract_seven(num)
    print("this should be zero: ", num)


def subtract_seven(num):
    num = num - 7
    return num


if __name__ == "__main__":
    main()
