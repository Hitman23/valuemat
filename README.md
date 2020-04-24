# KIPYA | Valuemat
Resosuce map link

## REQUIREMENTS

[git](http://git-scm.com)
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

```bash
pip install virtualenv virtualenvwrapper 
```


add it to shell startup file (.zshrc):

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/dev
source /usr/local/bin/virtualenvwrapper.sh
```

## DEVELOPMENT

# Clone secrets and fablib repositories
git clone git@github.com:mtcaddy/valuemat.git

# Change into project directory
cd valuemat

# Make virtual environment
mkvirtualenv -p python3 valuemat

# Activate virtual environment
workon valuemat

# Install requirements
pip3 install -r requirements.txt


# export DJANGO_SETTINGS_MODULE
```bash
    export DJANGO_SETTINGS_MODULE=5453949390evbdg93i94iri390
```
    
# set the proper DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE=services.settings.local

# Create the database
createdb valuemat

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
*In order to do cross origin resource sharing requests, you have to whitelist the requesting domain in the settings.

## Errors

* ERROR: jupyter-console 6.1.0 has requirement prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0, but you'll have prompt-toolkit 1.0.18 which is incompatible.
