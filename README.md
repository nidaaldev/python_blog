# Python Blog Project

This is a learning project to build a simple blog using Python and FastAPI. As a beginner, I created this project to understand web development concepts and practice Python programming.

## About the Project

This is a basic blog application built with:
- FastAPI for the backend
- SQLite for the database
- Jinja2 for templating
- Basic HTML/CSS for the frontend

## Features
- User authentication (login/register)
- Dashboard for managing posts
- Create, edit, and delete blog posts
- Simple and clean UI

## Installation

1. Clone the repository
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Create a `.env` file in the root directory with your JWT secret key:
```
SECRET_KEY=your_secure_random_string_here
```
4. Run the application:
```
fastapidev dev main.py
```

## Project Structure
- `/api` - API routes and endpoints
- `/auth` - Authentication utilities
- `/db` - Database configuration
- `/models` - Data models
- `/services` - Business logic
- `/templates` - HTML templates
- `/tests` - Unit tests

## Environment Variables

The project uses the following environment variables:
- `SECRET_KEY` - A secure random string used for JWT token signing and verification. This key is essential for the authentication system to work properly and should be kept secret.

## Learning Goals
- Understanding FastAPI framework
- Working with databases
- Implementing authentication
- Template rendering
- Basic testing

## Note
This is a learning project and may not follow all best practices. Feel free to suggest improvements or use it as a starting point for your own learning journey!
