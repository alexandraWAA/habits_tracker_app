import requests
from django.conf import settings


def send_message(chat_id, text, parse_mode='HTML'):
    """Отправка сообщения в Telegram"""
    url = f"{settings.TELEGRAM_BOT_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f'Ошибка отправки сообщения: {e}')
        return False


def get_updates(offset=None):
    """Получение обновлений от Telegram"""
    url = f"{settings.TELEGRAM_BOT_URL}{settings.TELEGRAM_BOT_TOKEN}/getUpdates"
    params = {'timeout': 30}
    if offset:
        params['offset'] = offset
    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f'Ошибка получения обновлений: {e}')
        return None