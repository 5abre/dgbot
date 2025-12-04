from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class AppKeyboard:
    @staticmethod
    def get_app_keyboard() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬇️Скачать в AppStore", url="https://apps.apple.com/ru/app/dolce-goose-cafe/id6739213566")],
            [InlineKeyboardButton(text="⬇️Скачать в RuStore", url="https://www.rustore.ru/catalog/app/com.yumasoft.ypos.dolcegoose.customer")]])