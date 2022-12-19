# Pluvo
Requirements:
Python 3
NodeJS
NPM
PIP


# To run this project
python3 -m venv env 
pip install -r requirements.txt

# To generate the tailwind css (this needs to keep running if you are updating the code)
python manage.py tailwind install
python manage.py tailwind start

# To run the django instance
python manage.py runserver


