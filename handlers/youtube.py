import os

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
    get_youtube_piple, to_valid, worker, get_audio


class FSMClient(StatesGroup):
    down_st = State()
    down_st_audio = State()
    title_st = State()
    thumb_st = State()
    quantity_st = State()


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=kb_user)



#@dp.message_handler(Text(equals='📹 Скачать видео'))
async def upload_video(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ссылку')
    await FSMClient.down_st.set()


#@dp.message_handler(state=FSMClient.down_st)
async def thanks_video_upload(message: types.Message, state: FSMContext):
    res = message.text
    VID_ID = ''
    to_valid(res)
    await bot.send_message(message.from_user.id, 'Начинаем загрузку видео...')
    print(VID_ID)
    get_yotybe_360(res)
    await bot.send_video(message.from_user.id, open('video.mp4', 'rb'))
    await state.reset_state()
    os.remove('video.mp4')  # удаляем видео на диске в целях жкономии места


#@dp.message_handler(Text(equals='📹 Скачать аудио'))
async def upload_audio(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ссылку')
    await FSMClient.down_st_audio.set()


#@dp.message_handler(state=FSMClient.down_st_audio)
async def thanks_video_audio(message: types.Message, state: FSMContext):
    res = message.text
    VID_ID = ''
    to_valid(res)
    await bot.send_message(message.from_user.id, 'Начинаем загрузку аудио...')
    get_audio(res)
    await bot.send_audio(message.from_user.id, open('audio.mp4', 'rb'))
    await state.reset_state()
    os.remove('audio.mp4')  # удаляем аудио на диске в целях жкономии места


#@dp.message_handler(Text(equals='🎓 Название'))
async def upload_video_title(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ссылку')
    await FSMClient.title_st.set()


#@dp.message_handler(state=FSMClient.title_st)
async def thanx_video_title(message: types.Message, state: FSMContext):
        res = message.text
        async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
            proxy['title_st1'] = res
        title = get_youtube_title(proxy['title_st1'])
        await message.answer(f'Название вашего видео: {title}')
        await state.reset_state()


#@dp.message_handler(Text(equals='🚀 Превью'))
async def upload_video_thumb(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ссылку')
    await FSMClient.thumb_st.set()


#@dp.message_handler(state=FSMClient.thumb_st)
async def thanx_video_thumb(message: types.Message, state: FSMContext):
        res = message.text
        async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
            proxy['thumb_st1'] = res
        thumb = get_youtube_thumb(proxy['thumb_st1'])
        #await message.answer(f'Превью вашего видео: {thumb}')
        await bot.send_photo(message.from_user.id, f'{thumb}')
        await state.reset_state()

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
        await state.reset_state()



def register_handlers_youtube(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(upload_video, Text(equals='📹 Скачать видео'))
    dp.register_message_handler(thanks_video_upload, state=FSMClient.down_st)
    dp.register_message_handler(upload_audio, Text(equals='🎶 Скачать аудио'))
    dp.register_message_handler(thanks_video_audio, state=FSMClient.down_st_audio)
    dp.register_message_handler(upload_video_title, Text(equals='🎓 Название'))
    dp.register_message_handler(thanx_video_title, state=FSMClient.title_st)
    dp.register_message_handler(upload_video_thumb, Text(equals='🚀 Превью'))
    dp.register_message_handler(thanx_video_thumb, state=FSMClient.thumb_st)
    dp.register_message_handler(upload_video_quatity, Text(equals='💹 Просмотры'))
    dp.register_message_handler(thanx_video_quatity, state=FSMClient.quantity_st)



