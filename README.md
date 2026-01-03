# Dayflow HRMS 🧑‍💼

Dayflow is a role-based Human Resource Management System built with Django.

## Features
- Admin / Employee roles
- Secure authentication
- Attendance check-in & check-out
- Attendance history
- Leave application & approval
- Employee profile management
- Clean dashboard UI

## Tech Stack
- Django
- Python
- SQLite
- HTML / CSS

## How to Run
```bash
git clone https://github.com/vanshbhanushali/dayflow.git
cd dayflow
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
