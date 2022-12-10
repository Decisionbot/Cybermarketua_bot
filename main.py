from aiogram import executor

import default_commands
from create_bot import dp, db

from handlers import device_states, item_states, account_states


async def on_startup(_):
    await db.bd_start()


default_commands.register_handlers_def_comm(dp)
device_states.register_handlers_device(dp)
item_states.register_handlers_device(dp)
account_states.register_handlers_device(dp)


if '__main__' == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
