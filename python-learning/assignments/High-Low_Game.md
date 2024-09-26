# Python Programming Assignment 08 (B): High-Low Game

## Objective

Develop a game called "High-Low" to gain experience working with control flow, Booleans, and user input validation in Python.

## Task Overview

We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

- Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!
- You make a guess, saying your number is either higher than or lower than the computer's number
- If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!
- These steps make up one round of the game. The game is over after all rounds have been played.

## Assignment Steps

### Milestone #1: Generate Random Numbers

**Objective:** Understand how to generate random numbers in Python.

**Task:** Use Python’s `random` module to generate two random numbers between 1 and 100: one for the player and one for the computer.

**Instructions:**

- Import the `random` module.
- Use `random.randint(1, 100)` to generate two numbers: one for the player and one for the computer.
- Print both numbers for testing purposes to verify your game logic in the next milestones.

### Milestone #2: Get the User Choice

**Objective:** Collect user input and understand how to handle it.

**Task:** Prompt the user to guess whether their number is higher or lower than the computer's number.

**Instructions:**

- Use the `input()` function to ask the user to type either "higher" or "lower" based on their guess.
- Display the user's number and ask them to guess if it is higher or lower than the computer’s number.

### Milestone #3: Write the Game Logic

**Objective:** Implement logic to determine if the user’s guess is correct.

**Task:** Check if the user’s guess matches the actual comparison between the two numbers and update the score.

**Instructions:**

- Compare the player's number to the computer's number using `if` and `else` statements.
- Print whether the user was correct or not, and display the actual computer number.
- Decide what happens if both numbers are equal (e.g., the computer wins in case of a tie).

### Milestone #4: Play Multiple Rounds

**Objective:** Implement the game over multiple rounds.

**Task:** Play a specified number of rounds and keep track of the current round number.

**Instructions:**

- Create a constant `NUM_ROUNDS` (e.g., 5 rounds) and use a loop to repeat the game logic for each round.
- In each round, generate new numbers and play according to the previous milestones.
- Display the round number and separate each round visually by adding blank lines.

### Milestone #5: Adding a Points System

**Objective:** Keep track of the user’s score throughout the game.

**Task:** Maintain and display a score based on the number of correct guesses.

**Instructions:**

- Initialize a score variable before starting the rounds.
- Increase the score by 1 if the user guesses correctly.
- Display the updated score at the end of each round.

## Extensions (Optional)

### Extension #1: Safeguard User Input

**Objective:** Handle invalid user input gracefully.

**Task:** If the user enters something other than "higher" or "lower," ask them to re-enter their choice.

**Instructions:**

- Use a loop or conditional checks to validate the user’s input.
- Re-prompt the user until they enter a valid choice.

### Extension #2: Conditional Ending Messages

**Objective:** Provide feedback based on the user’s performance.

**Task:** Display a final message based on the user’s score at the end of the game.

**Instructions:**

- Define thresholds for performance (e.g., perfect score, more than half, less than half).
- Print a corresponding message for each performance level.

## Expected Output

Here's what the output of your game might look like:

```
Welcome to the High-Low Game!
--------------------------------
Round 1
Your number is 8
Do you think your number is higher or lower than the computer's?: lower
You were right! The computer's number was 35
Your score is now 1

Round 2
Your number is 88
Do you think your number is higher or lower than the computer's?: higher
Aww, that's incorrect. The computer's number was 100
Your score is now 1

Round 3
Your number is 63
Do you think your number is higher or lower than the computer's?: higher
You were right! The computer's number was 5
Your score is now 2

Thanks for playing!
Good job, you played really well!
```

## Tips

- Break down each step into smaller tasks and test your code frequently to catch any errors.
- Pay attention to edge cases, like when the user's and computer's numbers are the same.
- Ensure your program is user-friendly and gives clear instructions.

By following these steps, you’ll develop a solid understanding of control flow and user input validation while creating an engaging game. Happy coding!

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
