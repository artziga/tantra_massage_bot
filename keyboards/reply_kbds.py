from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


BACK_BUTTON = KeyboardButton(text="В начало 🔙")

start_buttons = [
    KeyboardButton(text="Смотреть мастеров"),
    KeyboardButton(text="Смотреть анонсы"),
    KeyboardButton(text="Читать статьи"),
]

article_buttons = [
    KeyboardButton(text="Показать случайную статью"),
    KeyboardButton(text="Показать последнюю статью"),
    KeyboardButton(text="Искать статью"),
    BACK_BUTTON,
]

start_keyboard = ReplyKeyboardMarkup(keyboard=[start_buttons], resize_keyboard=True)

article_keyboard = ReplyKeyboardMarkup(keyboard=[article_buttons], resize_keyboard=True)
