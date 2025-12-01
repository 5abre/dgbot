import asyncio
import logging
from aiogram import Bot, Dispatcher
from dgbot.core import config
from dgbot.bot.handlers import cp_router, start_router, router, roullete_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info('Starting bot...')
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(router)
    dp.include_router(cp_router)
    dp.include_router(roullete_router)

    
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot error: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())