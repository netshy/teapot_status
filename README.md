# Teapot status

## Описание
Скрипт написан для того, чтобы проверять статус моего чайника в ремонте на сайте http://itetss.asuscomm.com/status/. С уведомлением в телеграмме.

## Стек технологий
- Python
- Python-telegram-bot
- BeautifulSoup
- Docker

## Как запустить скрипт:
1) Клонируйте репозиторий с проектом:
```
git clone https://github.com/netshy/teapot_status.git
```
2) В директории проекта создайте файл .env, по пути `<project_name>/.env`, в котором пропишите следующие переменные окружения:
- TELEGRAM_TOKEN = Токен бота
- CHAT_ID = номер вашего id в телеграмме 
- RECEIPT_NUMBER = номер квитанции из СЦ


3) С помощью Dockerfile разверните проект:

Перейдите в директорию проекта
```
cd teapot_status
```
Запустите билд и дошдитесь успешной сборки
```
docker build .
```
Запустите контейнер
```
docker run -d <image_id>
```

### Запуск без Docker-а
Установите виртуальное окружение и зависимости из requirements.txt. После можно запускать скрипт.
```
python main.py
```
