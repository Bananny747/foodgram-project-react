# praktikum_new_diplom

### Запуск проекта локально из образов с Docker hub:

Клонировать репозиторий:
```
git clone https://github.com/Bananny747/foodgram-project-react.git
```

В папкe проекта размещаем файл с секретами (по образцу с .env.example).

Из папки infra/ развернуть контейнеры:

```
docker compose up -d --build
```

Выполнить миграции:

```
docker compose exec backend python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec backend python manage.py createsuperuser
```

Собрать статику:

```
docker compose exec backend python manage.py collectstatic --no-input
```

Собрать статику:

```
docker compose exec backend python manage.py collectstatic --no-input
```

Наполните базу данных ингредиентами

```
docker compose exec backend python manage.py load_data
```

Теги создать в админке