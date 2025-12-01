from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dgbot.backend.services import RouletteService, UserService
from dgbot.bot.keyboards import CouponKeyboard, PromotionKeyboard


roullete_router = Router()


@roullete_router.message(F.text == 'Испытать удачу')
async def try_luck(message: Message):
    try:
        await UserService.update_user_activity(message.from_user.id)

        if not await UserService.check_consecutive(message.from_user.id):
            consecutive_days = await UserService.get_consecutive_days(message.from_user.id)

            await message.answer(
                f"<b>Доступ закрыт</b>\n"
                f"Испытать удачу возможно после 3 дней подряд использования бота\n"
                f"Ваша текущая серия: {consecutive_days}\n"
                f"Осталось <b>{3 - consecutive_days} дней</b>",
                parse_mode="HTML"
            )
            return
        
        coupon = await RouletteService.issue_coupon_to_user(message.from_user.id)
        await UserService.reset_counter(message.from_user.id)


        rarity_info = {
                'common': {'emoji': '🟢', 'name': 'Обычный', 'message': 'Хорошая удача!'},
                'uncommon': {'emoji': '🔵', 'name': 'Необычный', 'message': 'Отличный выигрыш!'},
                'rare': {'emoji': '🟣', 'name': 'Редкий', 'message': 'Невероятно! Вам крупно повезло! 🎉'}
            }
        
        await message.answer(
            f"<b>Поздравляем!</b>\n"
            f"Вы выиграли <b>{coupon.name}</b>\n"
            f"Редкость:{coupon.category}\n"
            f"Купон сохранён в вашей коллекции!",
            parse_mode="HTML"
        )

    except Exception as e:
        await message.answer("Произошла ошибка при выдаче купона.")
        print(f"Roullete error: {e}")

# @roullete_router.message(F.text == "Мои купоны")
# async def show_user_coupons(message: Message):
#     user_coupons = await RouletteService.get_user_coupons(message.from_user.id)
#     if not user_coupons:
#         await message.answer("У вас пока нет купонов")
#         return
    
#     coupons_names = []
#     for user_coupon, roulette_coupon in user_coupons:
#         coupons_names.append(roulette_coupon.name)

#     coupons_text = "<b>Ваши купоны:</b>\n" + "\n".join(
#         f"- <b>{name}</b>" for name in coupons_names
#     )
    
#     await message.answer(coupons_text, parse_mode="HTML", reply_markup=CouponKeyboard.get_coupon_kb())

@roullete_router.message(F.text == "Мои купоны")
async def show_user_coupons(message: Message):
    await UserService.update_user_activity(message.from_user.id)
    user_coupons = await RouletteService.get_user_coupons(message.from_user.id)
    if not user_coupons:
        await message.answer("У вас пока нет активных купонов")
        return
    
    coupons_text = "<b>Ваши активные купоны:</b>\n\n"
    
    for i, (user_coupon, roulette_coupon) in enumerate(user_coupons, 1):
        coupons_text += f"{i}. <b>{roulette_coupon.name}</b>\n"
    
    await message.answer(coupons_text, parse_mode="HTML", reply_markup=CouponKeyboard.get_coupon_kb())

@roullete_router.message(F.text == "Использовать купоны")
async def use_coupon_menu(message: Message):
    await UserService.update_user_activity(message.from_user.id)
    try:
        active_coupons = await RouletteService.get_user_coupons(message.from_user.id)
        
        if not active_coupons:
            await message.answer("У вас нет активных купонов для использования")
            return
        
        keyboard_buttons = []
        for i, (user_coupon, roulette_coupon) in enumerate(active_coupons, 1):
            button_text = f"{i}. {roulette_coupon.name}"
            keyboard_buttons.append([KeyboardButton(text=button_text)])
        
        keyboard_buttons.append([KeyboardButton(text="Вернуться назад")])
        
        use_coupon_kb = ReplyKeyboardMarkup(
            keyboard=keyboard_buttons,
            resize_keyboard=True
        )
        
        await message.answer(
            "Выберите купон для использования:",
            reply_markup=use_coupon_kb
        )
        
    except Exception as e:
        await message.answer("Ошибка при загрузке купонов")
        print(f"Use coupon menu error: {e}")

@roullete_router.message(F.text.regexp(r'^\d+\.'))
async def use_selected_coupon(message: Message):
    try:
        coupon_text = message.text
        coupon_number = int(coupon_text.split('.')[0])
        
        active_coupons = await RouletteService.get_user_coupons(message.from_user.id)
        
        if coupon_number < 1 or coupon_number > len(active_coupons):
            await message.answer("Неверный номер купона")
            return
        
        user_coupon, roulette_coupon = active_coupons[coupon_number - 1]
        
        success = await RouletteService.use_coupon(message.from_user.id, user_coupon.id)
        
        if success:
            await message.answer(
                f"✅ <b>Купон использован!</b>\n\n"
                f"🎁 {roulette_coupon.name}\n"
                f"Приятного использования! 🎉",
                parse_mode='HTML',
                reply_markup=CouponKeyboard.get_coupon_kb()
            )
        else:
            await message.answer(
                "❌ Не удалось использовать купон",
                reply_markup=CouponKeyboard.get_coupon_kb()
            )
            
    except ValueError:
        await message.answer("Неверный формат номера", reply_markup=CouponKeyboard.get_coupon_kb())
    except Exception as e:
        await message.answer("Ошибка при использовании купона", reply_markup=CouponKeyboard.get_coupon_kb())
        print(f"Use selected coupon error: {e}")

@roullete_router.message(F.text == "Вернуться назад")
async def get_back_to_coupon_menu(message: Message):
    await message.answer(text="Выберите действие в меню с акциями", 
        reply_markup=PromotionKeyboard.get_promotion_keyboard())
    
