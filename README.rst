
Requirements
==========

First of first you need to install: ``python 3.5.2``, ``virtualenv``, ``sqlite3``.

Setup
=========

Get the source code of the project::

    $ git clone git@github.com:borysvorona/glabs.git

Create and fill the environment
-----------------------------

Execute::

    $ cd glabs
    $ virtualenv -p python3 env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Database Configuration
-----------

Creating a database on SQLite::

    $ ./manage.py migrate

Create a super user with a command::

    $ ./manage.py createsuperuser

Launching
------

Now it should work::

    $ ./manage.py runserver
