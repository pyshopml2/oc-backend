# Установка проекта
1. [Установить docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. [Установить docker-compose](https://docs.docker.com/compose/install/#install-compose)
3. Клонировать репозиторий
    ```
    git clone https://github.com/pyshopml2/oc-backend.git
    ```
4. Выберем ветку master
    ```
    git checkout master
    ```
5. Создадим новую директорию рядом с Dockerfile
    ```
    mkdir Docker/crm
    ```
6. Создадим точку монтирования в директории oc-backend
    ```
    mount --bind /crm /Docker/crm
    ```
7. Построим проект и установим зависимости
    ```
    docker-compose build
    ```
8. Запустим наш docker-compose в режиме демона
    ```
    sudo docker-compose up -d
    ```
9. Произведем анализ моделей
    ```
    sudo docker exec -it django_server python manage.py makemigrations
    ```
10. Примененим изменения к базе данных
    ```
    sudo docker exec -it django_server python manage.py migrate
    ```
11. Создадим пользователя с правами администратора
    ```
    sudo docker exec -it django_server python manage.py createsuperuser
    ```
12. Проверим доступ к панели управления
    ```
    curl http://127.0.0.1:8000/admin
    ```