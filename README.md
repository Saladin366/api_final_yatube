# Учебный проект "API для Yatube"

## API для вымышленной социальной сети "Yatube".

API позволяет авторизованным пользователям создавать, редактировать, удалять
записи (посты), писать комментарии к постам, а также подписываться на авторов
публикаций.

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
source venv/Scripts/activate (Mac)
source venv/bin/activate (Mac)
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
