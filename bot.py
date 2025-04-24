# bot to send information about what holiday it is
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
import config
import scrap

PREFIX = "!/"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot with default properties
bot = Bot(
    token=config.API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Устанавливаем HTML-разметку по умолчанию
)
dp = Dispatcher()

@dp.message(Command("start", "help"))
async def send_welcome(message: types.Message):
    await message.reply("Hi! Send me /holiday, I'll tell you what holiday is today.")

@dp.message(Command("holiday"))
async def send_holidays(message: types.Message):
    holiday = scrap.get_data(url="https://www.calend.ru/")
    holiday_link = scrap.get_links(url="https://www.calend.ru/")
    await message.reply(
        f'И так, праздники на сегодня и завтра:\n\n'
        f'{holiday[0]}\n{holiday_link[0]}\n\n'
        f'{holiday[1]}\n{holiday_link[1]}\n\n'
        f'Спасибо за предоставленную информацию сайту https://www.calend.ru/'
    )

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())