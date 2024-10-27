---
# Python Basics Quiz

This quiz assesses fundamental and intermediate knowledge in Python, focusing on basic syntax, data types, control structures, and introductory concepts in the NumPy and Pandas libraries.

## Section 1: General Python Basics (25 Questions)

1. **What is the output of the following code?**
   ```python
   print(type(3.14))
   ```
   - a) `int`
   - b) `float`
   - c) `str`
   - d) `complex`

2. **What will the following code output?**
   ```python
   my_list = [1, 2, 3, 4]
   print(my_list[1])
   ```
   - a) `1`
   - b) `2`
   - c) `3`
   - d) `4`

3. **Which of the following is used to create a function in Python?**
   - a) `def`
   - b) `function`
   - c) `func`
   - d) `lambda`

4. **What is the output of this code?**
   ```python
   x = 5
   x += 3
   print(x)
   ```
   - a) `5`
   - b) `3`
   - c) `8`
   - d) `15`

5. **Which of the following is not a valid variable name in Python?**
   - a) `variable_name`
   - b) `2variable`
   - c) `variable2`
   - d) `var_name`

6. **What does the `range(5)` function return?**
   - a) `[1, 2, 3, 4, 5]`
   - b) `[0, 1, 2, 3, 4]`
   - c) `[0, 1, 2, 3, 4, 5]`
   - d) `[1, 2, 3, 4]`

7. **Which data type is mutable in Python?**
   - a) `tuple`
   - b) `int`
   - c) `list`
   - d) `string`

8. **What does the `len()` function return?**
   - a) The maximum value of a list
   - b) The number of elements in a list
   - c) The minimum value of a list
   - d) The sum of elements in a list

9. **Which of the following methods can add an item to the end of a list?**
    - a) `list.append(item)`
    - b) `list.insert(item)`
    - c) `list.pop()`
    - d) `list.remove(item)`

10. **What will `print(5 / 2)` output?**
    - a) `2.5`
    - b) `2`
    - c) `3`
    - d) `None`

11. **Which of these is a logical operator in Python?**
    - a) `and`
    - b) `or`
    - c) `not`
    - d) All of the above

12. **What is the result of the following code?**
    ```python
    x = 5
    y = 2
    print(x // y)
    ```
    - a) `2`
    - b) `2.5`
    - c) `0`
    - d) `1`

13. **How do you write an inline conditional expression in Python?**
    - a) `if-else`
    - b) `x if condition else y`
    - c) `condition ? x : y`
    - d) `if condition: x else: y`

14. **Which statement is used to exit a loop in Python?**
    - a) `exit`
    - b) `break`
    - c) `continue`
    - d) `pass`

15. **What will `print("hello".upper())` output?**
    - a) `Hello`
    - b) `HELLO`
    - c) `hello`
    - d) `SyntaxError`

16. **What is a dictionary in Python?**
    - a) A list of values
    - b) A collection of key-value pairs
    - c) A mutable list
    - d) A set of unique values

17. **What does the `is` keyword check in Python?**
    - a) Value equality
    - b) Type compatibility
    - c) Reference equality (identity)
    - d) Membership

18. **What will `my_dict.get("key", "default")` return if "key" does not exist?**
    - a) `None`
    - b) `"default"`
    - c) `Error`
    - d) `0`

19. **Which function converts a string into a list of characters?**
    - a) `list()`
    - b) `str()`
    - c) `split()`
    - d) `slice()`

20. **What will `range(10, 1, -2)` produce?**
    - a) `10, 9, 8, 7, 6, 5, 4, 3, 2, 1`
    - b) `[10, 8, 6, 4, 2]`
    - c) `[10, 9, 8, 7, 6, 5, 4, 3, 2]`
    - d) `SyntaxError`

21. **What does the `enumerate()` function do?**
    - a) Iterates over a list and counts each element
    - b) Returns an iterator with index-element pairs
    - c) Joins a list into a string
    - d) Iterates only over strings

22. **How do you read input from a user in Python 3?**
    - a) `get()`
    - b) `read()`
    - c) `input()`
    - d) `fetch()`

23. **What will the following code print?**
    ```python
    x = "5" + "3"
    print(x)
    ```
    - a) `8`
    - b) `53`
    - c) `Error`
    - d) `5 3`

24. **How do you check if `5` is in a list `my_list`?**
    - a) `my_list.contains(5)`
    - b) `5 in my_list`
    - c) `5 not in my_list`
    - d) `contains(my_list, 5)`

25. **What will `type([]) == list` return?**
    - a) `True`
    - b) `False`
    - c) `TypeError`
    - d) `None`

---

## Section 2: NumPy Basics (15 Questions)

26. **Which command imports the NumPy library with the alias `np`?**
    - a) `import numpy as np`
    - b) `import numpy`
    - c) `from numpy import np`
    - d) `import numpy as numpy`

27. **How do you create a 4x4 identity matrix in NumPy?**
    - a) `np.ones((4, 4))`
    - b) `np.zeros((4, 4))`
    - c) `np.identity(4)`
    - d) `np.eye(4, 4)`

