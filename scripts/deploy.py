#!/usr/bin/env python

import os

# git pull
os.system('git pull')

if not os.path.exists('venv'):
    os.system('pip3 install virtualenv')
    os.system('virtualenv venv')

# install requirements.txt
os.system('venv/bin/pip3 install -r requirements.txt')

# database migrate
os.system('venv/bin/flask db upgrade')

# gunicorn reload
os.system('kill -HUP $(cat app.pid)')

# npm build
os.system('cd openform; yarn build')