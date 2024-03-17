import asyncio
"""Библиотека для асинхронного запуска бота (!)"""
import logging
"""Библиотека для логгирования, поможет в отладке"""

from aiogram import Bot, Dispatcher
"""aiogram - основной модуль библиотеки aiogram, из которого берем Bot и Dispatcher"""
from aiogram.enums.parse_mode import ParseMode
"""Содержит настройки разметки сообщений (HTML, Markdown)"""
from aiogram.fsm.storage.memory import MemoryStorage
"""Хранилища данных для состояний пользователей"""
from aiogram.utils.chat_action import ChatActionMiddleware

import config
"""Импорт настроект бота, пока токен"""
from handlers import router
"""Внутри handler функционал бота"""

# Функция для запуска бота
async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    # Создаем объект бота с токеном И с разметкой сообщений HTML (чтобы не было экранирования символов)
    dp = Dispatcher(storage=MemoryStorage())
    # Создаем объект диспетчера
    dp.include_router(router)
    # Подключаем к диспетчеру все обработчики, которые используют router
    await bot.delete_webhook(drop_pending_updates=True)
    # Удаляет все обновления, которые произошли после последнего завершения работы бота
    dp.message.middleware(ChatActionMiddleware())
    # Подключение middleware для отправки состояний бота пользователям
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    # Запуск бота


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())