Install Instructions
=============================

These steps are for running this locally: 

Clone this repository

    git clone https://github.com/Jjack703/DjangoProject-CITP4350.git

Then cd into the directory:: 

    cd DjangoProject-CITP4350

(Python3 is required to install this next portion)

    python3 install virtualenv

    virtualenv env

(Powershell with admin persmission or Powershell Integrated Shell is required for this portion)
(Make sure you are still located in the project directory)

    env/Scripts/activate (WINDOWS)
    
OR

    source env/bin/activate (LINUX/MAC)

Once the virtual environment is active, install the dependencies::

    pip3 install -r requirements.txt

If there are no errors, we can move forward while continuing to work within the virtual environment named: "env"

These two commands may not be needed depending on how it was installed.
Ignore any failed messages and continue to the runserver command.

    python manage.py makemigrations
    python manage.py migrate

Start the server

    python manage.py runserver 8080

Once it starts running, test the site at http://127.0.0.1:8080/ or http://localhost:8080

<b>Prebuilt usernames and passwords for testing:</b>

User: admin 

Password: password 

OR

User: TesterD

Password: password



# Final Project
  This project is built to be an inventory management platform as well as a point of sale for customers in a SaaS format. I will be utilizing scafollding techniques to built a folder structure, authentication process and for a foundation of basic CRUD (Create Read Update Delete) actions. Once the scaffolding is complete, I will manually write all functions, routing, imports, db models(schema), and  design of the site. 

# Languages Used:
  -Python
  
  -SQL
  
  -HTML
  
  -CSS
  
  -JS
  
# Frameworks
  -Django (Python)
  
  -SQL (SQLite -> postgreSQL)
  
  -MDBootstrap (CSS&JS)

# Libraries 
  -autopep8==1.4.4
  
  -certifi==2019.3.9
  
  -chardet==3.0.4
  
  -defusedxml==0.6.0
  
  -Django==2.2.10
  
  -django-allauth==0.39.1
  
  -django-countries==5.3.3
  
  -django-crispy-forms==1.7.2
  
  -django-debug-toolbar==1.10.1
  
  -idna==2.8
  
  -oauthlib==3.0.1
  
  -pep8==1.7.1
  
  -Pillow==6.2.0
  
  -pycodestyle==2.5.0
  
  -python-decouple==3.1
  
  -python3-openid==3.1.0
  
  -pytz==2018.5
  
  -requests==2.21.0
  
  -requests-oauthlib==1.2.0
  
  -sqlparse==0.2.4
  
  -stripe==2.27.0
  
  -urllib3==1.24.2

