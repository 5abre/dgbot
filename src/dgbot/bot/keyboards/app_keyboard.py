from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class AppKeyboard:
    @staticmethod
    def get_app_keyboard() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Скачать", url="https://apps.apple.com/kz/app/dolce-goose-cafe/id6739213566")]])