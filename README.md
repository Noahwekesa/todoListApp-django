# Django Todo List App with DaisyUI and HTMX

- This is a simple Todo List web application built with Django, DaisyUI, and HTMX. DaisyUI provides a set of stylish UI components, and HTMX enables seamless and fast interactions between the client and server.

## Features

- Add, edit, and delete tasks
- Mark tasks as complete
- Responsive and user-friendly design

### DASHBOARD

![Image](https://github.com/Noahwekesa/todoListApp-django/blob/master/images/dash.png)

### lOGIN FORM

![Image](https://github.com/Noahwekesa/todoListApp-django/blob/master/images/login.png)

## Prerequisites

Make sure you have the following installed before running the application:

- python (3.12.1 or higher)
- check requirement.txt for django version

## Installation

1. clone the respository

```sh
git clone https://github.com/Noahwekesa/todoListApp-django.git
```

2. navigate inside the respository

```sh
cd todoListApp-django
```

3. install virtual env

```sh
virtualenv venv
```

4. Activate virtual env

```sh
source venv/bin/activate
```

4. install dependencies

```sh

pip install -r requirements.txt
```

5. Navigate into src and run migrations

```sh
cd src

python manage.py makemigrations


python manage.py migrate

```

6. runserver

```sh
python manage.py runserver
```

Open your browser and go to http://127.0.0.1:8000/ to view the Todo List app.

## Usage

- Log in using the superuser credentials created during the installation.
- Add, edit, and delete tasks as needed.
- Mark tasks as complete by clicking on the checkbox.

### Technology used:

- `daisyUI` - [doc link](https://daisyui.com/)
- `django-widget-tweaks` - [do link](https://pypi.org/project/django-widget-tweaks/)
- `HTMX` - [doc lin](https://htmx.org/docs/#installing)
- `django-template-partials` - [doc link](https://github.com/carltongibson/django-template-partials)
- `django-htmx` - [Adding CSRF Token to HTMX request](https://django-htmx.readthedocs.io/en/latest/tips.html)

Feel free to contribute, report issues, or suggest improvements!
