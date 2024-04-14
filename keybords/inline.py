from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def dice_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Кнопка 1", callback_data="1"),
        types.InlineKeyboardButton(text="Кнопка 2", callback_data="2"),
        types.InlineKeyboardButton(text="Кнопка 3", callback_data="3"),
        types.InlineKeyboardButton(text="Кнопка 4", callback_data="4"),
        types.InlineKeyboardButton(text="Кнопка 5", callback_data="5"),
        types.InlineKeyboardButton(text="Кнопка 6", callback_data="6"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="cancel", width=1),
        width=2
    )
    return builder.as_markup()


def play_again():
    builder = InlineKeyboardBuilder()
    builder.button(text="Сыграть ещё!", callback_data="play_again")
    return builder.as_markup()
