# bot to send information about what holiday it is
import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import scrap

PREFIX = "!/"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! Send me /holiday, I'll tell you what holiday is today.")

@dp.message_handler(commands=['holiday'])
async def send_holidays(message: types.Message):
    holiday = scrap.get_data(url="https://www.calend.ru/")
    holiday_link = scrap.get_links(url="https://www.calend.ru/")
    await message.reply(f'И так, праздники на сегодня и завтра:\n\n{holiday[0]}\n{holiday_link[0]}\n\n{holiday[1]}\n{holiday_link[1]}\n\nСпасибо за предоставленную информацию сайту https://www.calend.ru/')

# start polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)

