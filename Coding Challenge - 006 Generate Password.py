# Coding Challenge - 006: Generate Password

The purpose of this coding challenge is to write a program that creates a random password from a given full name.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

- Implement conditional statements effectively to solve a problem.

- Implement loops to solve a problem.

- Execute operations on strings.

- Make use of random numbers to solve a problem.

- Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

Write a Python program that prompts the user to enter his/her full name (without any spaces) and then creates a secret password consisting of three letters (in lowercase) randomly picked up from his/her full name, and a random four-digit number. For example, if the user enters "JackClarusway", a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250".

- Expected Output:

```text
Please enter your full name: StephenClarkson
rto8807

Please enter your full name: BillJames
ils6032

Please enter your full name: MarkJackson
jkr7034

Please enter your full name: CarlSmith
iih7800
```

# Here is the Lösung

import random

def generate_password(full_name):
    # Convert the full name to lowercase
    full_name = full_name.lower()

    # Initialize an empty list to store the three letters
    letters = []

    # Choose three random letters from the full name
    while len(letters) < 3:
        random_index = random.randint(0, len(full_name) - 1)
        letter = full_name[random_index]
        if letter.isalpha() and letter not in letters:
            letters.append(letter)

    # Generate a random four-digit number
    random_number = random.randint(1000, 9999)

    # Combine the three letters and the random number to create the password
    password = ''.join(letters) + str(random_number)

    return password

# Get the user's full name as input
full_name = input("Please enter your full name: ")

# Generate and print the password
password = generate_password(full_name)
print(password)