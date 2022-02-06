# Asynchronous Tasks in Django with Redis and Celery
build a minimalistic image processing application that generates thumbnails of images submitted by users.


<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="70" height="40"/>  <a href="https://docs.celeryproject.org/en/stable/" target="_blank" rel="noreferrer"> <img src="https://www.bitbarn.co.za/img/tech/celery.png" alt="django" width="70" height="40"/></a> 


**Recommendation**   -  Open one terminal and split in 3 parts 
  

### local dev setup

1) install Redis on you machine

2) clone repo

```
git clone https://github.com/encinasj/Image_processing.git
```
 after
```
cd image_parroter
```

3) make virtual env and activate it

```
python3 -m venv .env
source .env/bin/activate
```

4) install python requirements

```
pip install -r requirements.txt
```

5) Firsdt start redis-server in your terminal

```
redis-server
```

6)  Active virtual environment 

```
source .env/bin/activate
```

7) start celery worker in your terminal. 

'''make sure you are in the same directory as manage.py'''
```
celery -A image_parroter worker --loglevel=INFO                                                                                                          
```

8) start django dev server, in your terminal.

```
python3 manage.py runserver
```

Once these are complete you should be able to point your browser to http://127.0.0.1:8000 and see the Thumbnailer application

Source practice tutorial: https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/
