# telegram_bot/utils.py


def extract_chat_id_from_message(message):
    """Извлечение chat_id из сообщения"""
    if message and "message" in message:
        return message["message"]["chat"]["id"]
    return None


def extract_text_from_message(message):
    """Извлечение текста из сообщения"""
    if message and "message" and "text" in message["message"]:
        return message["message"]["text"]
    return None


def is_start_command(text):
    """Проверка команды /start"""
    return text and text.startswith("/start")


def parse_start_command(text):
    """Парсинг команды /start"""
    if is_start_command(text):
        parts = text.split()
        if len(parts) > 1:
            return parts[1]
    return None
