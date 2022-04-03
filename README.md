# test_t
Написать Todo

Инструкция по запуску:
1) Склонировать репо
2) Создать локальное окружение
3) Установить модули из src/requirements.txt
4) Создать файл .env внутри src/todo/core как на примере .env.example
5) Миграции:
   1) python src/todo/manage.py makemigrations
   2) python src/todo/manage.py migrate
   3) python src/todo/manage.py migrate_group_permissions
   4) python src/todo/manage.py createsuperuser
   5) python src/todo/manage.py runserver

Админка:
1) http://localhost:8000/admin

Документация:
1) http://localhost:8000/redoc
2) http://localhost:8000/swagger


Задача:
1) Должен быть организации.
2) Создатель организации может добавлять других людей которые зарегистрировались.
3) Доступ для создание проекта в организации.
4) Добавление задач в проектах с привязкой какому-то пользователю с сроком выполнения.


Требование: 
1) Использовать JWT Token Для авторизации
2) Написать Permissions использую perms_map