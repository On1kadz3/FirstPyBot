import asyncio

from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from keybords.inline import dice_kb, play_again

from filters.for_dice import FilterForDice

dice_router = Router()


@dice_router.message(Command("dice"))
async def cmd_dice(message: types.Message, state: FSMContext):
    await state.update_data(last_message=message)
    await message.answer("Выберите значение от 1 до 6:",
                         reply_markup=dice_kb())
    await message.delete()


@dice_router.callback_query(F.data == "play_again")
async def cmd_dice(event: types.CallbackQuery, state: FSMContext):
    await event.answer()
    await event.message.delete()
    await state.update_data(last_message=event.message)
    await event.message.answer("Выберите значение от 1 до 6:",
                               reply_markup=dice_kb())


@dice_router.callback_query(FilterForDice())
async def cmd_dice1(event: types.CallbackQuery):
    await event.message.delete()
    await event.answer("OK")
    value = event.data
    data = await event.message.answer_dice(emoji='🎲')
    await asyncio.sleep(3.75)
    await event.message.answer(f'значение кубика {data.dice.value}')
    if int(value) == data.dice.value:
        await event.message.answer("Победа!")
    else:
        await event.message.answer("В следующий раз повезёт!")
    await event.message.answer("Сыграем ещё?", reply_markup=play_again())
