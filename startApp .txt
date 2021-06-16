@echo off\
set url="http://127.0.0.1:8000"
start chrome %url%
cmd /k "./myvenv/Scripts/activate & python manage.py runserver "