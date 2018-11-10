# Django Cheat Sheet
# Table Of Content
   * [Overview](#overview)
   * [Highlight commands](#highlight-commands)

## Installation
* [Environment Setup](#environment-setup)
    * [Venv](#venv)
    * [Docker](#docker)

## Setup
* [Start / Run](#Start-/-Run)
    * [Run Server](#run-server)
    * [Create Superuser](#Create-Superuser-&-Migrate-DB)
    * [Create App](#create-app)
    * [Configure Settings](#configure-settings)
    * [Database Settings](#database-settings)


## Development
* [Django Files and Components](#django-files-and-components)
    * [Project files](#project-files)
        * [manage.py](#managepy)
        * [settings.py](#settingspy)
        * [wsgi.py](#wsgipy)
        * [urls.py](#urlspy)
    * [App Files](#app-files)
        * [urls.py](#urlspy)
        * [admin.py](#adminpy)
        * [models.py](#modelspy)
        * [views.py](#viewspy)
    * [Function Based Views](#function-based-views)
    * [Class Based Views](#class-based-views)
    * [Generic Based Views](#generic-based-views)
    * [Templates](#templates)
        * [Create base template](#create-base-template)
        * [Django to html syntax](#django-to-html-syntax)
* [Django Models](#django-models)
    * [Querysets](#querysets)
    * [Query objects](#query-objects)
* [Misc](#misc)
    * [Additional python libraries to use:](#additional-python-libraries-to-use)

## Overview
```
                  models.py : Data layer(Database)
                     │
                     v
    urls.py  ──>  views.py  : App logic
                     │
                     v
                  templates : UI layer(base.html, etc)
```


## Highlight commands
- Django console : ` $ python manage.py shell`

## Installation
### Environment Setup
- Lots of methods to use, either virtual environment or use a containers such as Docker with Docker-compose
#### Venv
- Install
```
    $ pip install django
    $ python -m django --version
```
- Create Project
```
    $ django-admin startproject <project-name>
```

#### Docker
##### Create Django Project in Container
- Create docker-compose.yml, Dockerfile & requirements.txt files
- Create Django project with docker-compose
```
    $ docker-compose exec web django-admin startproject <project>
```

- In docker, django-admin creates files ownership to root. Change to user:
```
    $ sudo chown -R $USER:$USER
```
- Move django files and folders so that manage.py is in the same folder dir as docker-compose.yml file


##### Database Settings
- Set Postgresql env settings
```
    $ POSTGRES_PASSWORD="PasswordHere"
    $ POSTGRES_USER="postgres"
    $ echo $POSTGRES_PASSWORD   PasswordHere
    $ echo $POSTGRES_USER       postgres
```

- Update settings.py with DB settings (take note of port used)
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
}

```
- When creating database, take note of the port number used. If conflicting with local env port number, stop local service before running docker.
- Stop local env service to release port(5432)
```
    $ sudo systemctl stop postgresql
```
[^](#table-of-content)

## Start / Run
### Docker
- Note : docker has different commands for different purposes. Use `up` for startup of services. Once services has started, to execute cmd within services, use `exec`. To start a separate service(one-off), use `run` to create separate individual container.

- Run dc command from top level dir of project
```
    $ docker-compose up / start
```

- To execute command within same service use `exec` instead of `run`
```
    $ docker-compose run web python manage.py runserver 8080
    $ docker-compose exec web python manage.py runserver 8000
    $ docker-compose exec web python manage.py migrate
```

- All other commands are similar to venv environment, with the execption of having docker-compose command at the front.

[^](#table-of-content)

### Run Server
- In the directory of `manage.py`:
```
    $ python manage.py run[^](#table-of-content)server 8080
    $ python manage.py run[^](#table-of-content)server 127.0.0.1:8080
    $ docker-compose exec [^](#table-of-content)web python manage.py runserver 8080
```
[^](#table-of-content)


### Create Superuser & Migrate DB
- For newly created projects, need to create a superuser and re-initialize the db.
- Create an admin user for the DB:
```
    $ python manage.py createsuperuser
```

- Re-migrate & re-init DB:
```
    $ python manage.py migrate

```
[^](#table-of-content)



### Create App
- An App is a subdirectory of a project.
- E.g: A project is a site that has multiple apps for blog, ecommerce, etc
```
    $ python manage.py startapp <app-name>
```

- Include new app to list of Installed App in `Settings.py`:
```
    INSTALLED_APPS = [
        'django.contrib.admin',
        ...,
        'app-name',
    ]
```

- Create tables for models in DB
- Whenever changes are made to models.py, migration needs to be executed:
```
    $ python manage.py makemigrations <app-name>
    $ python manage.py migrate <app-name>
```

- Add new App to url in <project/url.py>

[^](#table-of-content)


### Configure Settings
##### Static files
- Add static root directory
- Static file consists of CSS, images, etc and doesn't depend on request context and will be the same for every user.
```
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
- Uses local static folder directory that will be mimic(copied) into production live server static folder directory.
- Command to copy static files from local django folder to server static folders
```
    $ python manage.py collectstatic
    61 static files copied to "/home/.../static_cdn/static_root".
```

##### Allowed hosts
- When debug setting is True and ALLOWED_HOSTS is empty, the host is validated against `['localhost', '127.0.0.1', '[::1]']`

- For hosted solution, will need to include host name in the settings. Eg:
```
    ALLOWED_HOSTS =python manage.py runserver 0.0.0.0:8080 ['127.0.0.1', '<your_username>.pythonanywhere.com']
    ALLOWED_HOSTS = ['127.0.0.1',https://django-username.c9users.io]
```
[^](#table-of-content)

### Database Settings
```
    - default sqlite2 settings:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    - postgresql settings:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
```
[^](#table-of-content)


# Django Files and Components
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
[^](#table-of-content)

## Project files
- These are files that are autogenerated for each Django project (when `startproject` command is executed)

### manage.py
https://docs.djangoproject.com/en/2.0/ref/django-admin/
- puts project package on sys.path
- sets DJANGO_SETTINGS_MODULE env variables to point to settings.py file

### settings.py
https://docs.djangoproject.com/en/2.0/topics/settings/
- All settings / configuration are placed here

### wsgi.py
- Entry point for WSGI compatible web servers to serve project.

### urls.py
https://docs.djangoproject.com/en/2.0/topics/http/urls/
- Definition for urls in project and links to function-based-views / class-based-views in created Apps.
- Format:
```
    - required args :
        - regex : URL patterns to match
        - view : View associated with URL pattern
    - optional args:
        - kwargs : Arbitary keyword args passed in a dict to the target view
        - name : URL name used within templates, etc
```
- regex:
```
    - ^ for the beginning of the text
    - $ for the end of the text
    - \d for a digit
    - + to indicate that the previous item should be repeated at least once
    - () to capture part of the pattern
```
- Multiple files; for project/app level
- Project level file will store the main source of link with other folder views :
```
      urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'', include('myApp.urls')),
```
[^](#table-of-content)

## App Files
### urls.py
- App level file(manually create) will store the link for url with views specific for the app :
```
    from django.conf.urls import url
    from . import views
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    ]
```

### admin.py
- Include models defined in models.py and register to be visible on the admin page (will automatically creates django admin interface with defined models)
```
    from django.contrib import admin
    from .models import ModelClass1, ModelClass2

    # Register your models here.
    admin.site.register(ModelClass1)
    admin.site.register(ModelClass2)
```

### models.py
- Model field types : (https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types).
- Defines the database structure and relationship
- Everytime changes are made to models.py, run the migration command to update the database schema.


### views.py
- https://docs.djangoproject.com/en/2.0/topics/http/views/
- A view retrieves data from `models.py` according to the parameters, loads a template and renders the `template` with the retrieved data.
```
    Inputs  : A request
    Outputs : A (response) render function that renders the defined template (myApp/<url-name>.html).
              Either returns `HttpResponse` object containing the content for requested page, or raising an execption such as `Http404`
```
- Example:
```
    from django.views.generic import ListView, DetailView, TemplateView
    from django.views.generic.edit import CreateView, UpdateView, DeleteView
    from .models import ModelClass

    def ModelDoSomething(request):
        context = { 'object_list': data}
        return render(request, '<template>/<webPage>.html', context)

    class ModelListView(ListView):
        model = ModelClass
```
[^](#table-of-content)

## Function Based Views
In views.py:
```
    def contact(request):
        if request.method == 'POST':
            # Code block for POST request
        else:
            # Code block for GET / PUT / DELETE / etc request
```

In urls.py:
```
    urlpatterns = [
        url(r'contact/$', views.contact, name='contact')
    ]
```


## Class Based Views
In views.py:
```
    class ContactView(View):
        def get(self, request):
            # Code block for GET request

        def post(self, request):
            # Code block for POST request

```
In urls.py:
```
    urlpatterns = [
        url(r'contact/$', views.ContactView.as_view(), name='contact')
    ]
```

## Generic Based Views
- Django generic views have predefined template name that is expected. Name is derived from model name : `modelname_list.html`
- By default will look for templates in applications and template dir specified in settings.TEMPLATE_DIRS.

[^](#table-of-content)

## Templates
- Template extending to re-use HTML for different pages with different models, views, etc.
- Uses django template tags to transfer Python syntax to HTML.
- Adds to the top of templates file to load any static files
- Any static css file should be declared after all bootstrap styles to avoid being overwritten
```
    {% load staticfiles %}
    <html>
        <head>
          <link rel="stylesheet" href="{% static 'css/myApp.css' %}">
        </head>
    </html>
```
### Create base template
- Create block to insert specific HTML data from another template that extends to this particular template(base.html).
```
    {% block content %}
    ...
    {% endblock %}
```
- When other templates are extending the base.html file (calling the base.html), need to include linkage to base.html file.
- All other templates should be in same folder level as base.html
```
    {% extends 'myApp/base.html' %}
```
### Django to html syntax
- Print variables : `{{variables}}`
- Pipe string to convert line breaks to paragraph : ` string | linebreaksbr `
- Loops:
```
    {% for post in posts %}
        {{ post }}
    {% endfor %}
```
[^](#table-of-content)


# Django Models
## QuerySet
- A QuerySet is a list of objects of a given Model.
- https://docs.djangoproject.com/en/2.0/ref/models/querysets/
- In console shell import:
```
    $ from myApp.models import ModelClass
```

## Query objects
- Basic query for all objects
```
    $ qs = ModelClass.objects.all()
    $ qs = ModelClass.objects.all().values().order_by('id')
```

- Other commands to query data from db:
```
    $ qs = Product.objects.filter(title__contains='abc')
    $ qs = Product.objects.filter(title__icontains='shirt', description__iexact='Abc') #case insensitive
    $ qs = Product.objects.filter(id=4)
    $ qs = Product.objects.get(id=3)
    $ qs = self.get_queryset().filter(id=id)
```

- Import Users from DB
```
    $ from django.contrib.auth.models import User
    $ User.objects.all()
```

- Objects are created from classes in myApp.models.py
```
    $ <model-class-name>.objects.create(...)
```
[^](#table-of-content)

# Misc
### Additional python libraries to use:
#### pillow
- For ImageField control that checks if file used is an image file
- Installation : ` $ pip install pillow `
- Usage :
```
    [In models.py]:
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    [In views.py]:
    {{ object.image.url}}
```
[^](#table-of-content)


# Errors
```
    "django_session" does not exist
```
- Solution: run
```
    $ python manage.py migrate
    $ python manage.py syncdb
    $ python manage.py migrate sessions
```
[^](#table-of-content)
