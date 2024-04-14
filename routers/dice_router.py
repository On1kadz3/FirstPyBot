import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from filters.for_dice import FilterForDice

dice_router = Router()


class UserStates(StatesGroup):
    WAITING_FOR_VALUE = State()


@dice_router.message(Command("dice"))
async def cmd_dice(message: types.Message, state: FSMContext):
    await message.answer("Введите значение от 1 до 6 [для отмены пропишите /cancel]:")
    await state.set_state(UserStates.WAITING_FOR_VALUE)


@dice_router.message(FilterForDice(), UserStates.WAITING_FOR_VALUE)
async def cmd_dice1(message: types.Message, state: FSMContext):
    value = message.text
    data = await message.answer_dice(emoji='🎲')
    await asyncio.sleep(3.75)
    await message.answer(f'значение кубика {data.dice.value}')
    if int(value) == data.dice.value:
        await message.answer("Победа!")
    else:
        await message.answer("В следующий раз повезёт!")
    await state.clear()


@dice_router.message(UserStates.WAITING_FOR_VALUE)
async def wrong_num(message: types.Message):
    await message.answer("Неверный ввод, пожалуйства, введите чило от 1 до 6\nДля отмены пропишите /cancel")
