from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from dgbot.bot.keyboards import MainKeyboard
from dgbot.backend.services import UserService

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await UserService.set_user(message.from_user.id)
    await UserService.update_user_activity(message.from_user.id)
    await message.answer("""<b>Добро пожаловать!</b>🪿☕
                         \nВы общаетесь с ботом Dolce Goose, я сообщу Вам самую актуальную информацию об акциях и скидках, действующих в кафе!""",
                        reply_markup=MainKeyboard.get_main_keyboard(), parse_mode="HTML")