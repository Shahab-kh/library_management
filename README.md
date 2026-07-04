# Library Management System

A Django-based Library Management System designed to manage books, members, and borrowing operations.

## Overview

This project was developed as part of my Django learning journey and focuses on implementing real-world library management workflows.

The system allows librarians to manage books, register members, track borrowing records, and monitor book availability through a structured database design and business logic.

## Features

### Book Management

* Add and manage books
* Track total quantity and available quantity
* Store book information such as title, author, edition, and description

### Member Management

* Register library members
* Automatically generate unique member codes
* Store member contact information
* Automatically record join dates

### Borrowing System

* Borrow books
* Automatically set due dates (14 days)
* Prevent borrowing when no copies are available
* Limit members to a maximum of 5 active borrows
* Return borrowed books
* Automatically update book availability

### Admin Panel

* Customized Django Admin interface
* Read-only system-managed fields
* Search and filtering support for management tasks

## Technologies Used

* Python
* Django
* SQLite

## Project Structure

* Books App
* Members App
* Borrow Records App
* Accounts App
* Dashboard App

## Current Status

Implemented:

* Database models
* Business logic and validations
* Django Admin customization
* ModelForms

Planned:

* Views
* Templates
* Authentication
* Dashboard
* Search functionality
* Improved user interface

## Installation

Clone the repository:

```bash
git clone https://github.com/Shahab-kh/library_management.git
```

Move into the project directory:

```bash
cd library_management
```

Install dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

## Future Improvements

* Authentication and user roles
* Overdue book tracking
* Dashboard statistics
* Search and filtering
* Enhanced user experience
* Deployment

## License

This project is intended for learning purposes and portfolio demonstration.

