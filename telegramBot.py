import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from database import Database
load_dotenv()


API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    firstName = message.from_user.first_name
    lastName = message.from_user.last_name
    username = message.from_user.username
    chatId = str(message.chat.id)

    checkQuery = f"""SELECT * FROM users WHERE chat_id = '{chatId}'"""
    if len(Database.connect(checkQuery, "select")) >= 1:
        await message.reply(f"Hello @{username}")
    else:
        print(f"{firstName} started bot")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{firstName}', '{lastName}', '{username}', '{chatId}')"""
        print(f"{username} {Database.connect(query, "insert")} database")
        await message.reply(f"Hello @{username}")


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

@dp.message_handler(commands=["data"])
async def select(message: types.Message):
    chatID = message.chat.id
    selectQuery = f"SELECT * FROM users WHERE chat_id = '{chatID}'"
    data = Database.connect(selectQuery, "select")
    await message.reply(f"{data}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

