import asyncio, logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from config import token

bot = Bot(token=token)
dp = Dispatcher()

start_button = [
    [KeyboardButton(text='Geeks направления'), KeyboardButton(text='Geeks контакты')]
]
start_keybord = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True)

start_button_1 = [
    [KeyboardButton(text='BACKEND'), KeyboardButton(text='FRONTENT')],
    [KeyboardButton(text='UX/UI'), KeyboardButton(text='ANDROID')],
]
start_keybord_1 = ReplyKeyboardMarkup(keyboard=start_button_1, resize_keyboard=True)

start_button_2 = [
    [KeyboardButton(text='INSTAGRAM'), KeyboardButton(text='TELEGRAM')]
]    
start_keybord_2 = ReplyKeyboardMarkup(keyboard=start_button_2, resize_keyboard=True)

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("добро пожаловать, выберитье действие", reply_markup=start_keybord)

@dp.message(F.text == 'Geeks контакты')
async def contact(message:Message):
    await message.answer("Наши контакты: ", reply_markup=start_keybord_2 )

@dp.message(F.text == 'INSTAGRAM')
async def contact(message:Message):
    await message.answer("geeks.bitrix24site.ru/tiktokOsh")

@dp.message(F.text == 'TELEGRAM')
async def contact(message:Message):
    await message.answer("@geeks_osh")

@dp.message(F.text == 'Geeks направления')
async def star(message:Message):
    await message.answer('Наши направление:', reply_markup=start_keybord_1)

@dp.message(F.text == 'BACKEND')
async def star(message:Message):
    await message.answer("""Back-end — это код, который выполняется на сервере,
    который получает запросы от клиентов и содержит логику для отправки соответствующих
    данных обратно клиенту. Back-end также включает базу данных, которая будет постоянно 
    хранить все данные для приложения. В этой статье основное внимание уделяется 
    оборудованию и программному обеспечению на стороне сервера, которые делают это возможным.""")

@dp.message(F.text == 'FRONTENT')
async def star(message:Message):
    await message.answer("""Front-end — это код, который выполняется
     на стороне клиента. Этот код (обычно HTML, CSS и JavaScript)
     выполняется в браузере пользователя и создает пользовательский 
    интерфейс.""")

@dp.message(F.text == 'UX/UI')
async def star(message:Message):
    await message.answer('Пользовательский опыт (UX) относится к пути пользователя при взаимодействии с продуктом или услугой. UX-дизайн — это процесс создания продуктов или услуг, которые обеспечивают значимый опыт для пользователей, включающий множество различных областей разработки продукта, включая брендинг, удобство использования, функциональность и дизайн.')

@dp.message(F.text == 'ANDROID')
async def star(message:Message):
    await message.answer("Android — операционная система для смартфонов, планшетов, электронных книг, цифровых проигрывателей, наручных часов, фитнес-браслетов, игровых приставок, ноутбуков, нетбуков, смартбуков, очков Google Glass, телевизоров, проекторов и других устройств.")   

async def main():
    logging.basicConfig(level='INFO')
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

