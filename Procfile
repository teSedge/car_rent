release: python manage.py migrate
web: gunicorn locallibrary.wsgi --log-file -
web: vendor/bin/heroku-php-nginx public/