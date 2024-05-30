## Task Tracer v0.0.3
Rest Framework (DRF) without a server for a single HTML page. Here's a simple example of how you can do it:

First, you need to install Django and Django Rest Framework:

```pip install -r requirements.txt```


### For Create Project
Then, create a new Django project:

```django-admin startproject myproject```

Next, create a new Django app:

```python manage.py startapp myapp```

### Create DB
Now, let's create a simple model in myapp/models.py:
Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Now, you can run the server:

```python manage.py runserver```


