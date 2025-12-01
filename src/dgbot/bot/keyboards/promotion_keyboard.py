from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class PromotionKeyboard:
    @staticmethod
    def get_promotion_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Получить купон"), KeyboardButton(text="Испытать удачу")],
            [KeyboardButton(text="Мои купоны")], [KeyboardButton(text="Назад")]],
            resize_keyboard=True)