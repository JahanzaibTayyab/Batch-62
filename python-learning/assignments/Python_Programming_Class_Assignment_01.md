### Assignment: Python Programming Assignment 02

### Instructions:

Implement Python programs to accomplish the following tasks using basic Python concepts. Each task comes with a brief description and example to help you understand what is required.

---

## **Task 1: Add Two Numbers**

### **Objective:**

Write a Python program that takes two integer inputs from the user, calculates their sum, and prints the result.

### **Code:**

```python
# Prompt the user for two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum
total_sum = num1 + num2

# Print the result
print("The sum of", num1, "and", num2, "is", total_sum)
```

---

## **Task 2: Agreement Boot**

### **Objective:**

Write a Python program that asks the user for their favorite animal and responds with, "My favorite animal is also [user's favorite animal]!"

### **Code:**

```python
# Prompt the user for their favorite animal
animal = input("What's your favorite animal? ")

# Print the response
print("My favorite animal is also", animal + "!")
```

---

## **Task 3: Fahrenheit to Celsius**

### **Objective:**

Write a Python program to convert a temperature from Fahrenheit to Celsius using the formula:  
**degrees_celsius = (degrees_fahrenheit - 32) \* 5.0/9.0**

### **Code:**

```python
# Prompt the user for a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5.0/9.0

# Print the result
print(f"Temperature: {fahrenheit}F = {celsius}C")
```

---

## **Task 4: Triangle Perimeters**

### **Objective:**

Prompt the user to enter the lengths of three sides of a triangle and then calculate and print the perimeter of the triangle.

### **Code:**

```python
# Prompt the user for the lengths of the three sides
side1 = float(input("What is the length of side 1? "))
side2 = float(input("What is the length of side 2? "))
side3 = float(input("What is the length of side 3? "))

# Calculate the perimeter
perimeter = side1 + side2 + side3

# Print the perimeter
print("The perimeter of the triangle is", perimeter)
```

---

## **Task 5: Square Number**

### **Objective:**

Ask the user for a number and print its square.

### **Code:**

```python
# Prompt the user for a number
num = float(input("Type a number to see its square: "))

# Calculate the square
square = num ** 2

# Print the square
print(f"{num} squared is {square}")
```

---

## **Task 6: Delete a Number from a List**

### **Objective:**

Use the list method to delete the number 3 from the list `numbers = [1, 2, 3, 4, 5]`.

### **Code:**

```python
# Initial list
numbers = [1, 2, 3, 4, 5]

# Remove the number 3
numbers.remove(3)

# Print the updated list
print(numbers)
```

---

## **Task 7: Creating a List**

### **Objective:**

Create a program that adds the elements of `list2` to `list1` using a list method.

### **Code:**

```python
# Initial lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Add elements of list2 to list1
list1.extend(list2)

# Print the updated list
print(list1)
```

---

## **Task 8: Pop Method**

### **Objective:**

Demonstrate the effect of the pop method on a list called `items = [10, 20, 30, 40]`.

### **Code:**

```python
# Initial list
items = [10, 20, 30, 40]

# Remove and print the last item using pop()
removed_item = items.pop()

# Print the updated list and the removed item
print("Updated list:", items)
print("Removed item:", removed_item)
```

---

## **Task 9: Index Method**

### **Objective:**

Find the index of `'green'` in the list `colors = ['red', 'blue', 'green', 'yellow']`.

### **Code:**

```python
# Initial list
colors = ['red', 'blue', 'green', 'yellow']

# Find and print the index of 'green'
index_of_green = colors.index('green')
print("The index of 'green' is", index_of_green)
```

---

## **Challenge 1: Get Last Element**

### **Objective:**

Write a function `get_last_element(lst)` to print the last element in a list.

### **Code:**

```python
def get_last_element(lst):
    # Print the last element
    print(lst[-1])

# Example usage
example_list = [1, 2, 3, 4]
get_last_element(example_list)
```

---

## **Challenge 2: Get a List from User Input**

### **Objective:**

Write a program which continuously asks the user to enter values into a list. When the user presses enter without typing anything, the list is printed.

### **Code:**

```python
# Initialize an empty list
user_list = []

while True:
    # Prompt the user to enter a value
    value = input("Enter a value: ")

    # If the input is empty, break the loop
    if value == "":
        break

    # Add the value to the list
    user_list.append(value)

# Print the final list
print("Here's the list:", user_list)
```

### **How to Run:**

1. Ensure that Python is installed on your machine.
2. Save each task as a separate Python file (e.g., `exercise_class_solutions_01.ipynb`).
3. Run each file using your Python environment or command line.

---
