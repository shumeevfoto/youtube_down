from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('📹 Скачать видео')
button_load_audio = KeyboardButton('🎶 Скачать аудио')
button_load2 = KeyboardButton('🎓 Название')
button_load3 = KeyboardButton('🚀 Превью')
button_load4 = KeyboardButton('💹 Просмотры')


kb_user = ReplyKeyboardMarkup(resize_keyboard=True)

kb_user.row(button_load, button_load_audio).add(button_load2).row(button_load3, button_load4)