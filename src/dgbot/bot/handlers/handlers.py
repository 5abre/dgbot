# import os
# from pathlib import Path
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from datetime import date
from dgbot.bot.keyboards import MainKeyboard, SiteKeyboard, AppKeyboard
from dgbot.backend.services import set_user, get_coupon_by_date, day_check

# media_dir = Path(__file__).parent.parent.parent / "mediafiles"
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer("Добро пожаловать в бота кафе Dolce Goose!",
                        reply_markup=await MainKeyboard.get_main_keyboard())
    
@router.message(F.text == 'Перейти на наш сайт')
async def get_site(message: Message):
    site_photo = "AgACAgIAAxkDAAMZaSR87ypHqu9pN-me3PGnxt8lSpoAAm8Qaxug1yBJzBsxAAEXqcKeAQADAgADdwADNgQ"
    await message.answer_photo(photo=site_photo, 
                        reply_markup=SiteKeyboard.get_site_keyboard())

@router.message(F.text == 'Скачать приложение')
async def get_app(message: Message):
    mobile_photo = "AgACAgIAAxkDAAMSaSR7ujufSr6el2tUXTxGgcsec1gAAmMQaxug1yBJhq7gy1xJK2MBAAMCAAN5AAM2BA"
    await message.answer_photo(photo=mobile_photo,  
                        reply_markup=AppKeyboard.get_app_keyboard())

@router.message(F.text == "Контакты")
async def get_contacts(message: Message):
    channel_text = "<b>Наш телеграмм-канал:</b>\nhttps://t.me/dolcegoose_cafe"
    await message.answer(channel_text, parse_mode="HTML")

@router.message(F.text == "О нас")
async def about_us(message: Message):
    outside_photo = "AgACAgIAAxkDAAMbaSR9Rs9Y-A2SlwVHPifAm08AAbPVAAJyEGsboNcgSfcTuZwwveGjAQADAgADeQADNgQ"

    answer_text = "<b>Dolce Goose cafe</b> - это небольшое семейное кафе на юго-востоке Москвы 🌸\n" \
    "Наша нестандартная концепция уже завоевала сердца многих жителей нашего округа!\n" \
    "Ждём тебя в гости по адресу: ул.Михайлова, д.30А, корп 1 (со стороны 2 подъезда)"

    await message.answer_photo(photo=outside_photo, caption=answer_text, parse_mode="HTML")

@router.message(F.text == 'Получить купон')
async def get_coupon(message:Message):
    today = date.today()
    coupons = await get_coupon_by_date(today)
    check_th_sund = day_check(today)
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


# @router.message(Command('send_photo'))
# async def cmd_photo(message: Message):
#     photo_file = FSInputFile(path=os.path.join(media_dir, 'dg_outside.webp'))
#     msg_id = await message.answer_photo(photo=photo_file, parse_mode="HTML")
#     print(msg_id.photo[-1].file_id)