28. **What will be the shape of an array created by `np.arange(16).reshape(4, 4)`?**
    - a) `(4, 4)`
    - b) `(8, 2)`
    - c) `(2, 8)`
    - d) `(16,)`

29. **Which function would you use to calculate the standard deviation of a NumPy array?**
    - a) `np.median()`
    - b) `np.std()`
    - c) `np.var()`
    - d) `np.sum()`

30. **How would you horizontally stack two arrays `a` and `b`?**
    - a) `np.vstack((a, b))`
    - b) `np.hstack((a, b))`
    - c) `np.column_stack(a, b)`
    - d) `np.row_stack((a, b))`

31. **Which function will generate an array of 5 random floats between 0 and 1?**
    - a) `np.rand(5)`
    - b) `np.random.rand(5)`
    - c) `np.random.uniform(5)`
    - d) `np.random.random(5)`

32. **How do you set a random seed in NumPy for reproducibility?**
    - a) `np.seed()`
    - b) `np.set_seed()`
    - c) `np.random.seed()`
    - d) `np.random.set_seed()`

33. **What will `np.dot(a, b)` do if `a` and `b` are 1D arrays?**
    - a) Element-wise multiplication
    - b) Matrix multiplication
    - c) Dot product
    - d) Returns a 2D array

34. **How do you extract elements in an array `arr` that are greater than 5?**


    - a) `arr[arr > 5]`
    - b) `np.greater(arr, 5)`
    - c) `np.where(arr > 5)`
    - d) All of the above

35. **How do you create an array from a list `[1, 2, 3]` in NumPy?**
    - a) `np.array([1, 2, 3])`
    - b) `np.list([1, 2, 3])`
    - c) `np.arr([1, 2, 3])`
    - d) `np.array([1, 2, 3], dtype=int)`

36. **How do you find the maximum value in a NumPy array `arr`?**
    - a) `arr.max()`
    - b) `np.maximum(arr)`
    - c) `np.max(arr)`
    - d) Both a and c

37. **Which function adds all elements in an array `arr`?**
    - a) `sum(arr)`
    - b) `np.add(arr)`
    - c) `np.sum(arr)`
    - d) `arr.sum_all()`

38. **What does `np.full((2, 2), 7)` produce?**
    - a) A 2x2 matrix with sevens
    - b) An array with 4 sevens
    - c) An error
    - d) A 1D array with two sevens

39. **How would you reshape a 1D array of length 9 to a 3x3 matrix?**
    - a) `arr.shape = (3, 3)`
    - b) `np.reshape(arr, (3, 3))`
    - c) `arr.reshape(3, 3)`
    - d) All of the above

40. **How would you find unique elements in a NumPy array?**
    - a) `np.find_unique(arr)`
    - b) `np.unique(arr)`
    - c) `arr.unique()`
    - d) `np.elements(arr)`

---

## Section 3: Pandas Basics (10 Questions)

41. **How do you import the Pandas library with the alias `pd`?**
    - a) `import pandas`
    - b) `import pandas as pd`
    - c) `import pd as pandas`
    - d) `from pandas import pd`

42. **How can you read a CSV file into a Pandas DataFrame?**
    - a) `pd.read_csv("file.csv")`
    - b) `pd.load_csv("file.csv")`
    - c) `pd.readfile("file.csv")`
    - d) `pd.open_csv("file.csv")`

43. **Which function displays the first five rows of a DataFrame?**
    - a) `df.start()`
    - b) `df.first()`
    - c) `df.head()`
    - d) `df.top()`

44. **How do you select a column named "age" from a DataFrame `df`?**
    - a) `df.age()`
    - b) `df["age"]`
    - c) `df[age]`
    - d) `df.age`

45. **What does `df.describe()` return?**
    - a) A summary of all column names
    - b) Descriptive statistics of numerical columns
    - c) A list of all categorical values
    - d) A DataFrame without missing values

46. **Which method fills missing values in a DataFrame?**
    - a) `df.replace()`
    - b) `df.fillna()`
    - c) `df.fill()`
    - d) `df.missing()`

47. **How do you filter rows in a DataFrame where a column "age" is greater than 30?**
    - a) `df["age"] > 30`
    - b) `df.loc[df["age"] > 30]`
    - c) `df.where("age" > 30)`
    - d) `df.filter("age" > 30)`

48. **How do you add a new column to a DataFrame?**
    - a) `df.add_column("new_column", values)`
    - b) `df["new_column"] = values`
    - c) `df.insert_column(values)`
    - d) `df.create("new_column", values)`

49. **Which method removes duplicate rows in a DataFrame?**
    - a) `df.drop_duplicates()`
    - b) `df.unique()`
    - c) `df.remove_duplicates()`
    - d) `df.drop()`

50. **How do you get the mean of a column "age" in a DataFrame `df`?**
    - a) `df["age"].average()`
    - b) `df["age"].mean()`
    - c) `df.mean("age")`
    - d) `df.age.mean()`
