from aiogram.types import Message


async def test_start_command():
    message = Message(chat={'id': 123}, from_user={
                      'id': 456, 'first_name': 'John'})
    await send_welcome(message)
    assert message.text == 'Введите ваше имя на кириллице:'


async def test_cyrillic_to_latin_valid_input():
    message = Message(chat={'id': 123}, from_user={
                      'id': 456, 'first_name': 'John'}, text='Иван')
    await cyrillic_to_latin(message)
    assert message.text == 'Привет, Ivan!'


async def test_cyrillic_to_latin_invalid_input():
    message = Message(chat={'id': 123}, from_user={
                      'id': 456, 'first_name': 'John'}, text='Иван1')
    await cyrillic_to_latin(message)
    assert message.text == 'Имя может содержать только буквы. Пожалуйста, введите ваше имя еще раз:'


async def test_cyrillic_to_latin_multiple_names():
    message = Message(chat={'id': 123}, from_user={
                      'id': 456, 'first_name': 'John'}, text='Иван, Мария, Петр')
    await cyrillic_to_latin(message)
    assert message.text == 'Привет, Ivan Maria Petr!'
