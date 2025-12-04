from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class MainKeyboard:
    @staticmethod
    def get_main_keyboard() -> ReplyKeyboardMarkup:
      return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📅 Узнать акции на сегодня')],
                                                      [KeyboardButton(text='📲 Скачать приложение'),
                                                        KeyboardButton(text='🌐 Наш сайт')],
                                                        [KeyboardButton(text='📞 Контакты'),
                                                         KeyboardButton(text='ℹ️ О нас')]],
                                                         resize_keyboard=True, input_field_placeholder='Выберите необходимое действие.')
        