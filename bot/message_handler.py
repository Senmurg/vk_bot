import logging
import time
from random import randint

from pyexpat.errors import messages


class MessageHandler:
    def __init__(self, vk):
        self.vk = vk

    def send_message(self, user_id, message):
        try:
            self.vk.messages.send(
                user_id=user_id,
                message=message,
                random_id=int(time.time() * 1000) + randint(0, 999),
            )
            logging.info(f"Сообщение отправлено пользователю {user_id}: {message}")
        except Exception as e:
            logging.error(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

    def send_photo(self, user_id, photo):
        try:
            attachment = f"photo{photo}"
            self.vk.messages.send(
                user_id=int(user_id),
                attachment=attachment,
                random_id=int(time.time() * 1000) + randint(0, 999),
            )
            logging.info(f"Фото отправлено пользователю {user_id}.")
        except Exception as e:
            logging.error(f"Ошибка при отправке фото пользователю {user_id}: {e}")