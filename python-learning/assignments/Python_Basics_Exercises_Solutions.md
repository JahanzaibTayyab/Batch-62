# Python Basics Exercises - Solutions

## 1. Simple Message

**Task:**  
Assign a message to a variable and then print that message.

**Solution:**

```python
# Step 1: Assign a message to a variable
message = "Hello, this is my first Python program!"

# Step 2: Print the message
print(message)
```

**Explanation:**  
In this exercise, we create a variable called `message` and assign a string value to it. We then use the `print()` function to display the content of the variable.

---

## 2. Simple Messages

**Task:**

- Assign a message to a variable and print that message.
- Change the value of the variable to a new message, and print the new message.

**Solution:**

```python
# Step 1: Assign a message to a variable
message = "This is the first message."

# Step 2: Print the message
print(message)

# Step 3: Change the value of the variable to a new message
message = "This is the second message."

# Step 4: Print the new message
print(message)
```

**Explanation:**  
We first assign a message to the `message` variable and print it. Then, we change the value of `message` to a new string and print it again. This demonstrates how variables can hold different values over time.

---

## 3. Personal Message

**Task:**

- Use a variable to represent a person’s name.
- Print a message to that person, such as, “Hello Eric, would you like to learn some Python today?”

**Solution:**

```python
# Step 1: Assign a name to a variable
name = "Eric"

# Step 2: Print a personalized message using the name
print(f"Hello {name}, would you like to learn some Python today?")
```

**Explanation:**  
Here, we use a variable `name` to store a person's name. We then use an f-string (formatted string) to insert the value of `name` into a message that we print.

---

## 4. Name Cases

**Task:**

- Use a variable to represent a person’s name.
- Print the person’s name in lowercase, uppercase, and title case.

**Solution:**

```python
# Step 1: Assign a name to a variable
name = "Eric"

# Step 2: Print the name in lowercase
print(name.lower())

# Step 3: Print the name in uppercase
print(name.upper())

# Step 4: Print the name in title case
print(name.title())
```

**Explanation:**  
In this exercise, we manipulate the string stored in the `name` variable by converting it to different cases using `lower()`, `upper()`, and `title()` methods.

---

## 5. Famous Quote

**Task:**

- Find a quote from a famous person you admire.
- Print the quote and the name of its author.

**Solution:**

```python
# Step 1: Assign the quote and author to variables
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"

# Step 2: Print the quote and author
print(f'{author} once said, "{quote}"')
```

**Explanation:**  
We store the quote and its author in separate variables, `quote` and `author`, and then use an f-string to combine and print them in a formatted way.

---

## 6. Famous Quote 2

**Task:**

- Use a variable called `famous_person` to represent the famous person’s name.
- Compose the message and represent it with a variable called `message`.
- Print the message.

**Solution:**

```python
# Step 1: Assign the famous person's name to a variable
famous_person = "Albert Einstein"

# Step 2: Compose the message
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

# Step 3: Print the message
print(message)
```

**Explanation:**  
We use two variables, `famous_person` and `message`, to store the person's name and the complete quote. This shows how you can build more complex strings by combining variables.

---

## 7. Stripping Names

**Task:**

- Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
- Print the name once, so the whitespace around the name is displayed.
- Print the name using each of the three stripping functions: `lstrip()`, `rstrip()`, and `strip()`.

**Solution:**

```python
# Step 1: Assign a name with whitespace to a variable
name = " \t\n Eric \n\t "

# Step 2: Print the name with whitespace
print(f"Original name with whitespace: '{name}'")

# Step 3: Use lstrip() to remove leading whitespace
print(f"After lstrip(): '{name.lstrip()}'")

# Step 4: Use rstrip() to remove trailing whitespace
print(f"After rstrip(): '{name.rstrip()}'")

# Step 5: Use strip() to remove leading and trailing whitespace
print(f"After strip(): '{name.strip()}'")
```

**Explanation:**  
This exercise demonstrates how to use string methods to remove unwanted whitespace from the start (`lstrip()`), end (`rstrip()`), or both sides (`strip()`) of a string.

---

## 8. Variable Sum

**Task:**
Assign the values 5, 10, and 15 to three variables `x`, `y`, and `z`. Print their sum.

**Solution:**

```python
# Step 1: Assign values to variables
x = 5
y = 10
z = 15

# Step 2: Print the sum of the variables
print(x + y + z)
```

**Explanation:**  
We assign integers to the variables `x`, `y`, and `z`, and then use the `+` operator to sum them. The result is printed to the console.

---

## 9. Variable Swap

**Task:**
Swap the values of two variables `a` and `b`. Print the values before and after the swap.

**Solution:**

```python
# Step 1: Assign initial values to variables
a = 3
b = 7

# Step 2: Print the values before the swap
print(f"Before swap: a = {a}, b = {b}")

# Step 3: Swap the values
a, b = b, a

# Step 4: Print the values after the swap
print(f"After swap: a = {a}, b = {b}")
```

