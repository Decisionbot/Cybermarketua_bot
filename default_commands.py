from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from keyboards import get_kb, join_kb, help_kb

from create_bot import db, time_example, chat_id, bot


# создание state (для переодичности в вопросах)
class CooldownStatesGroup(StatesGroup):
    cooldown_timer = State()


# создание state (для переодичности в вопросах)
class ParametersStatesGroup(StatesGroup):
    parameter = State()


# создание state (для переодичности в вопросах)
class DeviceStatesGroup(StatesGroup):
    description = State()
    price = State()
    photo = State()
    name = State()


# создание state (для переодичности в вопросах)
class ItemStatesGroup(StatesGroup):
    game_name = State()
    description = State()
    price = State()
    photo = State()
    name = State()


# создание state (для переодичности в вопросах)
class AccountStatesGroup(StatesGroup):
    description = State()
    price = State()
    photo = State()
    name = State()


# # отмена кнопки Cancel / отмена действий
# @dp.message_handler(text_contains="↪ Повернутися назад", state=CooldownStatesGroup.cooldown_timer)
async def cmd_cancel_none():
    pass


# # проверка кнопки Cancel / отмена действий
# @dp.message_handler(text_contains="↪ Повернутися назад", state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.reply('Ви повернулися назад!',
                        reply_markup=get_kb())
    await ParametersStatesGroup.parameter.set()


# @dp.message_handler(commands=['start'], state=CooldownStatesGroup.cooldown_timer)
async def cmd_start_none(message: types.Message, state: FSMContext) -> None:
    ban = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
    if message.chat.id == message.from_user.id and ban.status != types.ChatMemberStatus.BANNED and ban.status != \
            types.ChatMemberStatus.LEFT:
        left_time = await db.get_time(message.from_user.id)
        if int(left_time) >= time_example:
            await ParametersStatesGroup.parameter.set()
            await message.answer('Запит знову доступний.',
                                 reply_markup=get_kb())
        else:
            left_time_hour = int(((time_example - left_time) / 60) / 60)
            left_time_minute = int(((time_example - left_time) / 60) - left_time_hour * 60)
            left_time_seconds = int(
                ((time_example - left_time) - (left_time_hour * 60) * 60) - left_time_minute * 60)
            if left_time_hour == 0 and left_time_minute != 0:
                await message.answer(f'Запит буде доступний через: {left_time_minute} хв '
                                     f'{left_time_seconds} сек')
            elif left_time_hour == 0 and left_time_minute == 0:
                await message.answer(f'Запит буде доступний через: {left_time_seconds} сек')
            else:
                await message.answer(f'Запит буде доступний через: {left_time_hour} год {left_time_minute} хв '
                                     f'{left_time_seconds} сек')
    elif message.chat.id == message.from_user.id and ban.status == types.ChatMemberStatus.BANNED:
        await state.finish()
        await message.answer(f"Недостатньо прав!",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer(f"Ви були занесені в чорний список!\nЗверніться за допомогою:",
                             reply_markup=help_kb)
    elif message.chat.id == message.from_user.id and ban.status == types.ChatMemberStatus.LEFT:
        await state.finish()
        await message.answer(f"Недостатньо прав!",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer(f"Ви не є учасником каналу!\nНатисніть кнопку нижче:",
                             reply_markup=join_kb)


# ожидание ввода пользователем (start) / вывод кнопки через команду
# @dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    ban = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
    if message.chat.id == message.from_user.id and ban.status != types.ChatMemberStatus.BANNED and ban.status != \
            types.ChatMemberStatus.LEFT:
        await message.answer('Доброго дня, я бот, який допоможе тобі з продажем твого товару. Отже, що продаємо, '
                             'річ з гри, аккаунт або девайс?',
                             reply_markup=get_kb())
        await db.sql_create_time(user_id=message.from_user.id)
        await ParametersStatesGroup.parameter.set()
    elif message.chat.id == message.from_user.id and ban.status == types.ChatMemberStatus.BANNED:
        await state.finish()
        await message.answer(f"Недостатньо прав!",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer(f"Ви були занесені в чорний список!\nЗверніться за допомогою:",
                             reply_markup=help_kb)
    elif message.chat.id == message.from_user.id and ban.status == types.ChatMemberStatus.LEFT:
        await state.finish()
        await message.answer(f"Недостатньо прав!",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer(f"Ви не є учасником каналу!\nНатисніть кнопку нижче:",
                             reply_markup=join_kb)


def register_handlers_def_comm(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel_none, text_contains="↪ Повернутися назад",
                                state=CooldownStatesGroup.cooldown_timer)
    dp.register_message_handler(cmd_cancel, text_contains="↪ Повернутися назад", state='*')
    dp.register_message_handler(cmd_start_none, commands=['start'], state=CooldownStatesGroup.cooldown_timer)
    dp.register_message_handler(cmd_start, commands=['start'])
