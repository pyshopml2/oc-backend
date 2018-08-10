# Установка проекта
1. [Установить docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. [Установить docker-compose](https://docs.docker.com/compose/install/#install-compose)
3. Клонировать репозиторий
    ```
    git clone https://github.com/pyshopml2/oc-backend.git
    ```
4. Запустить docker-compose в директории oc-backend
    ```
    sudo docker-compose up -d
    ```
5. Произвести анализ моделей
    ```
    sudo docker exec -it django_server python manage.py makemigrations
    ```
6. Применение изменение к базе данных
    ```
    sudo docker exec -it django_server python manage.py migrate
    ```
7. Создать пользователя с правами администратора
    ```
    sudo docker exec -it django_server python manage.py createsuperuser
    ```
8. Проверить доступ к панели управления
    ```
    curl http://127.0.0.1:8000/admin
    ```