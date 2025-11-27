from aiogram import F, Router
from aiogram.types import Message
from dgbot.bot.keyboards import SiteKeyboard, AppKeyboard

router = Router()

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