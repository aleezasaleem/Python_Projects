# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
def get_user_number():
    user_list = []
    while True:
        user_input = input("Enter a number (or press Enter to stop): ")
        if user_input == "":  # Stop when the user presses Enter without typing anything
            break
        user_number = int(user_input)  # Convert the input to an integer
        user_list.append(user_number)  # Add the number to the list
    return user_list


def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict


def print_counts(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def main():
    user_numbers = get_user_number()  # Get the list of user numbers
    num_dict = count_nums(user_numbers)  # Count occurrences
    print_counts(num_dict)  # Print the results


# Python boilerplate.
if __name__ == "__main__":
    main()


# In this program we show an example of using dictionaries to keep track of information in a phonebook.
def read_phone_numbers():
    phonebook = {}
    while True:
        name = input("Enter name:")
        if name == "":
            break
        number = input("Enter number:")
        phonebook[name] = number
        return phonebook


def print_phonebook(phonebook):

    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == "__main__":
    main()
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.


# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
def main():
    fruits = {"apple": 1.5, "mango": 3, "banana": 8, "kiwi": 9, "orange": 6}
    total_cost = 0

    for fruit_name in fruits:
        while True:
            amount = input(f"How many {fruit_name}s do you want to buy? ")
            if amount.isdigit():  # Check if input is a valid number
                amount = int(amount)
                price = fruits[fruit_name]
                total_cost += price * amount
                break
            else:
                print("Please enter a valid number.")

    print(f"\nYour overall total is: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
from hashlib import sha256


def login(email, stored_logins, password_to_check):

    if stored_logins[email] == hash_password(password_to_check):
        return True

    return False


# There is no need to edit code beyond this point


def hash_password(password):

    return sha256(password.encode()).hexdigest()


def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb",
    }

    print(login("example@gmail.com", stored_logins, "word"))
    print(login("example@gmail.com", stored_logins, "password"))

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))
    print(login("code_in_placer@cip.org", stored_logins, "karel"))

    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "123!456?789"))


if __name__ == "__main__":
    main()
