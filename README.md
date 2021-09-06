## Building

### Python Version

    ~$ python3 --version
    Python 3.8.2

### pip, django

    ~$ python3 -m pip install --upgrade pip
    ~$ pip install django~=3.1.2
    ...
    Successfully installed asgiref-3.2.10 django-3.1.2 pytz-2020.1 sqlparse-0.3.1
    ~$ pip install -r requirements.txt
    ...
    
### Database

    ~/smartdoorlock-backend$ python manage.py makemigrations
    ~/smartdoorlock-backend$ python manage.py migrate
    
### Run Server

    ~/smartdoorlock-backend$ python manage.py runserver
    
http://127.0.0.1:8000/ 로 접속
    
    
