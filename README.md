# Preventrivia

Preventrivia is a platform built to help neighborhoods looking to improve their life-saving
prevention systems.

Built with Django (backend) and Ionic (frontend).
### Execution instructions:
  - git clone https://github.com/pierorex/preventrivia.git
  - Backend
    ```
    
    $ cd preventrivia/backend/preventrivia_backend
    
    $ sudo pip3 install -r requirements.txt
    
    $ python3 manage.py migrate
    
    $ python3 manage.py makemigrations polls
    
    $ python3 manage.py migrate
    
    $ python3 manage.py loaddata fixtures

    $ python3 manage.py runserver 0.0.0.0:8000
    

    ```
  - Frontend
    ```
    
    $ cd preventrivia/frontend/
    
    $ install the ionic framework
    
    $ sh ionic-serve.sh
    ```
Now you should be able to open http://localhost:8000/admin to enter the django administration
site and http://localhost:8100 to access the ionic app
