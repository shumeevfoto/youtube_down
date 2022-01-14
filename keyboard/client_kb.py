from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Меню')
b3 = KeyboardButton('Поделиться телефоном', request_contact=True)
b4 = KeyboardButton('Поделиться моим расположением', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).row(b3, b4)
#kb_client.row(b1, b2)
#kb_client.insert(b1, b2)