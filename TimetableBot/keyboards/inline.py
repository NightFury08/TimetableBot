from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/c/AlexGyverShow"),
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=zamshelyi")
        ]
    ]
)