Django REST Skeleton
====================

**A Django REST framework project template for quickly bootstraping REST APIs**

---

This is an opinionated [Django][django] project skeleton based on:

* [Django REST framework][django-rest-framework]
* Configuration based on database URLs and configuration files
* Documentation with [Swagger][swagger]
* Authentication with OAuth2 [OAuth2][oaut2]

---


## Getting Started
1. Clone the repo from GitHub
1. Delete the `.git` folder
1. Remove/add anything as you see fit
1. Initialize as a new git repository for your own project
1. Change database connection settings `config.run_mode.[dev_mode | prod_mode].DATABASES` 
1. Install dependencies with the command `pip install -r .\requirements\all.txt `
1. Run the migrations with the command `python manage.py migrate`
1. Create superuser with the command `python manage.py createsuperuser`
1. Run the project using `python manage.py runserver` and you should see the default
success page provided by Django at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
1. Access the Django admin and create an application for OAuth2 authentication and configure as shown in the following screenshot [OAuth2_Configuration][OAuth2_Configuration]. Important to copy the Client_id and the Secret_id 



Project layout
--------------

## Project Tree
```bash
.
├── apps
│   └── core # A django rest app
│       ├── api
│       │   ├── v1
│       │   │   ├── example_component
│       │   │   │   ├── __init__.py
│       │   │   │   ├── UserPermissions.py
│       │   │   │   ├── UserSerializer.py
│       │   │   │   └── UserViewSet.py
│       │   │   ├── generic_component
│       │   │   │   ├── __init__.py
│       │   │   │   ├── GenericFilter.py
│       │   │   │   ├── GenericModel.py
│       │   │   │   ├── GenericPermissions.py
│       │   │   │   ├── GenericSerializer.py
│       │   │   │   ├── GenericService.py
│       │   │   │   └── GenericViewSet.py
│       │   │   ├── __init__.py
│       │   │   ├── tests.py
│       │   │   └── urls.py
│       │   ├── v2
│       │   │   ├── filters
│       │   │   │   └── __init__.py
│       │   │   ├── permissions
│       │   │   │   └── __init__.py
│       │   │   ├── serializers
│       │   │   │   └── __init__.py
│       │   │   ├── services
│       │   │   │   └── __init__.py
│       │   │   ├── viewsets
│       │   │   │   └── __init__.py
│       │   │   ├── __init__.py
│       │   │   ├── tests.py
│       │   │   └── urls.py
│       │   └── __init__.py
│       ├── models
│       │   └── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── tasks.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── common
│   ├── db
│   │   ├── __init__.py
│   │   └── ApiDBRouter.py
│   ├── middleware
│   │   ├── __init__.py
│   │   └── DisableCSRFMiddleware.py
│   ├── oauth2
│   │   ├── __init__.py
│   │   └── urls.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── __init__.py
│   └── generics.py
├── config
│   ├── run_mode
│   │   ├── __init__.py
│   │   ├── dev_mode.py
│   │   └── prod_mode.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── logs
│   ├── api.file.error.log
│   └── api.file.log
├── requirements
│   ├── all.txt
│   ├── deploy.txt
│   ├── dev.txt
│   ├── optional.txt
│   ├── required.txt
│   └── testing.txt
├── static
│   └── media
│       └── Configuracion de aplicacion de OAuth2.png
├── .gitignore
├── manage.py
└── README.md

```


License
-------

Copyright (c) 2023, Leyan Chang
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[django]: https://www.djangoproject.com/
[django-rest-framework]: http://django-rest-framework.org/
[swagger]: https://drf-yasg.readthedocs.io/en/stable/readme.html
[oaut2]: https://django-oauth-toolkit.readthedocs.io/en/latest/install.html
[OAuth2_Configuration]: static/media/Configuracion%20de%20aplicacion%20de%20OAuth2.png
