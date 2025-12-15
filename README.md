# Student Enrollment System

This codebase contains both the frontend and backend of a student enrollment system with basic functionality such as,

<ul>
<li>Registration / Login</li>
<li>Enrollment to courses</li>
<li>Removal from courses</li>
</ul>


# How to run locally

## Requirements

+ Python _3.10+_
+ Node.js _18+_
+ MS SQL _2019+_ ***or*** MySQL _8.0+_

## Configure Database

Create and populate the database by executing the following files in order,

1. [create.sql](schema/create.sql) - create the database
2. [schema.sql](schema/schema.sql) - create the tables in the database
3. [populate.sql](schema/populate.sql) - add data to the tables

>[!NOTE]
>The above schema is defined specifically for **MS SQL**. Slight variations may be needed if you are using a different type of database. Make sure to make the required changes to the schema before execution.

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
>[!NOTE]
>Make sure the backend is running on PORT 8000. If not do ***one of the following***,
>+ configure the backend to run on port 8000.
>+ change the PORT in the server url in [callers.ts](client/callers.ts).
><img width="437" height="68" alt="Screenshot 2025-12-15 161100" src="https://github.com/user-attachments/assets/9e07e314-8628-4c40-b37b-fa1eaf50a83e" />
 

## Run Frontend
In the `...\client`  directory, run the following commands,
```
npm install
npm run dev
```
>[!NOTE]
>PORT **5173** is the configured PORT in the backend to support CORS. If your localhost PORT is different you can do ***one of the following***,
>+ configure of the frontend to run on port 5173.
>+ add the correct localhost url into _origins_ array in [main.py](server/main.py).
><img width="712" height="82" alt="Screenshot 2025-12-15 142057" src="https://github.com/user-attachments/assets/f6da9f15-bb62-49d0-8fc6-61e27296101e" />

