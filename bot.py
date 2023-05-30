import logging

from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    text = "Введите ваше имя:"
    await message.reply(text)
    logging.info(f'{name=} {user_id=} sent messages: {message.text}')


@dp.message_handler()
async def cyrillic_to_latin(message):
    name = message.text.strip()

    if not all(char.isalpha() or char.isspace() for char in name):
        text = "Имя может содержать только буквы. Пожалуйста, введите ваше имя еще раз:"
        await message.reply(text)
        logging.info(f'{message.from_user.id=} entered invalid input')
        return

    words = name.split()
    output = []

    for word in words:
        translit_table = {'а': 'A', 'б': 'B', 'в': 'V', 'г': 'G', 'д': 'D', 'е': 'E', 'ё': 'YO',
                          'ж': 'ZH', 'з': 'Z', 'и': 'I', 'й': 'Y', 'к': 'K', 'л': 'L', 'м': 'M',
                          'н': 'N', 'о': 'O', 'п': 'P', 'р': 'R', 'с': 'S', 'т': 'T', 'у': 'U',
                          'ф': 'F', 'х': 'H', 'ц': 'TS', 'ч': 'CH', 'ш': 'SH', 'щ': 'SHCH', 'ъ': 'IE',
                          'ы': 'Y', 'ь': '', 'э': 'E', 'ю': 'IU', 'я': 'IA'}

        result = ''
        for char in word.lower():
            if char in translit_table:
                result += translit_table[char]
            else:
                result += char

        output.append(result.capitalize())

    text = f'Ваше имя на латинице: {" ".join(output)}'
    await message.reply(text)
    logging.info(f'{message.from_user.id=} sent messages: {text}')


if __name__ == '__main__':
    executor.start_polling(dp)
