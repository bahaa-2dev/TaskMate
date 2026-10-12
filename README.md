# TaskMate

A simple command-line task manager written in pure Python (no external libraries).

## Features
- Add a task (empty tasks and numbers-only tasks are rejected)
- Show all tasks with their numbers and status
- Mark a task as completed
- Delete a single task or all tasks
- Search tasks by keyword (case-insensitive)
- Tasks are saved to `tasks.json`, so they are not lost when you close the program
- Input validation: the program does not crash on invalid input

## How to Run
1. Install Python 3
2. Open a terminal in the project folder
3. Run:

```
python TaskMate.py
```

## Example
```
1: Add
2: Show
3: Complete
4: Delete
5: Delete all
6: Search
7: Exit
Choose a number (1-7): 1
Enter task: Study Python
Task added successfully!
```

## Concepts Used
- Lists and dictionaries
- Functions
- `while` and `for` loops
- Error handling with `try/except`
- Reading and writing JSON files

## Author
Bahaa Bani Khaled