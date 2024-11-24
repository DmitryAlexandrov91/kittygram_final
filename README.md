![Main Kittygram Workflow](https://github.com/DmitryAlexandrov91/kittygram_final/actions/workflows/main.yml/badge.svg)

# Kittygram

Kittygram — это веб-приложение, позволяющее пользователям делиться фотографиями своих котиков. Зарегистрировавшись на платформе, пользователи могут загружать фотографии своих пушистых друзей и добавлять их достижения. 

## Функции приложения

- Регистрация и аутентификация пользователей
- Загрузка фотографий кошек с возможностью добавления описания
- Просмотр галереи фотографий других пользователей
- Добавление невероятных достижений своих котеек 

## Стек технологий

### Backend

- Python
- PostgreSQL (база данных)
- Gunicorn (WSGI-сервер)
- Nginx

### Frontend

- HTML/CSS
- JavaScript (ES6+)
- Bootstrap (CSS-фреймворк)

### Инструменты разработки

- Docker (контейнеризация)
- Git (система контроля версий)

## Развертывание проекта

1. Клонируйте репозиторий:

   
   git clone https://github.com/DmitryAlexandrov91/kittygram_final.git
   

2. Перейдите в директорию проекта:

   
   cd kittygram
   

3. Запустите контейнеры с помощью Docker Compose:

   
   docker-compose up -d

4. Выполнить следующие команды внутри запущенного контейнера backend:
 - docker compose -f docker-compose.yml exec backend python manage.py migrate
 - docker compose -f docker-compose.yml exec backend python manage.py collectstatic
 - docker compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /backend_static/static/

Если вы работаете по системой Linux или MacOs не забывайте добавить в начало команда sudo.

4. После успешного запуска контейнеров приложение будет доступно по адресу http://localhost:9000/

## Настройка переменных окружения (.env)

Создайте файл .env в корневой директории проекта и добавьте следующие переменные:

- POSTGRES_DB=kittygram
- POSTGRES_USER=kittygram_user
- POSTGRES_PASSWORD=kittygram_password
- DB_NAME=kittygram
- DB_HOST=db
- DB_PORT=5432
- SECRET_KEY = секретный код проекта
- DEBUG = запуск проекта в режиме отладки 'True' или 'False'  
- ALLOWED_HOSTS = Строка из URL адресов проекта через запятю. Например 'my-kitty.org, 89.899.899.89'

## Автор

Александров Дмитрий Александрович

<u>GitHub</u>
 - https://github.com/DmitryAlexandrov91
