import time

from aiogram.types import ReplyKeyboardRemove, MediaGroup

from create_bot import bot, db, chat_id
from default_commands import AccountStatesGroup, CooldownStatesGroup, ParametersStatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import get_photo_confirm, get_public_confirm, get_cancel_kb, get_number


# # @dp.message_handler(text_contains="💻 Девайс", state=ParametersStatesGroup.parameter)
async def cmd_create(message: types.Message):
    await message.reply('Напиши невеличкий опис для нього:',
                        reply_markup=get_cancel_kb())
    await AccountStatesGroup.description.set()


# сохранения + ожидание ввода пользователем / новый вопрос + смена state
# @dp.message_handler(state=AccountStatesGroup.description)
async def load_desc(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['description'] = message.text

    await message.reply('Введи ціну:')
    await AccountStatesGroup.next()


# сохранения + ожидание ввода пользователем / новый вопрос + смена state
async def load_price(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['price'] = message.text

    await message.reply('Прикріпи декілька фото (не більше 10-и):',
                        reply_markup=get_photo_confirm())
    await AccountStatesGroup.next()
    async with state.proxy() as data:
        data['photo'] = 0


# # @dp.message_handler(text_contains="✅ Це все, зберігти зображення", state=AccountStatesGroup.photo)
async def photo_confirm(message: types.Message, state: FSMContext):
    await message.reply('Натисніть поділитися контактом:',
                        reply_markup=get_number())
    await AccountStatesGroup.next()
    async with state.proxy() as data:
        data['name'] = 0


# сохранения + ожидание ввода пользователем (фото) / новый вопрос + смена state
# @dp.message_handler(content_types=types.ContentType.ANY, state=AccountStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    if message.photo:
        photo_file = message.photo[-1].file_id
        async with state.proxy() as data:
            data['photo'] = data['photo'] + 1
        if data['photo'] == 1:
            column = 1
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 2:
            column = 2
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 3:
            column = 3
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 4:
            column = 4
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 5:
            column = 5
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 6:
            column = 6
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 7:
            column = 7
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 8:
            column = 8
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 9:
            column = 9
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Фото додано. Ще одне?')
        elif data['photo'] == 10:
            column = 10
            await db.sql_update_photo(column, photo_file, user_id=message.from_user.id)
            await message.reply(f'Ви досягли ліміту – 10 из 10.')
    else:
        await message.reply('Прикріпи будь ласка файл типу - "фото"')


# # @dp.message_handler(text_contains="📩 Опублікувати", state=AccountStatesGroup.name)
async def public_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        album = MediaGroup()
        first_photo = True
        photos_list = await db.get_photos(message.from_user.id)
        count = 0
        if data['photo'] == 0:
            album.attach_photo(photo=types.InputFile('media/logo.jpg'),
                               caption=f"<b>📝┃Info</b>: {data['description']}"
                                       f"\n\n<b>💰┃Price</b>: "
                                       f"{data['price']}\n\n<b>🔰┃{data['name']}</b> "
                                       f"\n\n<b><a href='https://t.me/Cybermarketua_bot'>ЗРОБИТИ ПОСТ"
                                       f"</a>┃<a href='https://t.me/+FIt6jHaovdJmYzky'>ЧАТ</a></b> "
                                       f"\n\n<i>#аккаунт_з_іграми</i>",
                               parse_mode="HTML")
            await bot.send_media_group(chat_id=chat_id, media=album)
        else:
            for photo_file in photos_list:
                if count < data['photo']:
                    count += 1
                    if first_photo:
                        album.attach_photo(photo=photo_file,
                                           caption=f"<b>📝┃Info</b>: {data['description']}"
                                                   f"\n\n<b>💰┃Price</b>: "
                                                   f"{data['price']}\n\n<b>🔰┃{data['name']}</b> "
                                                   f"\n\n<b><a href='https://t.me/Cybermarketua_bot'>ЗРОБИТИ ПОСТ"
                                                   f"</a>┃<a href='https://t.me/+FIt6jHaovdJmYzky'>ЧАТ</a></b> "
                                                   f"\n\n<i>#аккаунт_з_іграми</i>",
                                           parse_mode="HTML")
                        first_photo = False
                    else:
                        album.attach_photo(photo=photo_file)
            await bot.send_media_group(chat_id=chat_id, media=album)
    await message.answer('Для нового запиту на продажу введіть: «/start»',
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()

    await CooldownStatesGroup.cooldown_timer.set()
    cooldown_timer = time.time()
    await db.sql_update_time(cooldown_timer, user_id=message.from_user.id)


# сохранения + ожидание ввода пользователем / новый вопрос + смена state
# @dp.message_handler(state=AccountStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        if data['name'] == 0:
            if message.from_user.username:
                data['name'] = f'@{message.from_user.username}'
            elif message.contact.user_id == message.from_user.id:
                data['name'] = message.contact.phone_number
            album = MediaGroup()
            first_photo = True
            photos_list = await db.get_photos(message.from_user.id)
            count = 0
            if data['photo'] == 0:
                album.attach_photo(types.InputFile('media/logo.jpg'),
                                   caption=f"<b>📝┃Info</b>: {data['description']}"
                                           f"\n\n<b>💰┃Price</b>: "
                                           f"{data['price']}\n\n<b>🔰┃{data['name']}</b> ",
                                   parse_mode="HTML")

                await message.answer_media_group(media=album)
            else:
                for photo_file in photos_list:
                    if count < data['photo']:
                        count += 1
                        if first_photo:
                            album.attach_photo(photo=photo_file,
                                               caption=f"<b>📝┃Info</b>: {data['description']}"
                                                       f"\n\n<b>💰┃Price</b>: "
                                                       f"{data['price']}\n\n<b>🔰┃{data['name']}</b> ",
                                               parse_mode="HTML")

                            first_photo = False
                        else:
                            album.attach_photo(photo=photo_file)
                await message.answer_media_group(media=album)
            await message.reply('Все правильно ? Тоді натискай - "📩 Опублікувати"', reply_markup=get_public_confirm())


def register_handlers_device(dp: Dispatcher):
    dp.register_message_handler(cmd_create, text_contains="👤 Аккаунт", state=ParametersStatesGroup.parameter)
    dp.register_message_handler(load_desc, state=AccountStatesGroup.description)
    dp.register_message_handler(load_price, state=AccountStatesGroup.price)
    dp.register_message_handler(photo_confirm, text_contains="✅ Зберігти зображення",
                                state=AccountStatesGroup.photo)
    dp.register_message_handler(load_photo, content_types=types.ContentType.ANY, state=AccountStatesGroup.photo)
    dp.register_message_handler(public_confirm, text_contains="📩 Опублікувати", state=AccountStatesGroup.name)
    dp.register_message_handler(load_name, content_types=types.ContentType.CONTACT, state=AccountStatesGroup.name)
