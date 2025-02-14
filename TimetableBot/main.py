from conf import TOKEN

import asyncio
from aiogram import Bot, Dispatcher

from handlers import bot_messages, user_commands, notetimetable
from callbacks import pagination

from data.orm import create_tables
create_tables()

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        notetimetable.router,
        user_commands.router,
        pagination.router,
        bot_messages.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())