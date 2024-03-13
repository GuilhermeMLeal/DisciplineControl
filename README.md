# Discipline Control API

This is an API project for controlling students, disciplines, tasks, and their relationships.

## Overview

This project offers a set of tools for controlling instances of entities and their relationships. In this API, you can add, edit, list, delete, and perform many other functionalities.

## Requirements

- Python 3.11.5
- Django 4.2.4
- Django Rest Framework 3.14.0
- Postman (to test the API)

### Note: All requirements will be in the requirements.txt file, so when you have the virtual environment, the requirements will be automatically supplied after installation.

## Environment Setup

To start the project, we need to follow some steps for its operation. Follow the steps below to set up the development environment:

1. **Create a folder**
```
mkdir api_controle_disciplina
```
2. **Enter the folder**
```
cd samu
```
3. **Clone the repository:**
```
git clone origin https://github.com/GuilhermeMLeal/API_Controle_Diciplina.git
```
4. **Open the project**
Note: If you are using VSCode
```
code .
```
5. **Activate the virtual environment in the terminal**
Activate the terminal in your IDE, then execute the following commands:
```
python -m venv .env
./.env/Scripts/activate
```
6. **Install the requirements.txt to get all dependencies**
```
pip install -r requirements.txt
```
7. **Ready, just run this command and open the address in your browser, or, if you have the Postman software, run the provided JSON file**
```
python manage.py runserver
```

### For those interested in making significant modifications, run the commands below:

**Important Commands:**

- `python manage.py runserver`: Starts the server to run the application.
- `python manage.py makemigrations`: Executes the database formatting.
- `python manage.py migrate`: Applies the migrations to the database.

Remember to execute these commands in the terminal within the project directory to perform the necessary actions.

---
