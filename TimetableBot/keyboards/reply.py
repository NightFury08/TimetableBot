from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Расписание"),
            KeyboardButton(text="Заметки")
        ],
        # [
        #     KeyboardButton(text="Напоминания"),
        #     KeyboardButton(text="Личный кабинет")
        # ]
    ],
    resize_keyboard=True
)

spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить гео", request_location=True),
            KeyboardButton(text="Отправить контакт", request_contact=True),
            KeyboardButton(text="Отправить опрос", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="НАЗАД")
        ]
    ],
    resize_keyboard=True
)