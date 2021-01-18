The repository contains 2 flask applications with the below mentioned functionality:
1. App - Basic CRUD operation using Flask + SQL Alchemy
2. App JWT - User authentication using Flask with JWT based authentication


Please follow the steps for running the code (with assumption that python is installed):

1. Clone the repository
2. Create a virtual environment
3. In the virtual environment, install the requirements from requirement.txt
4. Once the requirements are installed successfully, then run each file and enter the prompted input.


There are 2 flask applications in the repository inside flask folder by the name app and app_jwt.

* App 
In order to run the flask application, please follow the steps below:
1. Clone the repository
2. Create a virtual environment
3. In the virtual environment, install the requirements from requirement.txt
4. Install sqlite3 and create a database named 'employee.db' using command sqlite3 employee.db
5. Once the requirements are installed successfully, go inside the app directory where run.py file is located.
6. In the terminal, write the following:
  export FLASK_ENV=development
  export FLASK_APP=run.py
7. Now run: flask run --port 8000. This will start the development server at the local machine
8. Open the URL in the browser and redirect to /swagger in order to view the documentation.
9. Run the APIs from the UI.


* App-JWT
In order to run the flask application, please follow the steps below:
1. Clone the repository
2. Create a virtual environment
3. In the virtual environment, install the requirements from requirement.txt
4. Install sqlite3 and create a database named 'user.db' using command sqlite3 user.db
5. Once the requirements are installed successfully, go inside the app directory where run.py file is located.
6. In the terminal, write the following:
  export FLASK_ENV=development
  export FLASK_APP=run.py
7. Open flask shell and create role and first admin user in the shell.
8. Now run: flask run --port 8000. This will start the development server at the local machine
 

