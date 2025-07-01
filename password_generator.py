from string import ascii_letters, digits
from random import choice

l_digits = []
for i in digits:
    l_digits.append(i)

l_letters = []
for j in ascii_letters:
    l_letters.append(j)

l_mix = []
for k in l_digits + l_letters:
    l_mix.append(k)

name = input("Please enter your name: ")

print(f"Hello, {name}! Let's generate a password for you. \n")
print("You can choose from the following options:")
print("1. Password with only numbers")
print("2. Password with only letters")
print("3. Password with letters and numbers \n")

option = input("Enter your choice (1, 2, or 3): ")
length = int(input("Enter the length of the password: "))
password = ""

if option == '1':
    while True:
        for _ in range(length):
            password += choice(l_digits)
        print(f"Your password is: {password}")
        new = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if new == 'yes':
            password = ""
        else:
            print("Thank you for using the password generator. Goodbye!")
            break

elif option == '2':
    while True:
        for _ in range(length):
            password += choice(l_letters)
        print(f"Your password is: {password}")
        new = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if new == 'yes':
            password = ""
        else:
            print("Thank you for using the password generator. Goodbye!")
            break

elif option == '3':
    while True:
        for _ in range(length):
            password += choice(l_mix)
        print(f"Your password is: {password}")
        new = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if new == 'yes':
            password = ""
        else:
            print("Thank you for using the password generator. Goodbye!")
            break

else:
    print("Invalid choice. Please run the program again and select a valid option.")
    exit()