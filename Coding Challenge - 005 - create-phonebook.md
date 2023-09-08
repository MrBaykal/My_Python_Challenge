# Coding Challenge - 005 : Create Phonebook Application

Purpose of the this coding challenge is to write a program that creates a phonebook and performs certain operations on the phonebook.

## Learning Outcomes

At the end of the this coding challenge, students will be able to;

- analyze a problem, identify and apply programming knowledge for appropriate solution.

- design, implement `for` and `while` loops effectively in Python to solve the given problem.

- control loops effectively by using `if` and `control` statements.

- demonstrate their knowledge of algorithmic design principles by using function effectively.

- apply exception handling to handle errors effectively.

## Problem Statement

- Write a program that creates a phonebook, adds requested contacts to the phonebook, finds them, and removes them.

- There should be 4 options available to the user and from the options, users should be able to add, find, delete contacts, or terminate the program as shown below.

- Phonebook has users and their corresponding phone numbers.

- At the beginning of the program the phonebook will be empty and user can choose to add new contacts to the phonebook.

- Program should ask user for the input, after giving information text shown as below.

```text
Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) :
```

- Application should be case sensitive and run until the user types `4`.

- Example for user inputs and respective outputs

```text
Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 2
Insert name of the person : John
Insert phone number of the person: ten
Invalid input format, cancelling operation ...

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 2
Insert name of the person : Alex
Insert phone number of the person: 1234
Phone number of Alex is inserted into the phonebook

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 1
Find the phone number of : Alex
1234

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 3
Whom to delete from phonebook : Alex
Alex is deleted from the phonebook

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 1
Find the phone number of : Alex
Couldn't find phone number of Alex

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 4
Exiting Phonebook
```

# Here is the Solution

# Define an empty phonebook as a dictionary to store contacts and their phone numbers
phonebook = {}

# Function to add a new contact to the phonebook
def insert_contact():
    name = input("Insert name of the person: ")
    phone = input("Insert phone number of the person: ")
    
    # Check if the phone number contains only digits
    if phone.isdigit():
        phonebook[name] = phone
        print(f"Phone number of {name} is inserted into the phonebook")
    else:
        print("Invalid input format, cancelling operation ...")

# Function to find a contact's phone number
def find_contact():
    name = input("Find the phone number of: ")
    if name in phonebook:
        print(phonebook[name])
    else:
        print(f"Couldn't find phone number of {name}")

# Function to delete a contact from the phonebook
def delete_contact():
    name = input("Whom to delete from phonebook: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} is deleted from the phonebook")
    else:
        print(f"Couldn't find {name} in the phonebook")

# Main loop to display the menu and handle user input
while True:
    print("\nWelcome to the phonebook application")
    print("1. Find phone number")
    print("2. Insert a phone number")
    print("3. Delete a person from the phonebook")
    print("4. Terminate")
    
    choice = input("Select operation on Phonebook App (1/2/3/4): ")
    
    if choice == "1":
        find_contact()
    elif choice == "2":
        insert_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        print("Exiting Phonebook")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
