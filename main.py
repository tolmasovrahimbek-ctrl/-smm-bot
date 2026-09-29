import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8975756356:AAGEnGW5FJQ9eD40MhE4NFEXCcBtcXDwl7I"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Xush kelibsiz! SMM Botimizga marhamat.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
