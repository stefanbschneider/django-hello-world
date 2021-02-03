# Django "Hello World" App

A Django web app that says "Hello World!", [deployed on Heroku](https://django-hello-world-app.herokuapp.com).

As an example of how to build a new Django app and deploy it on Heroku.

Corresponding blog posts:

* [Building a Django App and Deploying It on Heroku](https://stefanbschneider.github.io/blog/django-heroku). Corresponds to [release v1.0](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.0.0).
* [Adding Google Analytics to a Django App](https://stefanbschneider.github.io/blog/django-google-analytics). Corresponds to [release v1.1](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.1.0).
* [Adding a Database to a Django App](https://stefanbschneider.github.io/blog/django-db). Corresponds to [release v1.2](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.2.0).
* [Using Bootstrap to Style a Django App](https://stefanbschneider.github.io/blog/django-bootstrap). Corresponds to [release v1.3](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.3.0).

## Setup

```
pip install -r requirements
```

## Usage

### Development

```
python manage.py runserver
```

The app is running on http://localhost:8000/

### Production Deployment on Heroku

See corresponding [blog post](https://stefanbschneider.github.io/blog/django/heroku/github/deployment/2021/01/19/django-heroku.html).