**Explanation:**  
This exercise shows how to swap the values of two variables using tuple unpacking in Python, which is a very concise and Pythonic way to perform this operation.

---

## 10. Favorite Color

**Task:**
Create a variable with your favorite color and print it. Then change the variable name to something else and print the color again.

**Solution:**

```python
# Step 1: Assign a favorite color to a variable
favorite_color = "blue"

# Step 2: Print the favorite color
print(favorite_color)

# Step 3: Change the variable name and print the color again
my_color = favorite_color
print(my_color)
```

**Explanation:**  
We first assign a color to the `favorite_color` variable, print it, and then assign the same value to a new variable `my_color` and print it again.

---

## 11. Changing Pet Name

**Task:**
Create a variable `pet_name` and set it to "Buddy". Change the value of `pet_name` to "Max" and print the new value.

**Solution:**

```python
# Step 1: Assign a pet name to a variable
pet_name = "Buddy"

# Step 2: Print the initial pet name
print(pet_name)

# Step 3: Change the pet name
pet_name = "Max"

# Step 4: Print the new pet name
print(pet_name)
```

**Explanation:**  
This exercise shows how variables can be reassigned to hold new values. Initially, `pet_name` holds `"Buddy"`, and then it is changed to `"Max"`.

---

## 12. Observing Name Error

**Task:**
Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a variable with a different name (like `sunsine`) and observe the error.

**Solution:**

```python
# Step 1: Assign a value to a variable
sunshine = "Sunshine"

# Step 2: Print the correct variable
print(sunshine)

# Step 3: Try to print a misspelled variable (This will cause an error)
print(sunsine)  # NameError: name 'sunsine' is not defined
```

**Explanation:**  
This exercise demonstrates what happens when you try to access a variable that hasn’t been defined. Python will raise a `NameError` because the variable `sunsine` does not exist.

---

## 13. Reassigning Score

**Task:**
Assign the value 100 to a variable `score` and print it. Then assign a new value to `score` and print it again.

**Solution:**

```python
# Step 1: Assign an initial score to a variable
score = 100

# Step 2: Print the initial score
print(score)

# Step 3:

 Reassign a new score to the variable
score = 85

# Step 4: Print the new score
print(score)
```

**Explanation:**  
We initially assign the value 100 to `score` and print it. The variable is then reassigned the value 85, demonstrating how variables can be updated with new values.

---

## 14. City Name

**Task:**
Create a string variable `city` and assign it the name of a city you like. Print the city name.

**Solution:**

```python
# Step 1: Assign a city name to a variable
city = "Paris"

# Step 2: Print the city name
print(city)
```

**Explanation:**  
This is a simple exercise where you assign a city name to the `city` variable and print it. It demonstrates the basics of string assignment and output.

---

## 15. Title Case Text

**Task:**
Create a variable `text` with the value "python programming" and print it in title case.

**Solution:**

```python
# Step 1: Assign text to a variable
text = "python programming"

# Step 2: Print the text in title case
print(text.title())
```

**Explanation:**  
The `title()` method converts the first letter of each word to uppercase, showing how you can manipulate strings in Python.

---

## 16. Lowercase Conversion

**Task:**
Assign a string with mixed cases to a variable and print it in all lowercase letters.

**Solution:**

```python
# Step 1: Assign mixed-case text to a variable
mixed_text = "PyThOn PrOgRaMmInG"

# Step 2: Print the text in lowercase
print(mixed_text.lower())
```

**Explanation:**  
The `lower()` method converts all characters in the string to lowercase. This is useful for standardizing text input.

---

## 17. Uppercase Conversion

**Task:**
Assign a string with mixed cases to a variable and print it in all uppercase letters.

**Solution:**

```python
# Step 1: Assign mixed-case text to a variable
mixed_text = "PyThOn PrOgRaMmInG"

# Step 2: Print the text in uppercase
print(mixed_text.upper())
```

**Explanation:**  
The `upper()` method converts all characters in the string to uppercase. This is the opposite of the `lower()` method.

---

## 18. Current Temperature

**Task:**
Create a variable `temperature` with the value 25. Print "The current temperature is [temperature] degrees." using the variable.

**Solution:**

```python
# Step 1: Assign a temperature value to a variable
temperature = 25

# Step 2: Print a message with the temperature
print(f"The current temperature is {temperature} degrees.")
```

**Explanation:**  
This exercise demonstrates how to include variable values within a string using an f-string. The temperature value is dynamically inserted into the message.

---

## 19. Printing a Poem

**Task:**
Create a variable `poem` with a short poem that has multiple lines. Print the poem with each line starting on a new line.

**Solution:**

```python
# Step 1: Assign a multi-line poem to a variable
poem = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""

# Step 2: Print the poem
print(poem)
```

**Explanation:**  
The `"""` triple quotes are used to store multi-line strings in Python. When printed, each line starts on a new line, preserving the original formatting of the poem.
