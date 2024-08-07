.\Script\Activate.ps1

cd ..

cd bibliotheque

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


Normalement après tout ça le projet devrait tourner 

