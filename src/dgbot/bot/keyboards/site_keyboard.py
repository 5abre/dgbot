from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class SiteKeyboard:
    @staticmethod
    def get_site_keyboard() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Наш сайт🪿", url="https://dolcegoose.ru")]])