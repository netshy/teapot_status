import os
import sys
import time
import requests

import telegram
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def take_url(url, data):
    request = requests.post(url, data)
    request.encoding = 'cp1251'
    return request.text


def take_all_text(html):
    soup = BeautifulSoup(html, 'html.parser').get_text()
    return soup


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    return bot.send_message(chat_id=CHAT_ID, text=message)


def main():
    while True:
        try:
            url = 'http://itetss.asuscomm.com/status/'
            data = {'kvit': '46759'}
            html = take_url(url, data)
            page = take_all_text(html)

            if 'Статус:ОЖИДАЕТ ЗАПЧАСТИ' not in page:
                send_message(message=page)
                sys.exit()

            time.sleep(1200)

        except KeyboardInterrupt:
            print('Прерывание с клавиатуры')
            sys.exit()

        except Exception as e:
            send_message(f'Скрипт упал с ошибкой: {e}')
            time.sleep(600)


if __name__ == '__main__':
    main()
