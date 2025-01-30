import logging
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from .message_handler import MessageHandler
from Messages import load_welcome_message

class VKBot:
    def __init__(self, token):
        self.token = token
        self.vk_session = vk_api.VkApi(token=self.token)
        self.longpoll = VkLongPoll(self.vk_session, mode=2)
        self.vk = self.vk_session.get_api()
        self.users = set()
        self.welcome_message = load_welcome_message()
        self.message_handler = MessageHandler(self.vk)

    def run(self):
        logging.info("Бот запущен")
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if not event.from_me:
                    user_id = event.user_id
                    self.handle_event(user_id, event)

    def handle_event(self, user_id, event):
        try:
            if user_id not in self.users:
                self.message_handler.send_message(user_id, self.welcome_message)
                self.users.add(user_id)

            if event.attachments:
                if  event.attachments['attach1_type'] == 'photo':
                    self.message_handler.send_photo(user_id, event.attachments['attach1'])
                else:
                    pass
        except Exception as e:
            logging.error(f"Ошибка при обработке сообщения от пользователя {user_id}: {e}")
            self.message_handler.send_message(user_id, "Произошла ошибка. Пожалуйста, попробуйте снова.")