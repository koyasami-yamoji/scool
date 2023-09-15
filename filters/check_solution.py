from aiogram.filters import Filter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


class CheckSolution(Filter):
    async def __call__(self, message: Message, state: FSMContext) -> bool:
        data = await state.get_data()
        return message.text == data['answer']
