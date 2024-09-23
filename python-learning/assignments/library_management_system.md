# 📚 Python Library Management System Assignment

## 💡 Assignment Overview

This assignment is designed to help you apply the Python concepts learned in Chapters 1 to 7 of the _Python Crash Course, 3rd Edition_ by Eric Matthes. You will create a simple library management system that simulates basic operations such as storing book information, managing user data, borrowing and returning books, and searching for books.

## 📝 Scenario

You are tasked with developing a **Library Management System** for a small community library. This system will allow the library staff to manage books and user information efficiently. The system should include functionalities like viewing books, borrowing and returning books, and searching for books by title, author, or genre.

## 🎯 Assignment Requirements

### 1. **Store Book Information**

- Create a collection of books, each with a unique ID, title, author, genre, and availability status (e.g., "Available" or "Checked Out").
- Use dictionaries to represent each book and lists to store all the books.

### 2. **User Management**

- Create a list of users, each with a unique ID, name, and a list of books they have borrowed.
- Ensure that users can borrow and return books using their unique IDs.

### 3. **Borrowing and Returning Books**

- Allow users to borrow a book if it is available. Update the book's status to "Checked Out" and add it to the user's list of borrowed books.
- Implement a function for users to return books. Update the book's status to "Available" and remove it from the user's borrowed list.

### 4. **Search Functionality**

- Implement a search feature that allows users to find books by title, author, or genre.
- Display a list of books that match the search criteria, along with their current availability status.

### 5. **View Books by Status**

- Create separate functions to view:
  - All books in the library.
  - Only available books.
  - Only checked-out books.

### 6. **User Input and Interaction**

- Create a menu-driven interface that allows users to navigate through the system.
- Use `input()` and while loops to keep the program running until the user decides to exit.

## 🛠️ Step-by-Step Guide

### Step 1: Setting Up Data Structures

- Create lists to hold book and user data.
- Each book should have attributes like `ID`, `title`, `author`, `genre`, and `status`.
- Each user should have attributes like `ID`, `name`, and a list of borrowed books.

### Step 2: Creating the Main Menu

- Create a while loop that shows the main menu and prompts the user to choose an option.
- Use `if-elif` statements to perform actions based on the user's choice (e.g., view books, borrow a book).

### Step 3: Implementing Book and User Functions

- **Books:**
  - Create functions to add books, search for books, and display books based on their status.
- **Users:**
  - Create functions to add users and display user information.

### Step 4: Borrowing and Returning Books

- Create a function that checks if a book is available before allowing a user to borrow it.
- Create a function to return a book and update the user and book data accordingly.

### Step 5: Search Functionality

- Create a function that searches for books based on user input (title, author, or genre).
- Use a loop to display matching books and their status.

### Step 6: Display Books by Status

- Implement functions to display all books, only available books, or only checked-out books.

### Step 7: Error Handling and Validation

- Validate user inputs (e.g., check if the book ID exists before borrowing).
- Use loops and conditional statements to handle invalid inputs gracefully.

## 🧩 Hints and Tips

1. **Use Dictionaries for Complex Data:**

   - Use a dictionary for each book and user to store their details.

2. **Implement Functions for Each Task:**

   - Create separate functions for tasks like adding a book, borrowing a book, or searching for books to keep the code organized.

3. **Use Loops for Repeated Actions:**

   - Use `while` loops to keep the program running until the user decides to exit.

4. **Validate Inputs:**
   - Check if inputs like book IDs and user IDs are valid before performing any action.

## 📊 Example Output

```plaintext
Welcome to the Community Library System!
----------------------------------------
Please choose an option:
1. View all books
2. Search for a book
3. Borrow a book
4. Return a book
5. View all users
6. Exit

Enter your choice (1-6): 1

All Books:
1. "To Kill a Mockingbird" by Harper Lee (Available)
2. "1984" by George Orwell (Checked Out)
3. "The Great Gatsby" by F. Scott Fitzgerald (Available)
----------------------------------------

Please choose an option:
1. View all books
2. Search for a book
3. Borrow a book
4. Return a book
5. View all users
6. Exit

Enter your choice (1-6): 3

Enter your User ID: 1
Enter the Book ID you want to borrow: 2

Sorry, the book "1984" is currently checked out.
----------------------------------------
```

## 📌 Submission Guidelines

- **Choice of Platform:** You can complete this assignment in:
  - Google Colab (as a `.ipynb` file)
  - VS Code (as a `.py` file)
  - VS Code (Jupyter) (as a `.ipynb` file)
- **Push Your Code to GitHub:** Once you have completed the assignment, push your code to a GitHub repository.
- **Submit the GitHub Link:** Submit the link to your GitHub repository in Google Classroom.

## 🔗 Resources

- Chapters 1 to 7 of _Python Crash Course, 3rd Edition_ by Eric Matthes.

## 📧 Questions?

If you have any questions or need further guidance, feel free to reach out!

---
