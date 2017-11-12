# djangogo
Django Project

Table Of Content
- [Installation & Start-up](#installation-&-startup)
- [Django Models](#django-models)

## Installation & Startup
Basic installation for django
` pip install django`

- Check django version
` python -m django --version`

- Django setup should follow in the order below :


#### Creating new django project
```
    django-admin startproject <project-name>
```
#### Run server
```
    $ cd <project-name>
    $ python manage.py runserver 8080
    
    - For c9:
    $ python manage.py runserver 0.0.0.0:8080
```
#### Create Database
- If new server,will need to re-migrate the database to re-initialize and create superuser for admin
```
    $ cd <project-name>
    $ python manage.py migrate
```

#### Create an application (app)
```
    $ cd <to the same level as manage.py>
    $ python manage.py startapp <app-name>
```

#### Create tables for models in database
```
    $ python manage.py makemigrations <app-name>
    $ python manage.py migrate <app-name>
```

### Django file directory
    
```
    $ tree <project path>
    
myProject/
├── myApp
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── myApp
│   │       └── webPage.html
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── myProject
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

### Manage.py
Interaction wi    $ django-admin <command> [options]
    $ manage.py <command> [options]
    $ python -m django <command> [options]th django project :
https://docs.djangoproject.com/en/1.11/ref/django-admin/

- Sets package path on sys.path and DJANGO_SETTINGS_MODULE env variables to point to settings.py file.
- Django-admin script needs to be in the system path (originally located at Python installer : site-packages/django/bin
- Generally, when working on a single Django project, it’s easier to use manage.py than django-admin. If you need to switch between multiple Django settings files, use django-admin with DJANGO_SETTINGS_MODULE or the --settings command line option.

- Possible command line usage :
```
    $ django-admin <command> [options]
    $ manage.py <command> [options]
    $ python -m django <command> [options]
```
    
### myProject/Settings.py
Settings/configuration for Django project. Django settings will tell you all about how settings work.
https://docs.djangoproject.com/en/1.11/topics/settings/

#### Static files
- Add static root directory
```
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

#### Allowed hosts
- When debug setting is True and ALLOWED_HOSTS is empty, the host is validated against `['localhost', '127.0.0.1', '[::1]']`

- For hosted solution, will need to include host name in the settings. Eg:
```
    ALLOWED_HOSTS =python manage.py runserver 0.0.0.0:8080 ['127.0.0.1', '<your_username>.pythonanywhere.com']
    ALLOWED_HOSTS = ['127.0.0.1',https://django-username.c9users.io]
```

#### Database
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

#### Installed Apps
- List all the installed apps created, at to the end of the list.
- By default should have the following:
```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
```


### myProject/__init__.py 
An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
https://docs.python.org/3/tutorial/modules.html#tut-packages

- required to make Python treat the directories as containing packages; this is done to prevent directories with a common name from unintentionally hiding valid modules that occur later on the module search path.
- init code for packageSettings/configuration for this Django project. Django settings will tell you all about how settings work.
https://docs.djangoproject.com/en/1.11/topics/settings/ / set __all__ variable


### myProject/urls.py
- URLconfs : https://docs.djangoproject.com/en/1.11/topics/http/urls/
- Urls.py under the project folder(myProject) is the main source of link for urls with other folder views.
- Need to add
  1. In myProject.urls.py: add urlpatterns to include individual child app's urls
  ```
      urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'', include('myApp.urls')),
  ```
  2. Create the individual myApp.urls.py file under the myApp folder and add the below imports. This imports django's function url and imports all views in myApp.views.py(since urls.py and views.py are in the same folder). The urlpatterns will link the regex to its views.
  ```
    myApp.urls.py:
    from django.conf.urls import url
    from . import views 
    
    urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
  ```  
  3. Create the view to link the myApp.urls to the class / object and add the following :

#### Arguments
   - required : regex, view
   - optional : kwargs, name
    
(a) __regex - regular expression__

- Compiled the first time URLconf module is loaded
- Matches patterns in strings / url patterns, checks list of expression til finds one that matches
```
    - ^ for the beginning of the text
    - $ for the end of the text
    - \d for a digit
    - + to indicate that the previous item should be repeated at least once
    - () to capture part of the pattern
```

- E.g:
```
    For url : http://www.mysite.com/post/12345/ ==> ^post/(\d+)/$
    
    - ^post/ is telling Django to take anything that has post/ at the beginning of the url (right after ^)
    - (\d+) means that there will be a number (one or more digits) and that we want the number captured and extracted
    - / tells django that another / character should follow
    - $ then indicates the end of the URL meaning that only strings ending with the / will match this pattern
```

(b) __view__
- once found match for regex, django calls specified view function with an HttpRequest object and any captured values from the regex as other args.

(c) __kwargs__
- Arbitrary keyword args passed in a dict to the target view.

(d) __name__
- Name URL used to identify the view elsewhere in django, esp from within templates. Important to name each URL in the app


### myProject/wsgi.py  
An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/

## Django Model

Model field types : (https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types).

### myApp/views.py
- https://docs.djangoproject.com/en/1.11/topics/http/views/
- View holds the implementation logic of each application, it requests information from the model and passes it to a *template*.
- Inputs a request and returns a render function that renders the template myApp/<url-name>.html. Templates are webpages that are reuseable. 

### myApp//models.py

### myApp//admin.py
- To include models defined in models.py and register to be visible on the admin page. `admin.site.register(method)`
#### Templates
- https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
- E.g: 
```
    from .models import Post
    admin.site.register(Post)
```

- Create superuser for admin credentials for login admin dashboard access.
```
    $ pythong manage.py createsuperuser
```














