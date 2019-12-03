===========
Kele API
===========

Setup
======

1. Create virtual environment::

    virtualenv --python=python3.7 venv

2. Activate virtual environment::

    source venv/bin/activate

3. Install dependencies::

    pip install -r requirements.txt

4. Create media root directory::

    mkdir -p /var/www/kele/media
    chmod -R 777 /var/www/kele/

5. Run migrations::

    python manage.py migrate

6. Run the project::

    python manage.py runserver

