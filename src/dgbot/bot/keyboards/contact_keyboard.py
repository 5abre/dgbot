from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class ContactKeyboard:
    @staticmethod
    def get_contact_kb() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="📱Отправить контакт", request_contact=True)]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
            input_field_placeholder="Отправьте ваш контакт")