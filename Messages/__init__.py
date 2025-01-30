import logging

def load_welcome_message():
    try:
        with open("messages/welcome.txt", "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        logging.error("Файл welcome_message.txt не найден.")
        return "Здравствуйте!"