from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from dgbot.bot.keyboards.main_keyboard import MainKeyboard
from dgbot.bot.keyboards.site_keyboard import SiteKeyboard
from dgbot.bot.keyboards.app_keyboard import AppKeyboard
import dgbot.backend.services.user_service as us
import dgbot.backend.services.coupon_service as cs
from datetime import date



router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await us.set_user(message.from_user.id)
    await message.answer("Добро пожаловать в бота кафе Dolce Goose!", reply_markup=await MainKeyboard.get_main_keyboard())

@router.message(F.text == 'Перейти на наш сайт')
async def get_site(message: Message):
    await message.answer("Вот ссылка на наш сайт:", reply_markup=SiteKeyboard.get_site_keyboard())

@router.message(F.text == 'Скачать приложение')
async def get_app(message: Message):
    await message.answer("Вот ссылка на наше приложение:", reply_markup=AppKeyboard.get_app_keyboard())

@router.message(F.text == "Контакты")
async def get_contacts(message: Message):
    channel_text = "<b>Наш телеграмм-канал:</b>\nhttps://t.me/dolcegoose_cafe"
    await message.answer(channel_text, parse_mode="HTML")

@router.message(F.text == "О нас")
async def about_us(message: Message):
    answer_text = "Мы небольшое кафе, создающее уютную атмосферу и дарящее прекрасное настроение нашим гостям"
    await message.answer_photo(photo="AgACAgIAAxkBAAIBPWkIBblN9onsZoK_na9ud0jtmmZIAAInC2sbcJZBSJK0dPe63Ku3AQADAgADeQADNgQ", caption=answer_text)

@router.message(F.text == 'Получить купон')
async def get_coupon(message:Message):
    today = date.today()
    coupons = await cs.get_coupon_by_date(today)
    check_th_sund = cs.day_check(today)
    response_parts = []

    if coupons:
        coupon_names = [coupon.name for coupon in coupons]
        response_parts.append("Ваша скидка в 26% дейсвует сегодня на:\n"+"\n".join(f"- {name}" for name in coupon_names))
    else:
        response_parts.append("На сегодня купонов нет.")

    if check_th_sund == "thursday":
        response_parts.append("\nСегодня также действует акция Дуэт, при покупке десерта с витрины - кофе 0.3 или чай 0.4 за 150 рублей!")
    elif check_th_sund == "sunday":
        response_parts.append("\nСегодня также действует акция 1+1, при покупке позиции из меню вторая за 50% стоимости!")

    final_response = "\n".join(response_parts)
    await message.answer(final_response)
