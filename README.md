# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

## Как установить

Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся `HOST`, `PORT`, `USER`, `PASSWORD`, `SECRET_KEY`.
Прейдите в директорию с проектом. Откройте папку project. Внутри папки кликните на свободном месте правой клавишей мыши и в контекстном меню кликните на "Текстовый документ". 
На данный момент в настройках Вашей системы должно быть разрешено менять расширение файлов. 
Создайте текстовый файл с названием ".env". С помощью редактора кода Sublime (www.sublimetext.com) откройте файл ".env" и задайте значения параметров по примеру, показанному ниже, подставив свои значения.  

```ENGINE=django.db.backends.postgresql_psycopg2
HOST=checkpoint.devman.org
PORT=5434
NAME=checkpoint
USER=guard
PASSWORD=osim5
SECRET_KEY=REPLACE_ME
DEBUG=False```

Измените значения `HOST`, `PORT`, `USER`, `PASSWORD`, `SECRET_KEY` на те, которые выдал менеджер. Значения `ENGINE`, `NAME` и `DEBUG` оставьте без изменений. Закройте файл .env с сохранением изменений.

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`

Используя командную строку перейдите в папку с проектом и запустите команду `python manage.py runserver`.
Сайт запустится по адресу http://127.0.0.1:8000

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](http://dvmn.org).
