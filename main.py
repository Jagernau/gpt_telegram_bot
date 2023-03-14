from settings import dp, types, USER_ID, USER_NAME, bot, executor
from utils import get_message


@dp.message_handler(content_types=["text"])
async def gpt_message(message: types.Message):
    """
    Owner verified.
    When the bot starts, 3 buttons are sent.

    """
    if (
        str(message.from_user.id) == USER_ID
        and message.from_user.first_name == USER_NAME
    ):
        try:
            gpt_result = get_message(str(message))
            if len(gpt_result) > 3096:
                for x in range(0, len(gpt_result), 3096):
                    await bot.send_message(str(USER_ID), text=gpt_result[x : x + 3096])
            else:
                await bot.send_message(str(USER_ID), gpt_result)

        except BaseException:
            await bot.send_message(str(USER_ID), text="Что то с переданным текстом")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
