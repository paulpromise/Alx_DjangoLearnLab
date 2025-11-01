# Introduction to Django

A learning project to explore Django fundamentals, including project structure, settings, and basic configuration.

## Project Structure

```
Introduction_to_Django/
├── Pipfile              # Python dependencies
├── LibraryProject/      # Main Django project
│   ├── manage.py        # Django management script
│   └── LibraryProject/  # Project settings directory
│       ├── __init__.py
│       ├── settings.py  # Project settings
│       ├── urls.py      # URL routing
│       ├── asgi.py      # ASGI configuration
│       └── wsgi.py      # WSGI configuration
└── README.md           # This file
```

## Getting Started

### Prerequisites
- Python 3.x
- Pipenv (for dependency management)

### Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```

4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

### Running the Project

To run the development server:
```bash
cd LibraryProject
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Django Management Commands

Common Django management commands:

- `python manage.py migrate` - Apply database migrations
- `python manage.py makemigrations` - Create database migrations
- `python manage.py createsuperuser` - Create an admin user
- `python manage.py shell` - Open Django shell
- `python manage.py test` - Run tests

## Features

- Django project setup and configuration
- URL routing
- Settings management
- Development server

## Learning Objectives

- Understand Django project structure
- Learn Django configuration and settings
- Explore URL routing and views
- Work with models and databases

## License

This is an educational project for learning purposes.

## Author

Paul Promise
