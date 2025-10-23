# CLI Student Management System

A simple, command-line based student management system written in Python. This application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on student profiles.



## Features

*   **View All Students**: Display a list of all existing student profiles in a clean, tabular format.
*   **Create New Profile**: Add a new student to the system.
*   **Browse Particular Profile**: Search for and display a specific student's profile using their registration number.
*   **Edit Existing Profile**: Modify the details of an existing student.
*   **Delete Profile**: Remove a student's profile from the system.

## Prerequisites

*   Python 3.x

## Installation

1.  Clone the repository or download the source code.

2.  Install the required Python package using pip:
    ```sh
    pip install tabulate
    ```

## Usage

To start the application, run the `main.py` script from your terminal:

```sh
python main.py
```

You will be greeted with the main menu, where you can choose an option by entering the corresponding number.

```
Welcome to CLI Student management system!

Choose one of the following options:

[1] View list of all existing student profiles
[2] Create new student profile
[3] Browse particular profile
[4] Edit existing profile
[5] Delete existing profile

Your option -
```

## Project Structure

The project is organized into several modules, each with a specific responsibility:

*   `main.py`: The main entry point of the application. It displays the menu and handles user choices.
*   `banner.py`: Contains the function to print the ASCII art banner at startup.
*   `view_all.py`: Currently acts as a mock database, holding the student data in a Python list.
*   `browse_particular_profile.py`: Contains the logic to find and display a single student profile.
*   `createprofile.py`: Handles the logic for creating a new student profile.
*   `editprofile.py`: Manages the process of editing an existing profile's details.
*   `deleteprofile.py`: Contains the logic for deleting a student profile.
*   `closemenu.py`: A utility module that prompts the user to either exit the application or return to the main menu after an operation.

## Future Improvements

*   **Data Persistence**: Replace the hardcoded list in `view_all.py` with a persistent storage solution like a CSV file, JSON file, or a lightweight database (e.g., SQLite).
*   **Improved Main Loop**: Refactor `main.py` to use a continuous loop, allowing the user to perform multiple actions without the program trying to exit after each one.
*   **Enhanced Input Validation**: Add more robust validation for all user inputs to prevent errors and crashes.