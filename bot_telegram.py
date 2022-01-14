from aiogram import types
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.types import message
from aiogram.utils import executor
from create_bot import dp, bot
from data_base import sqllite_db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# @dp.message_handler(CommandStart())
# async def url(message):
#  markup = types.ReplyKeyboardMarkup()
#  key1 = types.KeyboardButton('START')
#  markup.add(key1)
# @dp.message_handler(commands = ['url'])
# async def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
#     markup.add(btn_my_site)
#     await message.answer("Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)
# async def bot_start(message: types.Message):
#     await message.answer(f'Welcome to the YouTube loader, {message.from_user.full_name}')

async def on_startup(_):
    print('Бот вышел онлайн')
    sqllite_db.sql_start()

    # await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(
    #     InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


'''******************************КЛИЕНСКАЯ ЧАСТЬ*****************************'''
from handlers import youtube, client, admin, other

youtube.register_handlers_youtube(dp)
#client.register_handlers_client(dp)

'''******************************АДМИНСКАЯ ЧАСТЬ*****************************'''

#admin.register_handlers_admin(dp)

'''******************************ОБЩАЯ ЧАСТЬ*********************************'''
# other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
