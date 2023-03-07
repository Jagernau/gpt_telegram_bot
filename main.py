from settings import bot, USER_ID, USER_NAME
from telebot.types import Message
from utils import get_message, get_pic


@bot.message_handler(content_types=['text'])
def start(message: Message):
    """
    Owner verified.
    When the bot starts, 3 buttons are sent.

    """
    if str(message.from_user.id) == USER_ID and message.from_user.first_name == USER_NAME:

        if "Сгенерируй" or "Создай" or "Generate" in str(message.text) :
            bot.send_photo(
                    str(USER_ID),
                    get_pic(str(message.text)),
                    reply_to_message_id=message.message_id
            )


        else:
            bot.send_message(
                    str(USER_ID), 
                    text=get_message(str(message.text))
             )

bot.polling(none_stop=True, interval=0)
