# Coding Challenge 003 : Find the Largest Number

Purpose of the this coding challenge is to solve a simple sorting problem in Python.

## Learning Outcomes

At the end of the this coding challenge, students will be able to;

- get a basic understanding of sorting algorithms.
- demonstrate their knowledge of lists in python
- implement loops to solve the problems in python
- get a better understanding of computational thinking concepts

## Problem Statement
  
- Write a python code that finds the largest number among the 5 numbers given by the user as input.

- It is forbidden to use max() function.  

- Indicate which computational thinking concepts have you used.

- Example for user inputs and respective outputs

```text
Input            Output
------------     ------
1 2 3 4 5         5
67 85 19 39       85
```

# Here is Solution 1
count=0
array=[]
while count < 5:
  number= int(input('Please enter the number: '))
  array.append(number)
  count = count +1
def findLargestNum(nums):
  largest = nums[0]
  for i in nums:
    if i > largest:
      largest = i
  return largest
print(findLargestNum(array))

# Here is Solution 2

num_list =list(num for num in input("Enter five numbers separated by space ").strip().split())


if len(num_list) < 5:
    print ("You should enter", 5-len(num_list), "more number(s)")

elif len(num_list) > 5:
    print ("You entered", len(num_list)-5, "more number(s) than 5")



elif len(num_list) == 5:
    
    for i in range (len(num_list)):
        max_num = num_list[i]
        if not num_list[i].isnumeric():
            
            print(num_list[i], " is not a number")
        #else:
            num_list[i]= float(num_list[i])
        
    
    for i in range (len(num_list)):    
        
        if num_list[i] > max_num:
            max_num = num_list[i]
    print(max_num)

# Here is solution 3 

# Taking input from the user
numbers = input("Enter 5 numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Converting input from strings to integers

# Initializing the largest with the first number
largest = numbers[0]

# Looping through the list to find the largest number
for num in numbers:
    if num > largest:
        largest = num

# Printing the largest number
print("The largest number is:", largest)
