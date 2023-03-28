source "venv/$1/bin/activate"
pip install --upgrade pip 
pip install django djangorestframework channels
django-admin startproject backend