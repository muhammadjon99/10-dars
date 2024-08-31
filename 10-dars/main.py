from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from knopkalar import *
storage = MemoryStorage()

bottoken = '6994564433:AAGYtbb-2YwAwntxggzC_I_uXqE3WJKWHBA'
bot = Bot(bottoken)
dp = Dispatcher(bot, storage=storage)

class RegistratsiyState(StatesGroup):
    kurs = State()
    ism = State()
    telefon = State()
    lokatsiya = State()

@dp.message_handler(commands='start')
async def start(message: Message):
    userid = message.from_user.id       
    await bot.send_message(chat_id=userid, text="Xush kelibsiz", reply_markup=asosiyknopka())

@dp.message_handler(text="Kurslar")
async def getkurslar(message: Message):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Kurslar", reply_markup=kurslarbutton())

@dp.message_handler(text="Asosiy menu")
async def getasosiymenu(message: Message):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Asosiy menu", reply_markup=asosiyknopka())

@dp.message_handler(text="Royxatdan o'tish")
async def registrstudent(message: Message):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Kurslarni tanlang.", reply_markup=kurslarbutton())
    await RegistratsiyState.kurs.set()

@dp.message_handler(state=RegistratsiyState.kurs)
async def getkurs(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Ism kiriting.",reply_markup=orqagabutton())
    text = message.text
    await state.update_data(
        {'kurs': text}
    )
    await RegistratsiyState.ism.set()

@dp.message_handler(state=RegistratsiyState.ism)
async def ismolish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Telefon raqamingizni kiriting", reply_markup=orqagabutton())
    text = message.text
    await state.update_data(
        {'ism': text}
    )
    await RegistratsiyState.telefon.set()


@dp.message_handler(state=RegistratsiyState.telefon)
async def telefonolish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Manzil kiriting", reply_markup=orqagabutton())
    text = message.text
    await state.update_data(
        {'telefon': text}
    )
    await RegistratsiyState.lokatsiya.set()


@dp.message_handler(state=RegistratsiyState.lokatsiya)
async def manzilolish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Royxatdan otdingiz", reply_markup=asosiyknopka())
    await state.update_data(
        {'lokatsiya': message.text}
    )
    data = await state.get_data()
    text = (f"🟢🟢🟢🟢Yangi oquvchi🟢🟢🟢🟢\n Ismi: {data['ism']}\n Telefon: {data['telefon']}\n "
            f"Manzil: {data['lokatsiya']}\n Kursi: {data['kurs']}")
    await bot.send_message(chat_id=6829390664, text=text)
    await state.finish()



executor.start_polling(dp, skip_updates=True)
