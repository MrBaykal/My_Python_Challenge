# Coding Challenge 004 : Validate Combination of Brackets

Purpose of the this coding challenge is to solve a combination problem using loops.

## Learning Outcomes

At the end of the this coding challenge, students will be able to;

- understand the use of loops.
- solve the advanced and complicated problems.
- understand the importance of pattern recognition.
- get a better understanding in manipulating lists or strings.

## Problem Statement
  
- Write a function that given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determines if the input string is valid or not by using following rules.

- An input string is valid if:

  - Open brackets must be closed by the same type of brackets.

  - Open brackets must be closed in the correct order.

- Note that an empty string is also considered valid.

- Example for user inputs and respective outputs

```text
Input           Output
------------    ------
"()"            true
"()[]{}"        true
"(]"            false
"([)]"          false
"{[]}"          true
""              true
```

# Here is the solution: 


def is_valid_brackets(string):
  """
  Determines if the given string is valid.

  Args:
    string: The string to check.

  Returns:
    True if the string is valid, False otherwise.
  """

  # Create a stack to store the opening brackets.
  stack = []

  # Iterate over the string.
  for char in string:
    # If the character is an opening bracket, push it onto the stack.
    if char in ["(", "{", "["]:
      stack.append(char)

    # If the character is a closing bracket, pop the top element from the stack.
    else:
      # If the stack is empty, the string is invalid.
      if not stack:
        return False

      # If the top element of the stack does not match the closing bracket, the string is invalid.
      top_element = stack.pop()
      if (top_element == "(" and char != ")") or (top_element == "{" and char != "}") or (top_element == "[" and char != "]"):
        return False

  # If the stack is not empty, the string is invalid.
  return not stack