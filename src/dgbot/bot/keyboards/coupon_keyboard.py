from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

class CouponKeyboard:
    def get_coupon_kb():
        return ReplyKeyboardMarkup(keyboard=
                                   [[KeyboardButton(text="Использовать купоны")],
                                    [KeyboardButton(text="Вернуться назад")]
                                    ], resize_keyboard=True)