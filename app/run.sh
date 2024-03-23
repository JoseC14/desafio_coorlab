#!/bin/bash
pip install django
pip install djangorestframework
pip install django-cors-headers

npm install @vue/cli

cd backend
python manage.py runserver 3000 &

cd ../
cd frontend/core
npm run serve
