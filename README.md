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
   pip install fastapi uvicorn jinja2 python-multipart python-jose[cryptography] passlib[bcrypt]
   ```
3. Run the application:
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

## Learning Goals

- Understanding FastAPI framework
- Working with databases
- Implementing authentication
- Template rendering
- Basic testing

## Note

This is a learning project and may not follow all best practices. Feel free to suggest improvements or use it as a starting point for your own learning journey!
