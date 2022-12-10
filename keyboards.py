from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


# создание кнопки photo_confirm / подтверждения фото
def get_photo_confirm() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="✅ Зберігти зображення"),
                KeyboardButton(text="↪ Повернутися назад"),
            ]
        ],
        resize_keyboard=True
    )
    return kb


# создание кнопки Опублікувати / повернення назад
def get_public_confirm() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📩 Опублікувати"),
                KeyboardButton(text="↪ Повернутися назад"),
            ]
        ],
        resize_keyboard=True
    )
    return kb


# создание клавиатур для State / авто отправка команды после нажатия для дальнейшего сравнения
def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👤 Аккаунт"),
                KeyboardButton(text="📦 Річ"),
                KeyboardButton(text="💻 Девайс"),

            ]
        ],
        resize_keyboard=True
    )
    return kb


# создание кнопки Cancel / отмена действий
def get_cancel_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="↪ Повернутися назад"),
            ]
        ],
        resize_keyboard=True
    )
    return kb


# создание клавиатур для State / авто отправка команды после нажатия для дальнейшего сравнения
def get_game_name() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎮 CS:GO"),
                KeyboardButton(text="🎮 Dota 2"),
                KeyboardButton(text="🎮 Інше"),
            ],
            [
                KeyboardButton(text="↪ Повернутися назад"),
            ],
        ],
        resize_keyboard=True
    )
    return kb


# создание клавиатур для State / авто отправка команды после нажатия для дальнейшего сравнения
def get_number() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📲 Поділитися контактом", request_contact=True),
                KeyboardButton(text="↪ Повернутися назад"),
            ],
        ],
        resize_keyboard=True
    )
    return kb


# # создание инлайн кнопок / подтверждния публикации
# public_kb = InlineKeyboardMarkup(row_width=2)
# garantButton = InlineKeyboardMarkup(text='ГАРАНТ ✅', url='https://t.me/Gran1k')
# chatButton = InlineKeyboardMarkup(text='ЧАТ ✅', url='https://t.me/cybermarket_ua')
# public_kb.add(garantButton, chatButton)


# # создание инлайн кнопок / подтверждния публикации
help_kb = InlineKeyboardMarkup(row_width=1)
HELPButton = InlineKeyboardMarkup(text='ДОПОМОГА ✅', url='https://t.me/Gran1k')
help_kb.add(HELPButton)

# # создание инлайн кнопок / подтверждния публикации
join_kb = InlineKeyboardMarkup(row_width=1)
JOINButton = InlineKeyboardMarkup(text='ПРИЄДНАТИСЯ ✅', url='https://t.me/cybermarket_ua')
join_kb.add(JOINButton)
