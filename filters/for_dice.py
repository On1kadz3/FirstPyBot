from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class FilterForDice(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        return message.text.isdigit() and int(message.text) in range(1, 7)
