````markdown
# Python List Exercises

This repository contains solutions for basic Python list exercises without using loops. These exercises are ideal for beginner Python students who are just starting to learn about lists and basic Python functions.

## Exercise 3-1: Names

**Task:**  
Store the names of a few of your friends in a list called `names`. Print each person’s name by accessing each element in the list, one at a time.

```python
names = ["Arslan", "Tooba", "Mubbara", "Ayesha","Kamran","Esha"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
```
````

## Exercise 3-2: Greetings

**Task:**  
Start with the list you used in Exercise 3-1. Instead of just printing each person’s name, print a message to them. The text of each message should be the same, but personalized with the person’s name.

```python
names = ["Ali", "Sara", "Ahmed", "Ayesha"]

print("Hello, " + names[0] + "! How are you?")
print("Hello, " + names[1] + "! How are you?")
print("Hello, " + names[2] + "! How are you?")
print("Hello, " + names[3] + "! How are you?")
```

## Exercise 3-3: Your Own List

**Task:**  
Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items.

```python
modes_of_transport = ["Honda motorcycle", "Toyota car", "Bicycle"]

print("I would like to own a " + modes_of_transport[0] + ".")
print("I would like to own a " + modes_of_transport[1] + ".")
print("I would like to own a " + modes_of_transport[2] + ".")
```

## Exercise 3-4: Guest List

**Task:**  
If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner.

```python
guest_list = ["Arslan", "Kamran", "Ali"]

print("Dear " + guest_list[0] + ", you are invited to dinner.")
print("Dear " + guest_list[1] + ", you are invited to dinner.")
print("Dear " + guest_list[2] + ", you are invited to dinner.")
```

## Exercise 3-5: Changing Guest List

**Task:**  
Start with your program from Exercise 3-4. Add a print statement indicating a guest who can’t make it. Modify your list and replace the guest with a new one.

```python
guest_list = ["Arslan", "Kamran", "Ali"]

print(guest_list[0] + " can't make it to dinner.")

guest_list[0] = "Mubbara"

print("Dear " + guest_list[0] + ", you are invited to dinner.")
print("Dear " + guest_list[1] + ", you are invited to dinner.")
print("Dear " + guest_list[2] + ", you are invited to dinner.")
```

## Exercise 3-6: More Guests

**Task:**  
Inform people that you found a bigger table and invite more guests. Add a new guest to the beginning, middle, and end of your list.

```python
guest_list = ["Arslan", "Kamran", "Ali"]

print("I found a bigger table for dinner!")

guest_list.insert(0, "Tooba")
guest_list.insert(2, "Esha")
guest_list.append("Arham")

print("Dear " + guest_list[0] + ", you are invited to dinner.")
print("Dear " + guest_list[1] + ", you are invited to dinner.")
print("Dear " + guest_list[2] + ", you are invited to dinner.")
print("Dear " + guest_list[3] + ", you are invited to dinner.")
print("Dear " + guest_list[4] + ", you are invited to dinner.")
print("Dear " + guest_list[5] + ", you are invited to dinner.")
```

## Exercise 3-7: Shrinking Guest List

**Task:**  
Inform people that you can only invite two guests for dinner. Remove guests one by one using `pop()` and apologize.

```python
guest_list = ["Arslan", "Ali", "Ayesha", "Kamran", "Mubbara", "Tooba"]

print("I can only invite two people for dinner.")

removed_guest = guest_list.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

removed_guest = guest_list.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

removed_guest = guest_list.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

removed_guest = guest_list.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

print("Dear " + guest_list[0] + ", you are still invited to dinner.")
print("Dear " + guest_list[1] + ", you are still invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)  # Empty list check
```

## Exercise 3-8: Seeing the World

**Task:**  
List five places you want to visit and manipulate the list using sorting and reversing functions.

```python
places = ["Paris", "Tokyo", "New York", "Sydney", "Cairo"]

print(places)  # Original order

print(sorted(places))  # Alphabetical order

print(places)  # Check original order is unchanged

print(sorted(places, reverse=True))  # Reverse alphabetical order

places.reverse()  # Reverse the list
print(places)

places.reverse()  # Reverse it back to original order
print(places)

places.sort()  # Sort alphabetically
print(places)

places.sort(reverse=True)  # Sort in reverse alphabetical order
print(places)
```

## Exercise 3-9: Every Function

**Task:**  
Create a list of items and use various list functions like `sorted()`, `reverse()`, `append()`, etc.

```python
rivers = ["Nile", "Amazon", "Yangtze", "Mississippi", "Danube"]

print(rivers)  # Original list

print(sorted(rivers))  # Sorted list

print(len(rivers))  # Length of the list

rivers.append("Thames")  # Add a new item
print(rivers)

rivers.reverse()  # Reverse the list
print(rivers)

rivers.sort()  # Sort alphabetically
print(rivers)

rivers.pop()  # Remove last item
print(rivers)
```

## Exercise 3-10: Intentional Error

**Task:**  
Cause an intentional index error by trying to access an invalid index.

```python
mountains = ["Everest", "K2", "Kangchenjunga"]

print(mountains[3])  # This will cause an IndexError
```

## How to Run

1. Ensure you have Python installed on your system.
2. Save each exercise as a separate Python file (e.g., `exercise_list_solutions.ipynb`).
3. Run each file in the terminal or a Python environment to see the results.

Happy coding!
