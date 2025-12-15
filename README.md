# Student Enrollment System

This codebase contains both the frontend and backend of a student enrollment system with basic functionality such as,

<ul>
<li>Registration / Login</li>
<li>Enrollment to courses</li>
<li>Removal from courses</li>
</ul>


# How to run locally

## Requirements

+ python
+ npm
+ MS SQL or MySQL

## Configure Database

Create and populate the database by executing the following files in order,

1. [create.sql](schema/create.sql) - create the database
2. [schema.sql](schema/schema.sql) - create the tables in the database
3. [populate.sql](schema/populate.sql) - add data to the tables

## Run Server
In the `...\server` directory, run the following commands,

### Windows
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app
```

### MacOS / Linux
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app
```

## Run Frontend
In the `...\client`  directory, run the following commands,
```
npm install
npm run dev
```
Make sure the frontend runs on port **5173** as that the is port configured in the backend to support CORS. If not, you can do one of the following,

+ change the configuration of the frontend to run on port 5173.
+ add the correct localhost url into _origins_ array in [main.py](server/main.py).

<img width="712" height="82" alt="Screenshot 2025-12-15 142057" src="https://github.com/user-attachments/assets/f6da9f15-bb62-49d0-8fc6-61e27296101e" />

