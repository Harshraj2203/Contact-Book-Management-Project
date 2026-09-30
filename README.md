# Python Contact Book Management App

A simple, command-line based **Contact Book Management Application** written in Python. This application allows users to perform standard CRUD (Create, Read, Update, Delete) operations on their contacts, alongside searching and counting capabilities.

## Features

- **Create Contact:** Save new contacts with a unique name, age, email, and mobile number.
- **View Contact:** Retrieve and view detailed information of a specific contact by name.
- **Update Contact:** Modify the age, email, and mobile number of an existing contact.
- **Delete Contact:** Remove a contact from the management system.
- **Search Contact:** Search for contacts using partial or full name matching (case-insensitive).
- **Count Contacts:** View the total number of contacts currently saved in the application.

## Prerequisites

To run this application, you only need:
- **Python 3.x** installed on your system.

## How to Run

1. Copy the source code into a file named `main.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where `main.py` is saved.
4. Run the script using the following command:
   ```bash
   python main.py
   ```

## Technical Notes & Known Issues
*The current script contains variables scoping bugs within the View (`choice == '2'`) and Search (`choice == '5'`) functionalities where it prints global/unbound variables (`age`, `mobile`, `email`) instead of pulling them directly from the local `contact` dictionary iterator.*
