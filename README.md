# User Authentication System in Flask/Python

### A Simple Authentication System Project with basic user functionality in Python Flask with SQLAlchemy.

## Framework & Library

1. [Flask](https://flask.palletsprojects.com/)
2. [Flask-Login](https://flask-login.readthedocs.io/)
3. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
4. [Flask-WTF](https://flask-wtf.readthedocs.io/)
5. [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
6. [Flask-Migrate](https://flask-migrate.readthedocs.io)
7. [Bootstrap-Flask](https://bootstrap-flask.readthedocs.io/)
8. [Jinja2](https://jinja.palletsprojects.com/)

## Some Screenshots of our Project

### 2. Go to the project directory.

```bash
cd flask-user-authentication
```

### 3. Create virtual environment.

```bash
python3 -m venv venv
```

### 4. Activate the environment.

On Windows

```bash
venv\scripts\activate
```

On MacOS/Linux

```bash
source venv/bin/activate
```

To run this project locally, you will need to change `.env.example` file to `.env` on base directory 
and set environment variables.

### 5. Install the requirement packages.

```bash
pip install -r requirements.txt
```

### 6. Migrate/Create a database.

Initialize the database migration directory.
```bash
flask db init
```

Run migrate command.
```bash
flask db migrate -m "initial_migration"
```

Upgrade the database for latest migration.
```bash
flask db upgrade
```

### 7. Last to run the server.

```bash
flask run
```

To access this application open `http://localhost:5000` in your web browser.
