from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import StatesGroup, State

from create_bot import bot, dp
from keyboard import kb_client
from keyboard import kb_user
from data_base import sqllite_db
from func_youtube import yotube_result, playlist_video_id
from youtube_down import get_youtube_title, get_yotybe_hd, get_yotybe_360, get_yotybe_720, get_youtube_thumb, \
    get_youtube_piple


class FSMClient(StatesGroup):
    down_st = State()
    title_st = State()
    thumb_st = State()
    quantity_st = State()


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=kb_user)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/wedmoment_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'наш режим работы')


# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqllite_db.sql_read(message)


# @dp.message_handler(Text(equals='📹 Скачать видео'))
# async def upload_video(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Введите ссылку')
#     await FSMClient.down_st.set()
#
#
# @dp.message_handler(state=FSMClient.down_st)
# async def thanks_video_upload(message: types.Message, state: FSMContext):
#     res = message.text
#     VID_ID = ''
#     #to_valid(res, VID_ID)
#     #print(res, VID_ID)
#     await bot.send_message(message.from_user.id, 'Начинаем загрузку видео...')
#     get_yotybe_360(res, VID_ID)
#     await bot.send_video(message.from_user.id, open('Cn0sMvgqf4E.mp4', 'rb'))


@dp.message_handler(Text(equals='🎓 Название'))
async def upload_video_title(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ссылку')
    await FSMClient.title_st.set()


    @dp.message_handler(state=FSMClient.title_st)
    async def thanx_video_title(message: types.Message, state: FSMContext):
        res = message.text
        async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
            proxy['title_st1'] = res
        title = get_youtube_title(proxy['title_st1'])
        await message.answer(f'Название вашего видео: {title}')



@dp.message_handler(Text(equals='🚀 Превью'))
async def upload_video_thumb(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ссылку')
    await FSMClient.thumb_st.set()


    @dp.message_handler(state=FSMClient.thumb_st)
    async def thanx_video_thumb(message: types.Message, state: FSMContext):
        res = message.text
        async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
            proxy['thumb_st1'] = res
        thumb = get_youtube_thumb(proxy['thumb_st1'])
        await message.answer(f'Превью вашего видео: {thumb}')


@dp.message_handler(Text(equals='💹 Просмотры'))
async def upload_video_quatity(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ссылку')
    await FSMClient.quantity_st.set()


    @dp.message_handler(state=FSMClient.quantity_st)
    async def thanx_video_quatity(message: types.Message, state: FSMContext):
        res = message.text
        async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
            proxy['quantity_st1'] = res
        quantity = get_youtube_piple( proxy['quantity_st1'])
        await message.answer(f'Колличество просмотров этого видео: {quantity}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
