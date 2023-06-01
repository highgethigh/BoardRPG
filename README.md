# MMORPG
## Доска объявлений

1. Запустить виртуальное окружение:

`python3 -m venv venv`

`source venv/bin/activate`

2. Установить программные компоненты из requirements.txt

`pip3 install -r requirements.txt`

3. Установить сервер redis на локальной машине и запустить

`brew install redis`

4. Установить поддержку Redis в Celery

`pip3 install -U "celery[redis]`

`celery -A BoardRPG worker -l info`

5. Запустить Django 

`python3 manage.py runserver`
