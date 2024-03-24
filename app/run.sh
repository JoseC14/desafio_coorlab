#!/bin/bash

cd ../
pip install django
pip install djangorestframework
pip install django-cors-headers

npm install -g @vue/cli
npm install axios

cd app/frontend/core
npm install

cd ../../
cd backend
python manage.py runserver 3000 &

cd ../
cd frontend/core
npm run serve

