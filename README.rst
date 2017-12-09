
Требования
==========

Руками надо поставить: ``python 3.5.2``, ``virtualenv``, ``sqlite3``.

Подразумевается, что в системе установлен свежий ``pip`` и через него поставлен ``virtualenvwrapper``.

Установка
=========

Получаем исходный код проекта::

    $ git clone git@github.com:borysvorona/glabs.git

Создаём и наполняем окружение
-----------------------------

Выполняем::

    $ cd glabs
    $ virtualenv -p python3 env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Конфигурация базы данных
-----------

Создаем базу данных на SQLite::

    $ ./manage.py migrate

Создаем супер-пользователя командой::

    $ ./manage.py createsuperuser

Запуск
------

Теперь должно работать::

    $ ./manage.py runserver
