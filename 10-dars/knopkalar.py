from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def asosiyknopka():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Royxatdan o'tish"),
        KeyboardButton(text="Kurslar")
    )
    return markup

def kurslarbutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text="Python"),
        KeyboardButton(text="Grafik dizayn"),
        KeyboardButton(text="Autocad"),
        KeyboardButton(text="Kompyuter savodxondligi"),
    )
    markup.add(
        KeyboardButton(text="Asosiy menu")
    )
    return markup

def orqagabutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text="Asosiy menu")
    )
    return markup
