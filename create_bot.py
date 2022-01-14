from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

#TOKEN = '5042805055:AAF7f5pdbO3t9UCoAodouj4irXdzUMhf1cA'
TOKEN = '5086992664:AAH-Ep3-zmxynwMr_cw_6gsQQ4i_9Z7taA0'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
