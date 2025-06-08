import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import router
from middleware.admin_midl import ErrorHandlerMiddleware


# Экземпляр класса бот
bot = Bot(token=BOT_TOKEN)
# Диспетчер обработки команд
dp = Dispatcher()


async def main():
    # Подключение Роутера
    dp.include_router(router)

    dp.update.middleware(ErrorHandlerMiddleware())

    # Очистка предыдущих обновлений
    await bot.delete_webhook(drop_pending_updates=True)

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход из бота')