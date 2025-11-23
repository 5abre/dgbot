import asyncio
import logging
from aiogram import Bot, Dispatcher
from dgbot.core.config import config
from dgbot.bot.handlers.handlers import router
from dgbot.core.database import async_main


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info('Starting bot...')
    await async_main()
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot error: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())