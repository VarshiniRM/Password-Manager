```markdown
##Password Manager

A simple and secure password manager web application built with Flask, SQLite, and SQLAlchemy. This project is designed to help users securely store and manage their passwords with encryption, making it easier to keep track of credentials for various websites and services. The passwords are stored securely using hashing techniques, and the application provides a simple user interface for adding, viewing, and deleting passwords.

## Features

- **User Authentication**: Secure login and registration system to ensure only authorized users can access their password data.
- **Password Storage**: Securely store passwords for various websites, with an option to view or delete them.
- **Password Hashing**: Passwords are hashed before being stored in the database, enhancing security.
- **SQLite Database**: The application uses SQLite to store user data and passwords.
- **Flask Backend**: Built using the Flask web framework for routing and server-side processing.
- **Responsive Design**: User interface designed for ease of use and accessibility.

## Technologies Used

- **Flask**: Web framework for Python to handle backend logic and routing.
- **SQLAlchemy**: Object Relational Mapper (ORM) for database interaction.
- **SQLite**: A lightweight, serverless database for storing user and password data.
- **Jinja2**: Templating engine for rendering HTML dynamically.
- **Werkzeug**: Provides utility functions for password hashing and session management.

## Installation

### Prerequisites

To run the project locally, you'll need:
- **Python 3.x**: Python version 3 or above.
- **Flask**: The Python web framework used to build the app.
- **Flask-SQLAlchemy**: ORM for easy database management.
- **SQLite**: Database system used for this project.

### Steps to Install

1. **Clone the Repository**:
   First, clone this repository to your local machine:
   ```bash
   git clone https://github.com/VarshiniRM/Password-Manager.git
   ```

2. **Navigate to the Project Folder**:
   Change into the project directory:
   ```bash
   cd Password-Manager
   ```

3. **Set Up a Virtual Environment**:
   Create and activate a Python virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   ```

   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Required Dependencies**:
   Install the project dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your browser and visit `http://127.0.0.1:5000` to start using the password manager.

## Using the Application

1. **Register for an Account**:
   - Go to the `Register` page to create a new account. You'll need to provide a username, email, and password.
   - Passwords are securely hashed and stored in the database.
   - ![image](https://github.com/user-attachments/assets/90757db5-399d-4908-acc0-3e613d238388)

2. **Log In**:
   - Once registered, log in to the application using your username and password.
   - ![image](https://github.com/user-attachments/assets/317ae136-1c37-4409-b33c-682ed3fbf616)

3. **Managing Passwords**:
   - After logging in, you can:
     - **Add a new password**: Store passwords for different websites and services.
     - **View stored passwords**: See the details of your saved passwords (hashed for security).
     - **Delete a password**: Remove saved passwords when they are no longer needed.

4. **Logout**:
   - Log out of the application when you're finished to protect your data.

## Database

This application uses **SQLite** as its database. The database file is stored in the project directory, and it contains two tables: `User` and `Passwords`.

You can manage the database using the [DB Browser for SQLite](https://sqlitebrowser.org/) to inspect or modify the data if needed.

## Security

- **Password Hashing**: The application uses Flask's built-in Werkzeug library to hash passwords before storing them in the database. This ensures that passwords are not stored in plain text.
- **Session Management**: The app uses Flask sessions to keep users logged in while they navigate between pages.
- ![image](https://github.com/user-attachments/assets/6d5aae09-3cbe-43a8-9a0f-8ef215c51206)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or open an issue if you find any bugs or have suggestions for improvement!
```
