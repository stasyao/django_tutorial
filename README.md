## Учебный проект для закрепления основ Django  

Подробный разбор проекта [здесь](https://gist.github.com/stasyao/587ae01c125b46e25281093b8a982374).  

Инструкция по запуску проекта на своей машине:
1. Скачиваем репозиторий
2. Устанавливаем и активируем виртуальное окружение  
3. Устанавливаем зависимости `pip install -r requirements.txt`  
4. Запустить миграции `python manage.py migrate`  
5. Загрузить данные в базу `python manage.py loaddata fixtures.json`
6. Создать суперюзера для доступа в админку `python manage.py createsuperuser`.  
