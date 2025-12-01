from aiogram import Router, F
from aiogram.types import Message
from datetime import date

from dgbot.backend.services import CouponService, UserService
from dgbot.bot.keyboards import MainKeyboard

cp_router = Router()

@cp_router.message(F.text == 'Узнать акции на сегодня')
async def get_coupon(message:Message):    
    today = date.today()
    coupons = await CouponService.get_coupon_by_date(today)
    check_th_sund = CouponService.day_check(today)
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

@cp_router.message(F.contact)
async def handle_contact(message: Message):
    contact = message.contact

    if contact.user_id == message.from_user.id:
        user = await UserService.upd_user(
            tg_id=message.from_user.id,
            phone_number=contact.phone_number
        )
    
    if user:
        await message.answer(
            f"Регистрация успешно завершена! Ваш номер телефона:\n{user.phone_number}",
            reply_markup=MainKeyboard.get_main_keyboard()
        )

# @register_router.message(F.contact)
# async def handle_contact(message: Message):
#     contact = message.contact

#     if contact.user_id == message.from_user.id:
#         await message.answer("Спасибо что отправили ваш контакт!\n"
#                              f"Ваш номер телефона: {contact.phone_number}",
#                              reply_markup=await MainKeyboard.get_main_keyboard())
#         return contact
#     else:
#         await message.answer("Это не ваш контакт!")
#         return None