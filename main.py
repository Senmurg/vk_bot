import logging

from bot.bot_vk import VKBot
from bot.config import TOKEN

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("bot.log", encoding='utf-8'),
            logging.StreamHandler()
        ],
    )

    bot = VKBot(TOKEN)
    bot.run()