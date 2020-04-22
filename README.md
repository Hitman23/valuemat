# valuemat

## REQUIREMENTS

[git](http://git-scm.com)
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)


## DEVELOPMENT

    # Clone secrets and fablib repositories
    git clone git@github.com:mtcaddy/valuemat.git

    # Change into project directory
    cd valuemat

    # Make virtual environment
    mkvirtualenv -ppython3 valuemat

    # Activate virtual environment
    workon valuemat

    # Install requirements
    pip3 install -r requirements.txt
    
    # Create the database
    createdb valuemat
    
    # set the proper DJANGO_SETTINGS_MODULE
    export DJANGO_SETTINGS_MODULE=services.settings.local
    
    # Migrate
    python manage.py migrate
    
    # Install Node Packages
    npm install
    
    # Start the development server
    python manage.py runserver


## REQUIRED ENVIRONMENT VARIABLES:

- DJANGO_SETTINGS_MODULE
- DJANGO_SECRET_KEY
- WORKON_HOME (set manually if not using mkvirtualenv)

## NOTE:
-In order to do cross origin resource sharing requests, you have to whitelist the requesting domain in the settings.

