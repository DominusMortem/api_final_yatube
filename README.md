# API Yatube
API для работы с блогом Yatube

Предоставляет доступ к данным для использования другими разработчиками или программами.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/DominusMortem/api_final_yatube
```

```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
```
```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Зависимости:

```

```

### Примеры запросов:

***Посты***
```
/api/v1/posts/
```
Доступные методы: GET, POST

### GET

### STATUS CODE: 200
 ```
 {
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### POST с парметрами:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
### STATUS CODE: 201
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### STATUS CODE: 400
```
{
  "text": [
    "Обязательное поле."
  ]
}
```

### STATUS CODE: 401
```
{
  "detail": "Учетные данные не были предоставлены."
}
```

***Пост по id***
```
api/v1/posts/{post_id}/
```
Доступные методы: GET, PUT, PATCH, DELETE

### PUT с параметрами
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

### STATUS CODE: 200
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### STATUS CODE: 400
```
{
  "text": [
    "Обязательное поле."
  ]
}
```

### STATUS CODE: 401
```
{
  "detail": "Учетные данные не были предоставлены."
}
```

### STATUS CODE: 403
```
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```

***Комментарии к посту***
```
api/v1/posts/{post_id}/comments/
```

Доступные методы: GET, POST

### GET

### STATUS CODE: 200
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

### STATUS CODE: 404
```
{
"detail": "Страница не найдена."
}
```

***Комментарий к посту***
```
api/v1/posts/{post_id}/comments/{comment_id}/
```

Доступные методы: GET, PUT, PATCH, DELETE

### DELETE

### STATUS CODE: 401
```
{
  "detail": "Учетные данные не были предоставлены."
}
```

### STATUS CODE: 403
```
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```

### STATUS CODE: 404
```
{
  "detail": "Страница не найдена."
}
```


***Список сообществ**
```
api/v1/groups/
```

Доступные методы: GET

### GET

### STATUS CODE: 200
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

***Сообщество***

```
api/v1/groups/{group_id}
```

Доступные методы: GET


***Подписки***
```
api/v1/follow/
```

Доступные методы: GET, POST

### GET

### STATUS CODE: 200
``` [
  {
    "user": "string",
    "following": "string"
  }
]
```

### POST

### STATUS CODE: 200
```
{
  "following": "string"
}
```

#STATUS CODE: 400
```{
  "following": [
    "Обязательное поле."
  ]
}
```


***Получить JWT-токен***
```
api/v1/jwt/create/
```

### POST
```
{
  "username": "string",
  "password": "string"
}
```

### STATUS CODE: 200
```
{
  "refresh": "string",
  "access": "string"
}
```

***Обновить JWT-токен***

```
api/v1/jwt/refresh/
```

### POST
```
{
  "refresh": "string"
}
```

### STATUS CODE: 200
```
{
  "access": "string"
}
```

***Проверить JWT-токен***
```
api/v1/jwt/verify/
```

### POST
```
{
  "token": "string"
}
```

### STATUS CODE: 401
```
{
  "detail": "Token is invalid or expired",
  "code": "token_not_valid"
}
```
