#!/bin/bash
if [ "default" == "$1" ]; then
    echo "use settings: $1"
    python manage.py runserver 0.0.0.0:8000
else
    echo "use settings: settings_dev.py$1"
    python manage.py runserver 0.0.0.0:8000 --settings=dj151site.settings_dev
fi
