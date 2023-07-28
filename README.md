<h1 align="center">Foodgram</h1>

# Описание проекта

Сайт Foodgram, «Продуктовый помощник». Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Проект доступен в сети: https://easypeasy.hopto.org/
Админка
логин: admin
пароль: admin


### Технологии:

Python, Django, Django Rest Framework, Docker, Gunicorn, NGINX, PostgreSQL, Yandex Cloud, Continuous Integration, Continuous Deployment


### Запуск проекта локально из контейнеров Docker:

Проект будет доступен по локальному адресу - http://127.0.0.1:8001/

Клонировать репозиторий:
```
git clone https://github.com/Bananny747/foodgram-project-react.git
```

В папкe проекта размещаем файл с секретами (по образцу с .env.example).

Из папки infra/ развернуть контейнеры:

```
docker compose -f docker-compose.yml up -d --build
```

Выполнить миграции:

```
docker compose -f docker-compose.yml exec backend python manage.py migrate
```

Создать суперпользователя:

```
docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```

Собрать статику и скопировать статику:

```

docker compose -f docker-compose.yml exec backend python manage.py collectstatic

docker compose -f docker-compose.yml exec backend cp -r collected_static/. ../backend_static/static/
```

Наполните базу данных ингредиентами

```
docker compose exec backend python manage.py load_data
```

Теги создать в админке


### Примеры запросов к эндпоинтам

**`POST` | Создание рецепта: `http://127.0.0.1:8001/api/recipes/`**

Request:
```
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```

**`POST` | Подписаться на пользователя: `http://127.0.0.1:8000/api/users/{id}/subscribe/`**


## Автор 

Алексей Филин (bananny747) 