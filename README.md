# django-vite-vue-starter

A starter project using Django, Vite and Vue where Vue is used inside Django templates instead of its own application.

This repository was created for my Vite tutorial series.

### [The Django Developer's Guide to Vite](https://ctrlzblog.com/the-django-developers-guide-to-vite/)
Introduction to Vite and how you can install it in a Django project. Uses the django-vite package to link Django templates with the Vite static file server.
 
### [Using Vue with Django Templates](https://ctrlzblog.com/add-vue-to-your-django-templates-with-vite/)
Demonstrates Vite's Vue plugin and shows you how to set up a Vue app that is rendered in a Django template. Covers how to pass data from a Django view to a Vue component. Uses Single File Components.

## How to use

1. Create a virtual environment
```
python3 -m venv venv
```

2. Activate your virtual environment
```
source venv/bin/activate
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Run migrations
```
python manage.py migrate
```

5. Start the Django development server
```
python manage.py runserver
```

6. Start the vite server
```
npm run vite
```
