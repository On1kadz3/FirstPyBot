from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class FilterForDice(BaseFilter):
    async def __call__(self, event: CallbackQuery) -> Union[bool, Dict[str, Any]]:
        return event.data.isdigit() and int(event.data) in range(1, 7)
