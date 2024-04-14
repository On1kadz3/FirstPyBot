from aiogram import Router, types, F, Bot
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.formatting import Text, Bold

cmd_router = Router()


@cmd_router.message(Command("start"))
async def cmd_start(message: types.Message):
    content = Text(
        "Добро пожаловать, ",
        Bold(message.from_user.first_name),
        "! \nПропиши /help, чтобы увидеть список команд."
    )
    await message.answer(
        **content.as_kwargs()
    )


# @cmd_router.message(Command("help"))
# async def cmd_help(message: types.Message, ru_com_list: dict):
#     response = 'Список команд\n'
#     for cmd in ru_com_list:
#         response += f"{cmd['command']}: {cmd['description']}\n"
#     await message.answer(response)


# @cmd_router.message(Command("buttons"))
# async def cmd_buttons(message: types.Message):
#     builder = InlineKeyboardBuilder()
#     builder.row(
#         types.InlineKeyboardButton(text="Кнопка 1", callback_data="1"),
#         types.InlineKeyboardButton(text="Кнопка 2", callback_data="2"),
#         types.InlineKeyboardButton(text="Кнопка 3", callback_data="3"),
#         types.InlineKeyboardButton(text="Кнопка 4", callback_data="4"),
#         types.InlineKeyboardButton(text="Кнопка 5", callback_data="5"),
#         types.InlineKeyboardButton(text="Кнопка 6", callback_data="6"),
#         types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back_to_menu", width=1),
#         width=2
#     )
#     await message.answer("Доступные кнопки:", reply_markup=builder.as_markup())


@cmd_router.message(Command("cancel"))
@cmd_router.callback_query(F.data == "cancel")
async def cmd_cancel(event: types.Message | types.CallbackQuery, state: FSMContext, bot: Bot):
    data: types.Message = (await state.get_data()).get("last_message", None)
    if data is not None:
        await bot.delete_message(chat_id=data.chat.id, message_id=data.message_id)
    await state.clear()
    if isinstance(event, types.Message):
        await event.answer("Операция отменена")
        await event.delete()
    else:
        await event.answer()
        await event.message.answer("Операция отменена")
        await event.message.delete()
