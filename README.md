# Student Enrollment System

This codebase contains both the frontend and backend of a student enrollment system with basic functionality such as,

<ul>
<li>Registration / Login</li>
<li>Enrollment to courses</li>
<li>Removal from courses</li>
</ul>


# How to run locally

## Configure Database

## Run Server

## Run Frontend
In the `...\client`  directory run the following commands,
```
npm install
npm run dev
```
Make sure the frontend runs on port 5173 as that the is port configured in the backend to support CORS. If not, you can do one of the following,

+ change the configuration of the frontend to run on port 5173.
+ change the middleware setup in [main.py](server/main.py) to support the correct localhost port.
