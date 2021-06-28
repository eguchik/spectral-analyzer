@echo off\
set url="http://127.0.0.1:8000"
start chrome %url%
cmd /k "myvenv\Scripts\activate & py -3.6 manage.py runserver "