# Учебный проект "API для Yatube"

## API для вымышленной социальной сети "Yatube".

API даёт возможность добавления новых пользователей, позволяет создавать,
редактировать, удалять записи (посты), писать комментарии к постам, а также
подписываться на авторов публикаций.

Проект реализован на Django REST Framework.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Saladin366/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

или

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Документация к API:

```
http://127.0.0.1:8000/redoc/
```

Регистрация нового пользователя:

```
http://127.0.0.1:8000/api/v1/users/
```