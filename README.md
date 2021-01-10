# MGP Weather

https://mgp-weather.herokuapp.com/

A weather forecast app. Allows users to search for the weather in any major city in the world.

Hosted on Heroku using a free plan. Site might take a moment to open on first launch.

### Tech stack:

* Python 3.8
* Django 3
* Bootstrap
* OPENWEATHER API

### How to run locally:

After cloning the app down to your machine, navigate into the root directory of the project. 

1. Install project requirements:
```
    pip install -r requirements.txt
```
2. Migrate and run project:
``` 
    python manage.py migrate
    python manage.py runserver
```