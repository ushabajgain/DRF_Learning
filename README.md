# Learning Django REST Framework

A hands-on collection of code examples and notes for learning Django REST Framework (DRF), focused on building RESTful APIs.

---

## What’s Covered

-  Django project and app setup
-  Basic REST API endpoints (POST, GET, PUT, DELETE)
-  Serializers
-  ViewSets and Views
-  Routers
-  Authentication (Basic and Token-based)
-  Permissions

---


---

## Learning Notes

### What is Django REST Framework (DRF)?
Django REST Framework is a powerful and flexible toolkit for building Web APIs using Django.

### Core Components

- **Serializers**: Convert complex data (like querysets) into JSON and vice versa.
- **Views & ViewSets**: Define logic for handling requests (CRUD).
- **Routers**: Automatically map URLs to ViewSets.
- **Authentication & Permissions**: Control access to the API.

### HTTP Methods
- `GET`: Retrieve data
- `POST`: Create data
- `PUT`: Update data
- `DELETE`: Remove data

---

## Requirements

- Python 
- Django 
- djangorestframework

Install dependencies:

```bash
pip install -r requirements.txt

git clone https://github.com/yourusername/learning-drf.git
cd learning-drf
python -m venv venv
source venv/bin/activate
pip install django djangorestframework
python manage.py runserver


