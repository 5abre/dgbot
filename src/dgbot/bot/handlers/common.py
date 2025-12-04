from aiogram import F, Router
from aiogram.types import Message
from dgbot.bot.keyboards import SiteKeyboard, AppKeyboard, PromotionKeyboard, MainKeyboard, ContactKeyboard
from dgbot.backend.services import UserService

router = Router()

@router.message(F.text == '🌐 Наш сайт')
async def get_site(message: Message):
    site_photo = "AgACAgIAAxkDAAMZaSR87ypHqu9pN-me3PGnxt8lSpoAAm8Qaxug1yBJzBsxAAEXqcKeAQADAgADdwADNgQ"
    await message.answer_photo(photo=site_photo, 
                        reply_markup=SiteKeyboard.get_site_keyboard())
    
@router.message(F.text == '📲 Скачать приложение')
async def get_app(message: Message):
    mobile_photo = "AgACAgIAAxkDAAMSaSR7ujufSr6el2tUXTxGgcsec1gAAmMQaxug1yBJhq7gy1xJK2MBAAMCAAN5AAM2BA"
    await message.answer_photo(photo=mobile_photo,  
                        reply_markup=AppKeyboard.get_app_keyboard())

@router.message(F.text == "📞 Контакты")
async def get_contacts(message: Message):
    channel_text = "<b>Наш телеграмм-канал:</b>\nhttps://t.me/dolcegoose_cafe"
    await message.answer(channel_text, parse_mode="HTML")

@router.message(F.text == "ℹ️ О нас")
async def about_us(message: Message):
    outside_photo = "AgACAgIAAxkDAAID52ktWz9QZazvljB0zt3Ozd3WywzxAALlDWsbRQ1pSYDMHP-RBESAAQADAgADdwADNgQ"

    answer_text = "<b>Dolce Goose cafe</b> - небольшое семейное кафе на юго-востоке Москвы 🌸\n" \
    "Наша нестандартная концепция уже завоевала сердца многих жителей нашего округа!\n" \
    "Ждём тебя в гости по адресу: ул.Михайлова, д.30А, корп 1 (со стороны 2 подъезда)"

    await message.answer_photo(photo=outside_photo, caption=answer_text, parse_mode="HTML")



# @router.message(F.text == "Акции")
# async def get_promotions(message:Message):
#     user = await UserService.get_user_by_tg_id(message.from_user.id)

#     if not user.phone_number:
#         await message.answer(
#             "Для получения купонов необходимо зарегистрироваться!\n"
#             "Пожалуйста, поделитесь вашим контактом:",
#             reply_markup=ContactKeyboard.get_contact_kb()
#             )
#         return
    
#     await UserService.update_user_activity(message.from_user.id)
#     await message.answer(
#         text="Выберите действие в меню с акциями", 
#         reply_markup=PromotionKeyboard.get_promotion_keyboard())
    
# @router.message(F.text == "Назад")
# async def get_back_to_main(message:Message):
#     await message.answer(
#         text="Выберите действие в главном меню", 
#         reply_markup=MainKeyboard.get_main_keyboard())
